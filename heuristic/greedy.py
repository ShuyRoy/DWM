from random import choice
import sys
sys.setrecursionlimit(1000000000)

#得到入度为0的点
def indegree0(v,e):

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
    if v:
        for t in tmp:
            v.remove(t)
    return tmp,v,degree

#找出与上一步所调度的指令 访问相同数据的指令
def find_same(e,list2,sch,access,list0):
    list00 = list0[:]
    for b in list00:
        if access[b] == access[sch[-1]] and b not in sch:
            sch.append(b)
            list0.remove(b)
            #依赖该点的点的入度减1，为0时，加入到list0中
            for i in range(len(e)):
                if b == e[i][0]:
                    list2[e[i][1]] = list2[e[i][1]] - 1
                    if list2[e[i][1]] == 0:
                        list0.append(e[i][1])
                        if access[e[i][1]] == access[b]:
                            list00.append(e[i][1])
        else:
            continue
    return sch,list0,list2

#找放在上一条指令所访问数据对应位置处数据的指令
def find_corr_position(e,list0,sch,place,access,pm,list2):
    list01 = list0[:]
    # 看上一条指令所访问数据的对应位置
    if place.index(access[sch[-1]]) >= pm:
        if place[place.index(access[sch[-1]]) - pm] != 0:  # 上一条指令所访问数据相对位置处有数据
            # for a in access.index(place[place.index(access[sch[-1]]) - pm]):  #遍历所有访问该数据的指令
            a = choice(access.index(place[place.index(access[sch[-1]]) - pm]))
            if a not in sch and a in list0:  # 访问该数据的指令没有被调度，且入度为0
                sch.append(a)
                list0.remove(a)
                # 依赖该点的点的入度减1，为0时，加入到list0中
                for i in range(len(e)):
                    if a == e[i][0]:
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) - pm] == 0:
            for i in range(len(list0)):
                a = choice(list01)
                if access[a] not in place:   #并且该指令所访问的数据还没有放置过
                    place[place.index(access[sch[-1]]) - pm] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                    for i in range(len(e)):
                        if a == e[i][0]:
                            list2[e[i][1]] = list2[e[i][1]] - 1
                            if list2[e[i][1]] == 0:
                                list0.append(e[i][1])
                break
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
    elif place.index(access[sch[-1]]) < pm:
        if place[place.index(access[sch[-1]]) + pm] != 0:  # 上一条指令所访问数据相对位置处有数据
            # for a in access.index(place[place.index(access[sch[-1]]) + pm]):  #遍历所有访问该数据的指令
            a = choice(access.index(place[place.index(access[sch[-1]]) + pm]))
            if a not in sch and a in list0:  # 访问该数据的指令没有被调度，且入度为0
                sch.append(a)
                list0.remove(a)
                # 依赖该点的点的入度减1，为0时，加入到list0中
                for i in range(len(e)):
                    if a == e[i][0]:
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) + pm] == 0:
            for i in range(len(list0)):
                a = choice(list01)
                if access[a] not in place:
                    place[place.index(access[sch[-1]]) + pm] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                    for i in range(len(e)):
                        if a == e[i][0]:
                            list2[e[i][1]] = list2[e[i][1]] - 1
                            if list2[e[i][1]] == 0:
                                list0.append(e[i][1])
                break
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
    return sch,list0,list2

