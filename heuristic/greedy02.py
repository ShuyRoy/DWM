'''
通过读文件得到数据
最初始的贪心，一次下来就得到调度和放置

跑benchmark中的jpeg    536次

跑benchmark中的epic
obj = 935次

rasta   519次
pgp    495
mesa 968
ghostscript 240
mpeg2   1700
pegwit  338

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
        if place[port_p+pm] != -1:
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
    corr_position(e, list0, list2, place, access, sch, port_p, pm)
    return port_p,shift

def right_neibor_position(e,sch,access,list0,list2,port_p,pm,shift):
    sch0 = sch[:]
    i = 0
    while True:
        i = i + 1
        port_pr = port_p + i
        if port_pr < PM :
            if place[port_pr] == -1 and place[port_pr + pm] == -1:
                for a in list0:
                    if access[a] not in place and a not in sch:
                        sch.append(a)
                        place[port_pr] = access[sch[-1]]
                        change_list02(sch[-1], e, list0, list2)
                        find_same(sch, access, e, list0, list2)
                        break
            elif place[port_pr] != -1 and place[port_pr + pm] == -1:
                for a in list0:
                    if access[a] == place[port_pr] and a not in sch:
                        sch.append(a)
                        change_list02(a, e, list0, list2)
                    else:
                        continue
                corr_position(e,list0,list2,place,access,sch,port_pr,pm)
                port_p = check_position(e,sch,list0,list2,port_pr,pm,place,access)
            elif place[port_pr] != -1 and place[port_pr + pm] != -1:
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
    sch = []

    file_path = "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro//pgp"

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

        if data_count%2 == 0:
            P = data_count
            D = data_count
        else:
            P = data_count + 1
            D = data_count
        PM = P // 2
        #print("data",data)

        off = []

        for i in range(PM):
            off.append(i)
        for i in range(PM):
            off.append(i)
        access = data
        # print(N,P,D,off)
        # print(len(access),access)

    content = []
    middle = []
    tmp = []
    sides = []
    with open(file_path + "//pgp4.txt") as file_object:
        for line in file_object:
            content.extend(line.rsplit())
        for i in range(len(content)):
            middle.extend(content[i].split(','))
        tmp = list(map(int, middle))
        #print(tmp)
        i = 0
        while i < len(tmp) - 1:
            sides.append((tmp[i], tmp[i + 1]))
            i += 2
    #print(sides)
    place = [-1] * P
    port_p = 0
    shift = greedy(nodes, sides, sch, place, port_p, PM)
    print(shift)