'''
文件读取数据
调度是入度为0中顺序拿的
根据统计次数进行轮换

4port
'''


import copy

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

# 对应位置都有数据
def not_7(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt + pm7] or access[a] == place[port_pt + pm6] or access[a] == place[port_pt + pm5] or access[a] == place[port_pt + pm4]\
                or access[a] == place[port_pt + pm3] or access[a] == place[port_pt + pm2] or access[a] == place[port_pt + pm1] or \
                access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)

# port7所管辖范围对应位置处没有数据
def not_6(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt + pm5] or access[a] == place[port_pt + pm5] or access[a] == place[port_pt + pm4] or access[a] == place[port_pt + pm3]\
                or access[a] == place[port_pt + pm2] or access[a] == place[port_pt + pm1] or access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt + pm7] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)

# port6、port7所管辖范围对应位置处没有数据
def not_5(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt + pm5] or access[a] == place[port_pt + pm4] or access[a] == place[port_pt + pm3]\
                or access[a] == place[port_pt + pm2] or access[a] == place[port_pt + pm1] or access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm6] == -1:
            sch.append(a)
            place[port_pt + pm6] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt + pm6] and access[a] == place[port_pt + pm7] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)

# port5、port6、port7所管辖范围对应位置处没有数据
def not_4(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt + pm4] or access[a] == place[port_pt + pm3] or access[a] == place[port_pt + pm2]\
                or access[a] == place[port_pt + pm1] or access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm5] == -1:
            sch.append(a)
            place[port_pt + pm5] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm6] == -1:
            sch.append(a)
            place[port_pt + pm6] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt + pm5] and access[a] == place[port_pt + pm6] and access[a] == place[port_pt + pm7] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)


# port4、port5、port6、port7所管辖范围对应位置处没有数据
def not_3(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt + pm3] or access[a] == place[port_pt + pm2] or access[a] == place[port_pt + pm1] or access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm4] == -1:
            sch.append(a)
            place[port_pt + pm4] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm5] == -1:
            sch.append(a)
            place[port_pt + pm5] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm6] == -1:
            sch.append(a)
            place[port_pt + pm6] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt + pm4] and access[a] == place[port_pt + pm5]\
                and access[a] == place[port_pt + pm6] and access[a] == place[port_pt + pm7] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)

# port3、port4、port5、port6、port7所管辖范围对应位置处没有数据
def not_2(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt + pm2] or access[a] == place[port_pt + pm1] or access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm3] == -1:
            sch.append(a)
            place[port_pt + pm3] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm4] == -1:
            sch.append(a)
            place[port_pt + pm4] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm5] == -1:
            sch.append(a)
            place[port_pt + pm5] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm6] == -1:
            sch.append(a)
            place[port_pt + pm6] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt + pm3] and access[a] == place[port_pt + pm4] and access[a] == place[port_pt + pm5]\
                and access[a] == place[port_pt + pm6] and access[a] == place[port_pt + pm7] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)

# port2 和 port3 、port4、port5、port6、port7所管辖范围对应位置处没有数据
def not_1(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt + pm1] or access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm2] == -1:
            sch.append(a)
            place[port_pt + pm2] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm3] == -1:
            sch.append(a)
            place[port_pt + pm3] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm4] == -1:
            sch.append(a)
            place[port_pt + pm4] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm5] == -1:
            sch.append(a)
            place[port_pt + pm5] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm6] == -1:
            sch.append(a)
            place[port_pt + pm6] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt + pm2] or access[a] == place[port_pt+ pm3] \
                and access[a] == place[port_pt + pm4] or access[a] == place[port_pt+ pm5]\
                and access[a] == place[port_pt + pm6] or access[a] == place[port_pt+ pm7]and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)