#找数据放相邻位置的指令
def find_neibor_position(e,list0,list2,sch,place,pm,access,p,shift):
    list02 = list0[:]
    if place.index(access[sch[-1]]) >= pm:
        if (place[place.index(access[sch[-1]]) + 1] != 0 and place.index(access[sch[-1]]) + 1 < p) or (
                place[place.index(access[sch[-1]]) + 1 - pm] != 0 and place.index(access[sch[-1]]) + 1 < pm):  # 看上条指令所访问数据的右边位置或对应位置右边的位置
            list_tmp = access.index(place[place.index(access[sch[-1]]) + 1]) + access.index(place[place.index(access[sch[-1]]) + 1 - pm])
            a = choice(list_tmp)
            if a not in sch and a in list0:  # 访问该数据的指令没有被调度，且入度为0
                sch.append(a)
                list0.remove(a)
                # 依赖该点的点的入度减1，为0时，加入到list0中
                for i in range(len(e)):
                    if a == e[i][0]:
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) + 1] == 0 and place.index(access[sch[-1]]) + 1 < p or (
                place[place.index(access[sch[-1]]) + 1 - pm] == 0 and place.index(access[sch[-1]]) + 1 < pm):
            for i in range(len(list0)):
                a = choice(list02)
                if access[a] not in place:
                    place[place.index(access[sch[-1]]) + 1] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                    for i in range(len(e)):
                        if a == e[i][0]:
                            list2[e[i][1]] = list2[e[i][1]] - 1
                            if list2[e[i][1]] == 0:
                                list0.append(e[i][1])
                break
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) - 1] != 0 and place.index(access[sch[-1]]) - 1 >= pm:  # 看上条指令所访问数据的左边位置
            a = choice(access.index(place[place.index(access[sch[-1]]) - 1]))
            if a not in sch and a in list0:  # 访问该数据的指令没有被调度，且入度为0
                sch.append(a)
                list0.remove(a)
                # 依赖该点的点的入度减1，为0时，加入到list0中
                for i in range(len(e)):
                    if a == e[i][0]:
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) - 1] == 0 and place.index(access[sch[-1]]) - 1 >= pm:
            for i in range(len(list0)):
                a = choice(list02)
                if access[a] not in place:
                    place[place.index(access[sch[-1]]) - 1] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                    for i in range(len(e)):
                        if a == e[i][0]:
                            list2[e[i][1]] = list2[e[i][1]] - 1
                            if list2[e[i][1]] == 0:
                                list0.append(e[i][1])
                break
            sch, list0, list2 = find_same(e, list2, sch, access, list0)

    elif place.index(access[sch[-1]]) < pm:
        if place[place.index(access[sch[-1]]) + 1] != 0 and place.index(access[sch[-1]]) + 1 < pm:  # 看上条指令所访问数据的右边位置
            a = choice(access.index(place[place.index(access[sch[-1]]) + 1]))
            if a not in sch and a in list0:  # 访问该数据的指令没有被调度，且入度为0
                sch.append(a)
                list0.remove(a)
                # 依赖该点的点的入度减1，为0时，加入到list0中
                for i in range(len(e)):
                    if a == e[i][0]:
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) + 1] == 0 and place.index(access[sch[-1]]) + 1 < pm:
            for i in range(len(list0)):
                a = choice(list02)
                if access[a] not in place:
                    place[place.index(access[sch[-1]]) + 1] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                    for i in range(len(e)):
                        if a == e[i][0]:
                            list2[e[i][1]] = list2[e[i][1]] - 1
                            if list2[e[i][1]] == 0:
                                list0.append(e[i][1])
                break
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) - 1] != 0 and place.index(access[sch[-1]]) - 1 >= 0:  # 看上条指令所访问数据的左边位置
            a = choice(access.index(place[place.index(access[sch[-1]]) - 1]))
            if a not in sch and a in list0:  # 访问该数据的指令没有被调度，且入度为0
                sch.append(a)
                list0.remove(a)
                # 依赖该点的点的入度减1，为0时，加入到list0中
                for i in range(len(e)):
                    if a == e[i][0]:
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
            sch, list0, list2 = find_same(e, list2, sch, access, list0)
        elif place[place.index(access[sch[-1]]) - 1] == 0 and place.index(access[sch[-1]]) - 1 >= 0:
            for i in range(len(list0)):
                a = choice(list02)
                if access[a] not in place:
                    place[place.index(access[sch[-1]]) - 1] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                    for i in range(len(e)):
                        if a == e[i][0]:
                            list2[e[i][1]] = list2[e[i][1]] - 1
                            if list2[e[i][1]] == 0:
                                list0.append(e[i][1])
                break
            sch, list0, list2 = find_same(e, list2, sch, access, list0)

    shift = shift + 1
    return sch,list0,list2,shift



