'''
最初的贪心
'''
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
    return tmp,v1,degree

#删除入度为0的列表中已经被调度过的指令
def remove(sch,list0):
    for b in sch:
        if b in list0:
            list0.remove(b)


def change_list02(a,e,list0,list2):
    # 依赖该点的点的入度减1，更新list2，为0时，加入到list0中
    for i in range(len(e)):
        if a == e[i][0]:
            list2[e[i][1]] = list2[e[i][1]] - 1
            if list2[e[i][1]] == 0:
                list0.append(e[i][1])

#找到访问相同数据的指令，并将其在list0中删除
def find_same(sch,access,e,list0,list2):
    #sch0 = sch[:]
    for a in list0:
        if access[a] == access[sch[-1]] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch,list0)


def corr_position(e,list0,list2,place,access,sch,port_p,pm):
    #sch0 = sch[:]
    if port_p <pm:
        if place[port_p+pm] != 0:
            for a in list0:
                if access[a] == place[port_p + pm] or access[a] == place[port_p] and a not in sch:
                    sch.append(a)
                    change_list02(a, e, list0, list2)
                else:
                    continue
            remove(sch, list0)
        else:

            for a in list0:
                if access[a] not in place and a not in sch:
                    sch.append(a)
                    place[port_p+pm] = access[sch[-1]]
                    change_list02(sch[-1], e, list0, list2)
                    find_same(sch, access, e, list0, list2)
                    break

#返回来检查在对应位置处的指令调度完之后，是否有访问该位置处数据的指令可以调度
def check_position(e,sch,list0,list2,port_p,pm,place,access):
    while True:
        sch0 = sch[:]
        for a in list0:
            if access[a] == place[port_p] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_p+pm] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)
        if sch0[-1] == sch[-1]:
            break

    return port_p

def left_neibor_position(e,list0,list2,sch,port_p,pm,shift):
    sch0 = sch[:]
    i = 0
    while True:
        i = i+1
        port_pl = port_p - i
        if port_pl >= 0:
            for a in list0:
                if access[a] == place[port_pl] or access[a] == place[port_pl + pm] and a not in sch:
                    sch.append(a)
                    change_list02(a, e, list0, list2)
                else:
                    continue
            remove(sch, list0)

        else:
            port_p,shift = right_neibor_position(e,sch,access,list0,list2,port_p,pm,shift)

        if port_pl < 0 or len(sch0) < len(sch):
            break

    if port_pl < 0:
        port_p = port_p
    else:
        shift = shift + port_p - port_pl
        port_p = port_pl
    return port_p,shift

def right_neibor_position(e,sch,access,list0,list2,port_p,pm,shift):
    sch0 = sch[:]
    i = 0
    while True:
        i = i + 1
        port_pr = port_p + i
        if port_pr < PM:
            if place[port_pr] == 0 and place[port_pr + pm] == 0:
                for a in list0:
                    if access[a] not in place and a not in sch:
                        sch.append(a)
                        place[port_pr] = access[sch[-1]]
                        change_list02(sch[-1], e, list0, list2)
                        find_same(sch, access, e, list0, list2)
                        break
            elif place[port_pr] != 0 and place[port_pr + pm] == 0:
                for a in list0:
                    if access[a] == place[port_pr] and a not in sch:
                        sch.append(a)
                        change_list02(a, e, list0, list2)
                    else:
                        continue
                corr_position(e,list0,list2,place,access,sch,port_p,pm)
                port_p = check_position(e,sch,list0,list2,port_p,pm,place,access)
            elif place[port_pr] != 0 and place[port_pr + pm] != 0:
                for a in list0:
                    if (access[a] == place[port_pr] or access[a] == place[port_pr + pm]) and a not in sch:
                        sch.append(a)
                        change_list02(a, e, list0, list2)
                    else:
                        continue
                remove(sch, list0)
        else:
            break
        if port_pr == pm or len(sch0) < len(sch):
            break

    if port_pr == pm:
        port_p = port_p
    else:
        shift = shift + port_pr - port_p
        port_p = port_pr
    corr_position(e, list0, list2, place, access, sch, port_p, pm)
    return port_p, shift


def greedy(v,e,sch,place,port_p,pm):
    list0, list1, list2 = indegree0(v, e)
    shift = 0
    if len(sch) == 0:
        sch.append(min(list0))
        place[port_p] = access[sch[-1]]
        change_list02(sch[-1], e, list0, list2)
        find_same(sch, access, e, list0, list2)

    while len(sch) < len(v):
        corr_position(e,list0,list2,place,access,sch,port_p,pm)
        port_p = check_position(e, sch, list0, list2, port_p, pm, place, access)
        if port_p != 0:
            port_p, shift = left_neibor_position(e, list0, list2, sch, port_p, pm, shift)
        else:
            port_p, shift= right_neibor_position(e,sch,access,list0,list2,port_p,pm,shift)
        print(sch)
        print(place)
        print(list0)
    return shift



if __name__ == "__main__":
    D = 7
    P = 8
    port = 2
    PM = int(P/port)
    port_p = 0   #port_p永远是小于PM的
    sch = []
    place = [0]*P
    #例子一数据
    # N = 25
    # nodes = [i for i in range(N)]
    # sides = [(0, 1), (2, 3), (4, 5), (1, 10), (1, 6), (3, 7), (5, 8), (5, 11), (5, 15),
    #          (10, 12), (6, 9), (7, 12), (7, 9), (8, 9), (11, 12), (15, 18), (9, 16), (9, 13),
    #          (16, 18), (13, 14), (14, 17), (14, 19), (17, 18), (18, 20), (18, 23), (19, 21),
    #          (20, 21), (23, 24), (21, 22), (22, 24),(12,-1),(24,-1)]
    # access = ['a', 'b', 'a', 'c', 'a', 'd', 'b', 'c', 'd', 'e', 'b', 'd', 'c', 'e', 'f', 'd', 'e', 'f', 'g', 'f', 'g',
    #           'e', 'e', 'g', 'a']
    #例子二数据
    # N = 17
    # nodes = [i for i in range(N)]
    # sides = [(0, 1), (3, 4), (12, 13), (15, 16), (1, 2), (1, 5), (1, 11), (2, 4),
    #          (5, 6), (11, 13), (4, 7), (6, 8), (7, 9), (8, 9), (9, 10), (10,13),(13, 14), (14, 16)]
    # access = ['a', 'b', 'b', 'a', 'c', 'b', 'd', 'c', 'd', 'a', 'a', 'b', 'e', 'f', 'f', 'g', 'a']
    #例子三数据
    N = 25
    nodes = [i for i in range(N)]
    sides = [(0,1),(2,3),(17,18),(1,7),(1,4),(1,9),(3,5),(3,10),(7,8),(4,6),(9,11),(5,6),(10,11),(8,12),(6,14),(11,13),
             (12,15),(14,15),(13,15),(15,22),(15,20),(15,16),(16,18),(20,21),(22,24),(18,19),(19,21),(21,23),(23,24)]
    access = ['a','b','a','c','b','c','d','b','a','b','c','c','a','c','d','e','e','f','b','b','e','g','e','g','f']
    #print(len(sides))
    shift = greedy(nodes,sides,sch,place,port_p,PM)
    print("sch",sch)
    print("place",place)
    print("shift:",shift)