# port1、port2 和 port3、port4、port5、port6、port7 所管辖范围对应位置处没有数据
def not_0(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] == place[port_pt] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm1] == -1:
            sch.append(a)
            place[port_pt + pm1] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm2] == -1:
            sch.append(a)
            place[port_pt + pm2] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm3] == -1:
            sch.append(a)
            place[port_pt + pm3] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm4] == -1:
            sch.append(a)
            place[port_pt + pm4] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm5] == -1:
            sch.append(a)
            place[port_pt + pm5] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm6] == -1:
            sch.append(a)
            place[port_pt + pm6] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt + pm1] or access[a] == place[port_pt + pm2] or access[a] == place[port_pt + pm3]\
                and access[a] == place[port_pt + pm4] or access[a] == place[port_pt + pm5] or access[a] == place[port_pt + pm6]\
                and access[a] == place[port_pt +pm7] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)

# port0、port1、port2 和 port3、port4、port5、port6、port7 所管辖范围对应位置处都没有数据
def all_none(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt):
    for a in list0:
        if access[a] not in place and a not in sch and place[port_pt] == -1:
            sch.append(a)
            place[port_pt] = access[sch[-1]]
            change_list02(a, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm1] == -1:
            sch.append(a)
            place[port_pt + pm1] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm2] == -1:
            sch.append(a)
            place[port_pt + pm2] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm3] == -1:
            sch.append(a)
            place[port_pt + pm3] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm4] == -1:
            sch.append(a)
            place[port_pt + pm4] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm5] == -1:
            sch.append(a)
            place[port_pt + pm5] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm6] == -1:
            sch.append(a)
            place[port_pt + pm6] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] not in place and a not in sch and place[port_pt + pm7] == -1:
            sch.append(a)
            place[port_pt + pm7] = access[sch[-1]]
            change_list02(sch[-1], e, list0, list2)
            find_same(sch, access, e, list0, list2)
        elif access[a] == place[port_pt] or access[a] == place[port_pt + pm1] or access[a] == place[port_pt + pm2] or access[a] == place[port_pt + pm3]\
                and access[a] == place[port_pt+pm4] or access[a] == place[port_pt + pm5] or access[a] == place[port_pt + pm6] or access[a] == place[port_pt + pm7]\
                and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch, list0)


def corr_position(e,list0,list2,place,port_pt,pm1,pm2,pm3,pm4,pm5,pm6,pm7):
    #sch0 = sch[:]
    if port_pt <pm1:
        print("*****",port_pt,pm1,pm2,pm3,len(place))
        if place[port_pt+pm1] != -1 and place[port_pt+pm2] != -1 and place[port_pt+pm3] != -1 \
                and place[port_pt+pm4] != -1 and place[port_pt+pm5] != -1 and place[port_pt+pm6] != -1 and place[port_pt+pm7] != -1:
            not_7(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pt)    # 对应位置都有数据
        elif place[port_pt+pm1] != -1 and place[port_pt+pm2] != -1 and place[port_pt+pm3] != -1 \
                and place[port_pt+pm4] != -1 and place[port_pt+pm5] != -1 and place[port_pt+pm6] != -1 and place[port_pt+pm7] == -1:
            not_6(e, list0, list2, pm1, pm2, pm3, pm4, pm5, pm6, pm7, port_pt)
        elif place[port_pt+pm1] != -1 and place[port_pt+pm2] != -1 and place[port_pt+pm3] != -1 \
                and place[port_pt+pm4] != -1 and place[port_pt+pm5] != -1 and place[port_pt+pm6] == -1 and place[port_pt+pm7] == -1:
            not_5(e, list0, list2, pm1, pm2, pm3, pm4, pm5, pm6, pm7, port_pt)
        elif place[port_pt+pm1] != -1 and place[port_pt+pm2] != -1 and place[port_pt+pm3] != -1 \
                and place[port_pt+pm4] != -1 and place[port_pt+pm5] == -1 and place[port_pt+pm6] == -1 and place[port_pt+pm7] == -1:
            not_4(e, list0, list2, pm1, pm2, pm3, pm4, pm5, pm6, pm7, port_pt)
        elif place[port_pt+pm1] != -1 and place[port_pt+pm2] != -1 and place[port_pt+pm3] != -1 \
                and place[port_pt+pm4] == -1 and place[port_pt+pm5] == -1 and place[port_pt+pm6] == -1 and place[port_pt+pm7] == -1:
            not_3(e, list0, list2, pm1, pm2, pm3, pm4, pm5, pm6, pm7, port_pt)
        elif place[port_pt+pm1] != -1 and place[port_pt+pm2] != -1 and place[port_pt+pm3] == -1 \
                and place[port_pt+pm4] == -1 and place[port_pt+pm5] == -1 and place[port_pt+pm6] == -1 and place[port_pt+pm7] == -1:
            not_2(e, list0, list2, pm1, pm2, pm3, pm4, pm5, pm6, pm7, port_pt)
        elif place[port_pt+pm1] != -1 and place[port_pt+pm2] == -1 and place[port_pt+pm3] == -1 \
                and place[port_pt+pm4] == -1 and place[port_pt+pm5] == -1 and place[port_pt+pm6] == -1 and place[port_pt+pm7] == -1:
            not_1(e, list0, list2, pm1, pm2, pm3, pm4, pm5, pm6, pm7, port_pt)
        elif place[port_pt+pm1] == -1 and place[port_pt+pm2] == -1 and place[port_pt+pm3] == -1 \
                and place[port_pt+pm4] == -1 and place[port_pt+pm5] == -1 and place[port_pt+pm6] == -1 and place[port_pt+pm7] == -1:
            not_0(e, list0, list2, pm1, pm2, pm3, pm4, pm5, pm6, pm7, port_pt)