def find_diferent_position(v,e,sch,list2,place,pm,shift,access,p,list0):


    #直接在入度为0的列表中找
    for a in list00:
        #如果该点的入度不为0，或者该点被调度过，则直接跳出本次循环，换下一个点
        if a in sch:
            continue
        #当找的点入度为0时
        # a指令访问的数据还没有被放置过
        if access[a] not in place:
            if place.index(access[sch[-1]]) >= pm:
                # 判断上一条指令访问的数据所放置位置的对应位置处是否有空
                if place[place.index(access[sch[-1]]) - pm] == 0:
                    place[place.index(access[sch[-1]]) - pm] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                else:
                    for i in range(0,p-place.index(access[sch[-1]])):
                        for j in range(0,place.index(access[sch[-1]]) -pm):
                            if place[place.index(access[sch[-1]]) + i] == 0 and place.index(access[sch[-1]]) + i < p:  # 否则看上条指令访问数据的位置的右边是否有空
                                place[place.index(access[sch[-1]]) + i] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度
                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                            elif place[place.index(access[sch[-1]]) - pm + i] == 0 and place.index(access[sch[-1]]) - pm + i < pm:  # 否则看上条指令访问数据的位置的对应位置右边是否有空
                                place[place.index(access[sch[-1]]) - pm + i] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度
                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                            elif place[place.index(access[sch[-1]]) - j] == 0 and place.index(
                                access[sch[-1]]) - j >= p:  # 否则看上条指令访问数据的位置的左边是否有空
                                place[place.index(access[sch[-1]]) - j] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度

                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                            elif place[place.index(access[sch[-1]]) - pm + j] == 0 and place.index(
                                access[sch[-1]]) - pm -1 < pm:  # 否则看上条指令访问数据的位置的对应位置左边是否有空
                                place[place.index(access[sch[-1]]) - pm - j] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度
                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                list0.remove(a)  # 删除以调度过的点
                for i in range(len(e)):
                    if a == e[i][0]:
                        print(sch, list2)
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
                            if access[e[i][1]] == access[a]:
                                list00.append(e[i][1])
            elif place.index(access[sch[-1]]) < pm:
                # 判断上一条指令访问的数据所放置位置的对应位置处是否有空
                if place[pm - place.index(access[sch[-1]])] == 0:
                    place[pm - place.index(access[sch[-1]])] = access[a]  # 并且放置
                    sch.append(a)  # 成立则调度
                else:
                    for i in range(0,pm-place.index(access[sch[-1]])):
                        for j in range(0,place.index(access[sch[-1]])):
                            if place[place.index(access[sch[-1]]) + i] == 0 and place.index(access[sch[-1]]) + i < p:  # 否则看上条指令访问数据的位置的右边是否有空
                                place[place.index(access[sch[-1]]) + i] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度
                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                            elif place[place.index(access[sch[-1]]) + pm + i] == 0 and place.index(access[sch[-1]]) + pm + i < pm:  # 否则看上条指令访问数据的位置的对应位置右边是否有空
                                place[place.index(access[sch[-1]]) + pm + i] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度
                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                            elif place[place.index(access[sch[-1]]) +j] == 0 and place.index(access[sch[-1]]) - j >= p:  # 否则看上条指令访问数据的位置的左边是否有空
                                place[place.index(access[sch[-1]]) - j] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度
                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                            elif place[place.index(access[sch[-1]]) + pm + j] == 0 and place.index(access[sch[-1]]) + pm -1 < pm:  # 否则看上条指令访问数据的位置的对应位置左边是否有空
                                place[place.index(access[sch[-1]]) + pm - j] = access[a]  # 并且放置
                                sch.append(a)  # 成立则调度
                                shift = shift + abs(place.index(access[a]) % pm - place.index(access[sch[-2]]) % pm)
                list0.remove(a)  # 删除以调度过的点
                for i in range(len(e)):
                    if a == e[i][0]:
                        print(sch, list00,list2)
                        list2[e[i][1]] = list2[e[i][1]] - 1
                        if list2[e[i][1]] == 0:
                            list0.append(e[i][1])
                            if access[e[i][1]] == access[a]:
                                list00.append(e[i][1])
        sch,list0, list2 = find_same(e, list2, sch, access,list0)
    print(sch)
    print(place)
    print(shift)
    return sch,list2,place,shift



#
def greedy(v,e,p,pm):
    sch = []
    shift = 0
    place = [0]*p
    if v == []:
        return None
    tmp = v[:]
    list0,list1,list2 = indegree0(tmp,e)  #没有入度的节点列表，有入度的节点列表,每个节点的入度数列表
    #在最开始入度为0的点的列表中随机取一个点
    if list0 != None:
        a = choice(list0)
        sch.append(a)
        list0.remove(a)
        for i in range(len(e)):
            if a == e[i][0]:
                list2[e[i][1]] = list2[e[i][1]] - 1
                if list2[e[i][1]] == 0:
                    list0.append(e[i][1])
        place[0] = access[a]    #将第一条指令所访问的数据放在第一个位置

    #取出当前情况下所能取的访问相同数据的点
    sch,list0,list2=find_same(e,list2,sch,access,list0)
    sch,list2,place,shift = find_diferent_position(v,e,sch,list2,place,pm,shift,access,p,list0)



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
    #print(len(sides))

    #print(indegree0(nodes,sides))
    print('ss',greedy(nodes,sides,P,PM))