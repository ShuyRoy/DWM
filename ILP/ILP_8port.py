# coding=UTF-8

'''
取消layer之间的依赖
暂时不需要线性化

benchmark: jpeg
obj =
runtime =
'''

from gurobipy import *


file_path = "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro\pegwit"

# 读取 data
data = []
with open(file_path + "//DataA.txt") as file_object:
    for line in file_object:
        data.extend(line.rsplit())

    data = list(map(int, data))
    DI = len(data)  # 指令的数量
    L = len(data)  # step

    data_count = 1
    for i in range(1, len(data)):
        for j in range(0, i):
            if data[i] != data[j] and j != i - 1:
                continue
            elif data[i] != data[j] and j == i - 1:
                data_count = data_count + 1
            elif data[i] == data[j]:
                break
    if data_count % 8 == 0:
        P = data_count
        D = data_count
    elif data_count % 8 == 1:
        P = data_count + 7
        D = data_count
    elif data_count % 8 == 2:
        P = data_count + 6
        D = data_count
    elif data_count % 8 == 3:
        P = data_count + 5
        D = data_count
    elif data_count % 8 == 4:
        P = data_count + 4
        D = data_count
    elif data_count % 8 == 5:
        P = data_count + 3
        D = data_count
    elif data_count % 8 == 6:
        P = data_count + 2
        D = data_count
    else:
        P = data_count + 1
        D = data_count
    PM1 = P // 8
    PM2 = 2 * (P // 8)
    PM3 = 3 * (P // 8)
    PM4 = 4 * (P // 8)
    PM5 = 5 * (P // 8)
    PM6 = 6 * (P // 8)
    PM7 = 7 * (P // 8)
    #print(data)
    #access = data
    Q = []

    for i in range(PM1):
        Q.append(i)
    for i in range(PM1):
        Q.append(i)
    for i in range(PM1):
        Q.append(i)
    for i in range(PM1):
        Q.append(i)
    for i in range(PM1):
        Q.append(i)
    for i in range(PM1):
        Q.append(i)
    for i in range(PM1):
        Q.append(i)
    for i in range(PM1):
        Q.append(i)
    N = len(Q)
# former latter: latter depend on former
content = []
middle = []
former = []
latter = []
with open(file_path + "//pegwit4.txt") as file_object:
    for line in file_object:
        content.extend(line.rsplit())
    for i in range(len(content)):
        middle.extend(content[i].split(','))
    middle = list(map(int, middle))

    index = 0
    while index < len(middle) - 1:
        former.append(middle[index])
        latter.append(middle[index + 1])
        index += 2


def cor(i):
    return data[i]


try:
    m = Model("dwm026")

    Xil = m.addVars(DI, L, vtype=GRB.BINARY, name="step_l")
    Pdn = m.addVars(D, N, vtype=GRB.BINARY, name="block_n")
    Ins = m.addVars(DI, vtype=GRB.INTEGER, name="instruction_i")
    Off = m.addVars(DI, vtype=GRB.INTEGER, name="offset")
    Pla = m.addVars(L, vtype=GRB.INTEGER, name="placement")
    Abs = m.addVars(L, vtype=GRB.INTEGER, name="absolute")

    m.setObjective(Pla[0] + quicksum(Abs[l] for l in range(L - 1)), GRB.MINIMIZE)

    # Xil 在每一步只能有1个instruction
    # Xil 在每个指令处只能占1个step
    m.addConstrs((Xil.sum('*', j)) == 1 for j in range(L))
    m.addConstrs((Xil.sum(i, '*')) == 1 for i in range(DI))

    # Pdn 每个data只能有1个placement
    # Pdn 每个placement中最多有1个data
    m.addConstrs((Pdn.sum('*', j)) <= 1 for j in range(N))
    m.addConstrs((Pdn.sum(i, '*')) == 1 for i in range(D))

    # m.update()

    # Ins[i] 指令i所在的step
    for i in range(DI):
        for j in range(L):
            m.addConstr((Xil[i, j] == 1) >> (Ins[i] == j))

    # dependence: later depend on former
    # Ins[former[i]] <= Ins[later[i]]
    for i in range(len(former)):
        m.addConstr(Ins[former[i]], GRB.LESS_EQUAL, Ins[latter[i]])

    # offset
    for i in range(DI):
        m.addConstr(Off[i] == quicksum(Pdn[cor(i), n] * Q[n] for n in range(N)))

    # placement sequence
    # Pla[l] = Off[i], if Xil[i, l] = 1
    for l in range(L):
        for i in range(DI):
            m.addConstr((Xil[i, l] == 1) >> (Pla[l] == Off[i]))

    # Abs[l] = |Pla[l + 1] - Pla[l]|
    for l in range(L - 1):
        m.addConstr(Abs[l] >= Pla[l + 1] - Pla[l])
        m.addConstr(Abs[l] >= Pla[l] - Pla[l + 1])

    # m.setParam(GRB.Param.TimeLimit, 1800)
    m.optimize()
    # m.terminate()

    # if m.SolCount > 0:
    #     for v in m.getVars():
    #         print("obj1111",Abs)



    # 为什么约束不住？？？？？？？？？？？？？？？？？
    # for i in range(DI):
    #     for l in range(L):
    #         if Xil[i, l] == 1:
    #             print("Xil[", i, "][", l, "]: ", Xil[i, l])
    print("Xil: ", Xil)
    print("Off: ", Off)
    print("Pdn: ", Pdn)
    print("Ins: ", Ins)
    print("Pla: ", Pla)
    print('Obj: %g' % m.objVal)


except GurobiError as e:
    print('Error code ' + str(e.message) + ": " + str(e))

except AttributeError as e:
    print("Encountered an attribute error" + str(e.args) + ": " + str(e))