#返回来检查在对应位置处的指令调度完之后，是否有访问该位置处数据的指令可以调度
def check_position(e,sch,list0,list2,port_pt,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access):
    while True:
        sch0 = sch[:]
        for a in list0:
            if access[a] == place[port_pt] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_pt+pm1] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_pt+pm2] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_pt+pm3] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_pt+pm4] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_pt+pm5] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_pt+pm6] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)

        for a in list0:
            if access[a] == place[port_pt+pm7] and a not in sch:
                sch.append(a)
                change_list02(a, e, list0, list2)
            else:
                continue
        remove(sch, list0)
        if sch0[-1] == sch[-1]:
            break

    return port_pt

def left_neibor_position(e,list0,list2,sch,port_pt,pm1,pm2,pm3,pm4,pm5,pm6,pm7,shift):
    sch0 = sch[:]
    i = 0
    while True:
        i = i+1
        port_pl = port_pt - i
        if port_pl >= 0:
            for a in list0:
                if access[a] == place[port_pl] or access[a] == place[port_pl + pm1] or access[a] == place[port_pl + pm2]\
                        or access[a] == place[port_pl + pm3] or access[a] == place[port_pl+pm4] or access[a] == place[port_pl + pm5]\
                        or access[a] == place[port_pl + pm6] or access[a] == place[port_pl + pm7]and a not in sch:
                    sch.append(a)
                    change_list02(a, e, list0, list2)
                else:
                    continue
            remove(sch, list0)
        else:
            port_pt,shift = right_neibor_position(e,sch,access,list0,list2,port_pt,pm1,pm2,pm3,pm4,pm5,pm6,pm7,shift)
        if port_pl < 0 or len(sch0) < len(sch):
            break

    if port_pl < 0:
        port_pt = port_pt
    else:
        shift = shift + port_pt - port_pl
        shift0.append(port_pt - port_pl)
        shift_D.append((access[sch0[-1]], access[sch[-1]]))
        port_pt = port_pl
    corr_position(e, list0, list2, place, port_pt, pm1,pm2,pm3,pm4,pm5,pm6,pm7)
    return port_pt,shift

