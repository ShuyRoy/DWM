
#得到入度为0的点
def indegree0(v,e):
    v1 = v[:]
    if v == []:
        return None
    tmp = v[:]
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])
    if tmp ==[]:
        return -1

    degree=[0] * len(v)
    for t in v:
         for i in range(len(e)):
            if t == e[i][1]:
                 degree[t] = degree[t]+1
    if v1:
        for t in tmp:
            v1.remove(t)
    print(degree)
    return tmp,v1,degree

def greedy_sch(v,e,sch):
    list0,list1,list2 = indegree0(v,e)
    while len(sch) < len(v):
        if len(list0) > 1:
            sch.append(min(list0))
        elif len(list0) == 1:
            sch.append(list0[0])
        for i in range(len(e)):
            if sch[-1] == e[i][0]:
                list2[e[i][1]] = list2[e[i][1]] - 1
                if list2[e[i][1]] == 0:
                    list0.append(e[i][1])
        for a in list0:
            print(list0)
            if access[a] == access[sch[-1]] and a not in sch:
                sch.append(a)
                # 依赖该点的点的入度减1，为0时，加入到list0中
                for i in range(len(e)):
                    if a == e[i][0]:
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
            else:
                continue
        for b in sch:
            if b in list0:
                list0.remove(b)
    return sch


if __name__ == "__main__":

    N = 25
    D = 7
    P = 8
    PM = int(P/2)
    shift = 0
    sch = []
    offset = [0, 1, 2, 3, 0, 1, 2, 3]
    nodes = [i for i in range(N)]
    sides = [(0, 1), (2, 3), (4, 5), (1, 10), (1, 6), (3, 7), (5, 8), (5, 11), (5, 15),
             (10, 12), (6, 9), (7, 12), (7, 9), (8, 9), (11, 12), (15, 18), (9, 16), (9, 13),
             (16, 18), (13, 14), (14, 17), (14, 19), (17, 18), (18, 20), (18, 23), (19, 21),
             (20, 21), (23, 24), (21, 22), (22, 24)]
    access = ['a', 'b', 'a', 'c', 'a', 'd', 'b', 'c', 'd', 'e', 'b', 'd', 'c', 'e', 'f', 'd', 'e', 'f', 'g', 'f', 'g',
              'e', 'e', 'g', 'a']
    greedy_sch(nodes, sides, sch)