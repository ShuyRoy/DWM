from gurobipy import *

N = 8
D = 8
DI = 17
L = 17

data = [2, 4, 1, 3, 5, 6, 3, 7, 8, 2, 4, 6, 4, 2, 8, 5, 7]
placement = [0, 1, 2, 3, 4, 5, 6, 7]
pred = {
    1: [1, 3], 2: [1, 4], 3: [2, 3], 4: [2, 4], 5: [3, 5], 6: [3, 6], 7: [3, 7], 8: [3, 8], 9: [3, 9],
    10: [4, 5], 11: [4, 6], 12: [4, 7], 13: [4, 8], 14: [4, 9], 16: [5, 10], 17: [5, 11],
    18: [6, 10], 19: [6, 11], 20: [7, 10], 21: [7, 11], 22: [8, 10], 23: [8, 11], 24: [9, 10], 25: [9, 11],
    26: [10, 12], 27: [10, 13], 28: [10, 14], 29: [10, 15], 30: [11, 12], 31: [11, 13], 32: [11, 14], 33: [11, 15],
    34: [12, 16], 35: [12, 17], 36: [13, 16], 37: [13, 17], 38: [14, 16], 39: [14, 17], 40: [15, 16], 41: [15, 17]
        }


def cor(i):
    return data[i]


try:
    m = Model("dwm007")

    Xil = m.addVars(DI, L, vtype=GRB.BINARY, name="step_l")
    Pdn = m.addVars(D, N, vtype=GRB.BINARY, name="block_n")
    Ins = m.addVars(DI, vtype=GRB.INTEGER, name="instruction_i")
    Seq = m.addVars(L, vtype=GRB.INTEGER, name="sequence")
    #Sij = m.addVars(DI, DI, vtype=GRB.BINARY, name="if_sequence")
    #Cons = m.addVars(DI, DI, vtype=GRB.INTEGER, name="obj_constrains")
    New = m.addVars(DI, vtype=GRB.INTEGER, name="instead_var")

    m.setObjective(quicksum(New[i] for i in range(DI)), GRB.MINIMIZE)

    m.addConstrs(quicksum(Xil.select('*', j)) == 1 for j in range(L))
    m.addConstrs(quicksum(Xil.select(i, '*')) == 1 for i in range(DI))
    m.addConstrs(quicksum(Pdn.select('*', j)) == 1 for j in range(N))
    m.addConstrs(quicksum(Pdn.select(i, '*')) == 1 for i in range(D))

    m.update()

    for i in range(DI):
        Ins[i] = quicksum(Xil[i, j] * j for j in range(L))

    #for i, j in pred.items():
        #Ins.select(i) < Ins.select(j)

    #m.addConstrs(Ins[pred[i][0]] < Ins[pred[i][1]] for i in pred.items())
    m.addConstrs(Ins[i] < Ins[j] for key in pred if (i == pred[key][0]) and (j == pred[key][1]))

    m.addConstrs(abs_(quicksum(Pdn[Seq[i + 1], n] * placement[n] for n in range(N))
                      - quicksum(Pdn[Seq[i], m] * placement[m] for m in range(N))) == New[i] for i in range(DI - 1))

    '''
    for i in range(DI):
        for j in range(DI):
            for l in range(L - 1):
                if (l + 1) * Xil.get(j, l + 1) - l * Xil.get(i, l) == 1:
                    Sij[i, j] = 1
                else:
                    Sij[i, j] = 0
    '''

    for i in range(DI):
        for j in range(DI):
            if Xil[i, j] == 1:
                Seq[j] = cor(i)

    m.optimize()

    print('Obj: %g' % m.objVal)
    #print(Sij)
    print(Seq)
    print(Xil)
    print(Pdn)
    print(Ins)


except GurobiError as e:
    print('Error code ' + str(e.message) + ": " + str(e))

except AttributeError as e:
    print("Encountered an attribute error" + str(e.args) + ": " + str(e))