def right_neibor_position(e,sch,access,list0,list2,port_pt,pm1,pm2,pm3,pm4,pm5,pm6,pm7,shift):
    sch0 = sch[:]
    i = 0
    while True:
        i = i + 1
        port_pr = port_pt + i
        if port_pr < PM1 :
            if place[port_pr] == -1 and place[port_pr + pm1] == -1 and place[port_pr + pm2] == -1 and place[port_pr + pm3] == -1 and \
                    place[port_pr+pm4] == -1 and place[port_pr + pm5] == -1 and place[port_pr + pm6] == -1 and place[port_pr + pm7] == -1:
                all_none(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
            elif place[port_pr] != -1 and place[port_pr + pm1] == -1 and place[port_pr + pm2] == -1 and place[port_pr + pm3] == -1 and \
                    place[port_pr+pm4] == -1 and place[port_pr + pm5] == -1 and place[port_pr + pm6] == -1 and place[port_pr + pm7] == -1:
                not_0(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                corr_position(e,list0,list2,sch,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
                port_pt = check_position(e,sch,list0,list2,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm1] != -1 and place[port_pr + pm2] == -1 and place[port_pr + pm3] == -1 and \
                    place[port_pr+pm4] == -1 and place[port_pr + pm5] == -1 and place[port_pr + pm6] == -1 and place[port_pr + pm7] == -1:
                not_1(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                corr_position(e,list0,list2,sch,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
                port_pt = check_position(e,sch,list0,list2,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm1] != -1 and place[port_pr + pm2] != -1 and place[port_pr + pm3] == -1 and \
                    place[port_pr+pm4] == -1 and place[port_pr + pm5] == -1 and place[port_pr + pm6] == -1 and place[port_pr + pm7] == -1:
                not_2(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                corr_position(e,list0,list2,sch,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
                port_pt = check_position(e,sch,list0,list2,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm1] != -1 and place[port_pr + pm2] != -1 and place[port_pr + pm3] != -1 and \
                    place[port_pr+pm4] == -1 and place[port_pr + pm5] == -1 and place[port_pr + pm6] == -1 and place[port_pr + pm7] == -1:
                not_3(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                corr_position(e,list0,list2,sch,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
                port_pt = check_position(e,sch,list0,list2,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm1] != -1 and place[port_pr + pm2] != -1 and place[port_pr + pm3] != -1 and \
                    place[port_pr+pm4] != -1 and place[port_pr + pm5] == -1 and place[port_pr + pm6] == -1 and place[port_pr + pm7] == -1:
                not_4(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                corr_position(e,list0,list2,sch,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
                port_pt = check_position(e,sch,list0,list2,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm1] != -1 and place[port_pr + pm2] != -1 and place[port_pr + pm3] != -1 and \
                    place[port_pr+pm4] != -1 and place[port_pr + pm5] != -1 and place[port_pr + pm6] == -1 and place[port_pr + pm7] == -1:
                not_5(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                corr_position(e,list0,list2,sch,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
                port_pt = check_position(e,sch,list0,list2,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm1] != -1 and place[port_pr + pm2] != -1 and place[port_pr + pm3] != -1 and \
                    place[port_pr+pm4] != -1 and place[port_pr + pm5] != -1 and place[port_pr + pm6] != -1 and place[port_pr + pm7] == -1:
                not_6(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                corr_position(e,list0,list2,sch,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
                port_pt = check_position(e,sch,list0,list2,port_pr,pm1,pm2,pm3,pm4,pm5,pm6,pm7,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm1] != -1 and place[port_pr + pm2] != -1 and place[port_pr + pm3] != -1 and \
                    place[port_pr+pm4] != -1 and place[port_pr + pm5] != -1 and place[port_pr + pm6] != -1 and place[port_pr + pm7] != -1:
                not_7(e,list0,list2,pm1,pm2,pm3,pm4,pm5,pm6,pm7,port_pr)
                remove(sch, list0)
        else:
            break
        if port_pr == pm1 or len(sch0) < len(sch):
            break

    if port_pr == pm1:
        port_pt = port_pt
    else:
        shift = shift + port_pr - port_pt
        shift0.append(port_pr - port_pt)
        shift_D.append((access[sch0[-1]],access[sch[-1]]))
        port_pt = port_pr
    corr_position(e, list0, list2, place, port_pt, pm1,pm2,pm3,pm4,pm5,pm6,pm7)
    return port_pt, shift


def greedy(v,e,sch,place,port_p,pm1,pm2,pm3,pm4,pm5,pm6,pm7):
    list0, list1, list2 = indegree0(v, e)
    print(list0)
    shift = 0
    if len(sch) == 0:
        sch.append(min(list0))
        place[port_p] = access[sch[-1]]
        change_list02(sch[-1], e, list0, list2)
        find_same(sch, access, e, list0, list2)

    while len(sch) < len(v):
        corr_position(e,list0,list2,place,port_p,pm1,pm2,pm3,pm4,pm5,pm6,pm7)
        port_p = check_position(e, sch, list0, list2, port_p, pm1,pm2,pm3,pm4,pm5,pm6,pm7, place, access)
        if port_p != 0:
            port_p, shift = left_neibor_position(e, list0, list2, sch, port_p, pm1,pm2,pm3,pm4,pm5,pm6,pm7, shift)
        else:
            port_p, shift= right_neibor_position(e,sch,access,list0,list2,port_p,pm1,pm2,pm3,pm4,pm5,pm6,pm7,shift)
        # print(sch)
        # print(place)
        print(list0)
    return shift

def count_sch(sch,access):
    sch0 = sch[:]
    I_D = []  # 将连续访问相同数据的指令合为一个指令
    I_D1 = []
    I_D.append(access[sch0[0]])
    for i in sch0:
        I_D1.append(access[sch0[i]])
        for a in access:
            if access[i] == a and a != I_D[-1]:
                I_D.append(a)
                # 统计连续访问的次数
    count = {}
    for i in range(len(I_D) - 1):
        j = i + 1
        key = (I_D[i], I_D[j])
        key1 = (I_D[j], I_D[i])
        if key in count:
            count[key] = count[key] + 1
        elif key1 in count:
            count[key1] = count[key1] + 1
        else:
            count[(I_D[i], I_D[j])] = 1
    print("访问数据顺序合集：", I_D)
    print("访问数据顺序:",I_D1)
    print("访问不同数据的连续次数：", count)
    sort_list = sorted(count.values(), reverse=True)
    print("对访问连续次数排序：",sort_list)
    return I_D,count,sort_list


#整体循环右移
def all_cycle(place,pm1,pm2,pm3):
    aplace = copy.deepcopy(place)
    place1 = aplace[0:pm1]
    place2 = aplace[pm1:pm2]
    place3 = aplace[pm2:pm3]
    place4 = aplace[pm3:]
    for i in range(1):
        place1.insert(0, place1.pop())
        place2.insert(0, place2.pop())
        place3.insert(0, place3.pop())
        place4.insert(0, place4.pop())
    place0 = place1 + place2 + place3 + place4
    return place0

# port0区域单边右移
def single_cycle_0(place,pm1):
    aplace = copy.deepcopy(place)
    place1 = aplace[0:pm1]
    for i in range(1):
        place1.insert(0, place1.pop())
    return place1

# port1区域单边右移
def single_cycle_1(place,pm1,pm2):
    aplace = copy.deepcopy(place)
    place2 = aplace[pm1:pm2]
    for i in range(1):
        place2.insert(0, place2.pop())
    return place2

# port2区域单边右移
def single_cycle_2(place,pm2,pm3):
    aplace = copy.deepcopy(place)
    place3 = aplace[pm2:pm3]
    for i in range(1):
        place3.insert(0, place3.pop())
    return place3

# port3区域单边右移
def single_cycle_3(place,pm3):
    aplace = copy.deepcopy(place)
    place4 = aplace[pm3:]
    for i in range(1):
        place4.insert(0, place4.pop())
    return place4


# 数据放置位置变异
def dataPlacement(place,pm1,pm2,pm3,fre):
    aplace = copy.deepcopy(place)
    if fre < pm1:
        return all_cycle(aplace,pm1,pm2,pm3)
    elif pm1 <= fre < 2*pm1:
        return single_cycle_0(aplace,pm1) + aplace[pm1:]
    elif 2*pm1 <= fre < 3*pm1:
        return aplace[0:pm1] + single_cycle_1(aplace,pm1,pm2) + aplace[pm2:]
    elif 3*pm1 <= fre < 4*pm1:
        return aplace[0:pm2] + single_cycle_2(aplace,pm2,pm3) + aplace[pm3:]
    else:
        return aplace[0:pm3] + single_cycle_3(aplace,pm3)



def compute_max(sch,access,shift00,shift_DD):
    I_D,count,sort_list = count_sch(sch, access)
    mult_result = {}    # 统计连续次数乘移动次数，看其权重，根据改值进行位置调换

    for key in count:
        i = key
        if i in shift_DD:
            t = shift00[shift_DD.index(i)] * count[key]
            mult_result[i] = t
    print(len(mult_result),len(shift00),len(count),mult_result)
    sort_mult = sorted(mult_result.values(), reverse=True)
    print("++++++++++++++++++++++++++++++++++++++++++++++++", sort_mult)
    # sort_shift0 = sorted(shift0, reverse=True)
    return sort_mult,mult_result


def change_place(sch,access,place,shift00,shift_DD,pm1,pm2,pm3):
    aplace = copy.deepcopy(place)
    tmp_place = aplace[:]
    sort_mult,mult_result = compute_max(sch, access,shift00,shift_DD)
    pair = []
    a = 0
    place0 = []
    for key in mult_result:
        if sort_mult[a] == mult_result[key]:
            pair.append(key)
            if aplace.index(pair[0][0]) < aplace.index(pair[0][1]):
                first = aplace.index(pair[0][0])
                second = aplace.index(pair[0][1])
            else:
                first = aplace.index(pair[0][1])
                second = aplace.index(pair[0][0])
            if first < pm1 and pm1 <= second < pm2:
                if first + pm1 >= second:
                    place1 = tmp_place[0:second]
                    place2 = tmp_place[second:first+pm1+1]
                    place3 = tmp_place[first+pm1+1:]
                    for i in range(first+pm1+1 - second):
                        if len(place2):
                            place2.insert(0,place2.pop())
                    place0 = place1 + place2 + place3
                elif first + pm1 < second:
                    place1 = tmp_place[0:first+pm1]
                    place2 = tmp_place[first+pm1:second+1]
                    place3 = tmp_place[second+1:]
                    for i in range(1):
                        if len(place2):
                            place2.insert(0, place2.pop())
                    place0 = place1 + place2 + place3
            elif first < pm1 and second < pm1:
                temp = aplace[first + pm1]
                aplace[first + pm1] = aplace[second]
                aplace[second] = temp
                place1 = tmp_place[0 : first + 1]
                place2 = tmp_place[first + 1 : second + 1]
                place3 = tmp_place[second + 1 :]
                for i in range(1):
                    if len(place2):
                        place2.insert(0, place2.pop())
                place0 = place1 + place2 + place3
                place1 = place0[0 : first + pm1 + 1]
                place2 = place0[first + pm1 + 1 : second + pm1 + 1]
                place3 = place0[second + pm1 + 1:]
                for i in range(1):
                    if len(place2):
                        place2.insert(0, place2.pop())
                place0 = place1 + place2 + place3
            elif first >= pm1 and second >= pm1:
                temp = aplace[second - pm1]
                aplace[second - pm1] = aplace[first]
                aplace[first] = temp
                place1 = tmp_place[0 : first - pm1 + 1]
                place2 = tmp_place[first - pm1 + 1 : second - pm1]
                place3 = tmp_place[second - pm1 :]
                for i in range(1):
                    if len(place2):
                        place2.insert(0, place2.pop())
                place0 = place1 + place2 + place3
                place1 = place0[0 : first]
                place2 = place0[first : second]
                place3 = place0[second:]
                for i in range(second - first - 1):
                    if len(place2):
                        place2.insert(0, place2.pop())
                place0 = place1 + place2 + place3

            print("****",place0)
    return place0


def sumShift(sch,access,PM,shift):
    tmp_shift = shift
    tmp_sch = sch[:]
    frequency = 0
    shift00 = []
    shift_DD = []
    place0 = change_place(sch, access, place,shift0,shift_D)
    k = 0

    while k < 1:
        while frequency < 3*PM:

            temp = 0    # 记录shift次数
            index = 0   # port当前位置
            a = 0   # 从sch中的第0个位置开始找
            i = 0  # 记录步数
            while len(tmp_sch):
                print("temp sch: ", tmp_sch)
                print("place0 lenth: ", len(place0))
                if index + i < PM and access[sch[a]] == place0[index+i]:
                    index += i   # 改变port指向的位置
                    temp += i   # shift次数加i
                    print("11111111111", temp)
                    if i != 0:
                        shift00.append(i)
                        shift_DD.append((access[sch[a-1]],access[sch[a]]))
                    tmp_sch.remove(sch[a])   # 将找过的指令删除
                    i = 0   # 步长归零
                    a += 1
                elif index + i < PM and access[sch[a]]  == place0[index+i + PM]:

                    index += i  # 改变port指向的位置
                    temp += i  # shift次数加i
                    print("2222222222", temp)
                    tmp_sch.remove(sch[a])  # 将找过的指令删除
                    if i != 0:
                        shift00.append(i)
                        shift_DD.append((access[sch[a-1]],access[sch[a]]))
                    i = 0  # 步长归零
                    a += 1
                elif index - i >= 0 and access[sch[a]] == place0[index - i]:

                    index -= i
                    temp += i
                    print("3333333333", temp)
                    if i != 0:
                        shift00.append(i)
                        shift_DD.append((access[sch[a-1]],access[sch[a]]))
                    tmp_sch.remove(sch[a])
                    i = 0
                    a += 1
                elif index - i >= 0 and access[sch[a]] == place0[index - i + PM]:

                    index -= i
                    temp += i
                    print("4444444", temp)
                    if i != 0:
                        shift00.append(i)
                        shift_DD.append((access[sch[a-1]],access[sch[a]]))
                    tmp_sch.remove(sch[a])
                    i = 0
                    a += 1
                else:
                    i += 1
            tmp_sch = sch[:]
            place0 = dataPlacement(place0, PM, frequency)
            print("place: ", place0)
            print(len(place0))
            frequency += 1
            print("))))))))",temp, k, frequency)
            if temp < tmp_shift:
                tmp_shift = temp
        frequency = 0
        k += 1
        place0 = change_place(sch, access, place0,shift00,shift_DD)
    return tmp_shift




if __name__ == "__main__":
    sch = []
    shift0 = []  # 存放连续两个数据需要移动的次数
    shift_D = []  # 存放需要移动的连续的两个数据对
    file_path = "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro//epic"

    # 读取 data
    data = []
    with open(file_path + "//DataA.txt") as file_object:
        for line in file_object:
            data.extend(line.rsplit())

        data = list(map(int, data))
        data_count = 1
        for i in range(1,len(data)):
            for j in range(0,i):
                if data[i] != data[j] and j != i-1:
                    continue
                elif data[i] != data[j] and j == i-1:
                    data_count = data_count + 1
                elif data[i] == data[j]:
                    break
        N = len(data)
        nodes = [i for i in range(N)]
        L = len(data)
        #print(data_count)
        #print(data)

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
        #print("data",data)

        # off = []
        #
        # for i in range(PM):
        #     off.append(i)
        # for i in range(PM):
        #     off.append(i)
        access = data

    content = []
    middle = []
    tmp = []
    sides = []
    with open(file_path + "//epic16.txt") as file_object:
        for line in file_object:
            content.extend(line.rsplit())
        for i in range(len(content)):
            middle.extend(content[i].split(','))
        tmp = list(map(int, middle))
        i = 0
        while i < len(tmp) - 1:
            sides.append((tmp[i], tmp[i + 1]))
            i += 2
    place = [-1] * P
    port_p = 0
    shift = greedy(nodes, sides, sch, place, port_p, PM1,PM2,PM3,PM4,PM5,PM6,PM7)
    temp_place = copy.deepcopy(place)
    print("sch", sch)
    print("place", place)
    print("shift:", shift)
    # print("shift0:",len(shift0),sum(shift0),shift0)
    # print("shift_D:",len(shift_D),shift_D)
    # #I_D,count,sort_list = count_sch(sch, access)
    #compute_max(sch, access)
    # newShift = sumShift( sch, access, PM, shift)
    # print("newShift",newShift,shift)
    # compute_max(sch, access, shift0, shift_D)

