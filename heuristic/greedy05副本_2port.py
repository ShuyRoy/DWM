'''
文件读取数据

根据统计次数进行轮换
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
        shift0.append(port_p - port_pl)
        shift_D.append((access[sch0[-1]], access[sch[-1]]))
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
        shift0.append(port_pr - port_p)
        shift_D.append((access[sch0[-1]],access[sch[-1]]))
        port_p = port_pr
    corr_position(e, list0, list2, place, access, sch, port_p, pm)
    return port_p, shift


def greedy(v,e,sch,place,port_p,pm):
    list0, list1, list2 = indegree0(v, e)
    print(list0)
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
def all_cycle(place,PM):
    aplace = copy.deepcopy(place)
    place1 = aplace[0:PM]
    place2 = aplace[PM:]
    for i in range(1):
        place1.insert(0, place1.pop())
        place2.insert(0, place2.pop())
    place0 = place1 + place2
    return place0

#左边单边右移
def l_single_cycle(place,PM):
    aplace = copy.deepcopy(place)
    place1 = aplace[0:PM]
    for i in range(1):
        place1.insert(0, place1.pop())
    return place1

#右边单边右移
def r_single_cycle(place,PM):
    aplace = copy.deepcopy(place)
    place2 = aplace[PM:]
    for i in range(1):
        place2.insert(0, place2.pop())
    return place2

# 数据放置位置变异
def dataPlacement(place,PM,fre):
    aplace = copy.deepcopy(place)
    if fre < PM:
        return all_cycle(aplace,PM)
    elif fre >= PM and fre < 2 * PM:
        return l_single_cycle(aplace,PM) + aplace[PM:]
    else:
        return aplace[0:PM] + r_single_cycle(aplace,PM)



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


def change_place(sch,access,place,shift00,shift_DD):
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
            if first < PM and second >= PM:
                if first + PM >= second:
                    place1 = tmp_place[0:second]
                    place2 = tmp_place[second:first+PM+1]
                    place3 = tmp_place[first+PM+1:]
                    for i in range(first+PM+1 - second):
                        if len(place2):
                            place2.insert(0,place2.pop())
                    place0 = place1 + place2 + place3
                elif first + PM < second:
                    place1 = tmp_place[0:first+PM]
                    place2 = tmp_place[first+PM:second+1]
                    place3 = tmp_place[second+1:]
                    for i in range(1):
                        if len(place2):
                            place2.insert(0, place2.pop())
                    place0 = place1 + place2 + place3
            elif first < PM and second < PM:
                temp = aplace[first + PM]
                aplace[first + PM] = aplace[second]
                aplace[second] = temp
                place1 = tmp_place[0 : first + 1]
                place2 = tmp_place[first + 1 : second + 1]
                place3 = tmp_place[second + 1 :]
                for i in range(1):
                    if len(place2):
                        place2.insert(0, place2.pop())
                place0 = place1 + place2 + place3
                place1 = place0[0 : first + PM + 1]
                place2 = place0[first + PM + 1 : second + PM + 1]
                place3 = place0[second + PM + 1:]
                for i in range(1):
                    if len(place2):
                        place2.insert(0, place2.pop())
                place0 = place1 + place2 + place3
            elif first >= PM and second >= PM:
                temp = aplace[second - PM]
                aplace[second - PM] = aplace[first]
                aplace[first] = temp
                place1 = tmp_place[0 : first - PM + 1]
                place2 = tmp_place[first - PM + 1 : second - PM]
                place3 = tmp_place[second - PM :]
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
    file_path = "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro//mpeg2"

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

    content = []
    middle = []
    tmp = []
    sides = []
    with open(file_path + "//mpeg2-4.txt") as file_object:
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
    shift = greedy(nodes, sides, sch, place, port_p, PM)
    temp_place = copy.deepcopy(place)
    print("sch", sch)
    print("place", place)
    print("shift:", shift)
    print("shift0:",len(shift0),sum(shift0),shift0)
    print("shift_D:",len(shift_D),shift_D)
    #I_D,count,sort_list = count_sch(sch, access)
    #compute_max(sch, access)
    newShift = sumShift( sch, access, PM, shift)
    print("newShift",newShift,shift)
    # compute_max(sch, access, shift0, shift_D)







# "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro\epic"
# epic16

# "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro\jpeg"
# jpeg

# D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro\pegwit
# pegwit16