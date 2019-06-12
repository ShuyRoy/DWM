'''
陈咸彰的算法

4个port
'''

# from python import *
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

def find_same(sch,access,e,list0,list2):
    for a in list0:
        if access[a] == access[sch[-1]] and a not in sch:
            sch.append(a)
            change_list02(a, e, list0, list2)
        else:
            continue
    remove(sch,list0)

def generate_sch(v,e,access):
    sch = []
    data_sch = []
    list0,list1,list2 = indegree0(v,e)

    while len(sch) < len(v):
        sch.append(min(list0))
        change_list02(sch[-1], e, list0, list2)
        find_same(sch, access, e, list0, list2)
    for i in sch:
        data_sch.append(access[i])
    return sch,data_sch

def grouping(access):
    sch, data_sch = generate_sch(nodes, sides, access)
    I_D = []  # 将连续访问相同数据的指令合为一个指令
    I_D1= []   #存储访问数据的顺序
    I_D.append(access[sch[0]])

    for i in sch:
        I_D1.append(access[i])
        for a in access:
            if access[i] == a and a != I_D[-1]:
                I_D.append(a)

    # 统计每对数据连续访问的次数
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

    # 将访问的数据去重并且排序
    data_list = list(set(copy.deepcopy(access)))
    data_list.sort()

    # 统计每个节点的权重,并降序排序权重
    weight = []
    # w = []
    t = 0
    for d in data_list:
        for key in count:
            if d in key:
                # print(count[key])
                t = t + count[key]
        # w.append(t)
        weight.append((d,t))     #每个数据节点的权重,存储结构为  （数据，权重）
        t = 0
    Q = sorted(weight,key=lambda x: (-x[1], x[0]))    #将权重降序排序
    # print("sch",sch)
    # print("I_D1",I_D1)
    # print("count",count)
    # print("I_D",I_D)
    # print("weight",weight)
    print("Q",Q)

    # 开始分组
    # 4个port 所以一组有4个数据,一共可以分len(place)//4或len(place)//4 +1 组  一行是一组  多少列就表示一组多少数据  多少行表示多少组
    Q1 = copy.deepcopy(Q)
    col = len(place)//PM1
    tmp_row = len(place)//4
    if len(place) > tmp_row * 4:
        row = tmp_row + 1
    else:
        row = tmp_row
    gx = [[-1]*col for j in range(row)]        #每一行存一组
    i = 0
    gth = 0  # 用来统计是每组的第几个，即在哪个port所管辖区域
    while len(Q1):
        for x in range(row):   #一共可以分PM组
            if len(Q1) > 0:
                a = Q[i][0]
                gx[x][gth] = a    # 将a放在x组中
                Q1.remove(Q[i])
                i += 1
        gth += 1
    print(gx)

    group_weight = []   # 统计每个组的权重
    tmp_w = 0
    for group in gx:
        j = gx.index(group)
        for i in group:
            if i != -1:
                tmp_w = tmp_w + Q[j][1]
                # print("tmp_w",tmp_w)
                j = j + PM1
        group_weight.append(tmp_w)
        tmp_w = 0
    print("group_weight",group_weight)  # 每组的权重

    g_w = {}
    for i in range(len(gx)):
        a = tuple(gx[i])
        # print(a)
        g_w[a] = group_weight[i]

    # 按字典中的值排序 即按照权重排序  好像本来也不用排 因为之前的权重和就是递减的  不过就留着吧
    sorted_gw =  sorted(g_w.items(), key=lambda item: item[1], reverse=True)

    # print("g_w_sort",g_w)
    print("sorted_gw",sorted_gw)

    # 开始对每组进行放置
    index = PM1//2   # port初始位置在中间
    i = 0
    for key in g_w:
        if index < PM1 and index >= 0:
            place[index] = key[0]
            place[index + PM1] = key[1]
            place[index + PM2] = key[2]
            place[index + PM3] = key[3]
        # tmp_index = index   #
        i = i + 1
        if i%2 == 0:
            index = index + i
        else:
            index = index - i
    print("place",place)
    return sch,place

def sumShift(sch,place):
    index = 0  # 记录port当前位置
    shift = 0 # 记录次数
    for i in sch:
        tmp_index = place.index(access[i])    #找到当前指令访问数据的位置
        if PM1 <= tmp_index < PM2:
            tmp_index = tmp_index -PM1
            shift =shift + abs(index - tmp_index)    # 用当前头所指位置减去此时要找的数据的位置得到本次要移动的次数
        elif PM2<= tmp_index <PM3:
            tmp_index = tmp_index - PM2
            shift = shift + abs(index - tmp_index)  # 用当前头所指位置减去此时要找的数据的位置得到本次要移动的次数
        elif tmp_index>=PM3:
            tmp_index = tmp_index - PM3
            shift = shift + abs(index - tmp_index)  # 用当前头所指位置减去此时要找的数据的位置得到本次要移动的次数
        else:
            shift = shift + abs(index - tmp_index)
        index = tmp_index      # 更新此时头所指的位置
    print("shift",shift)








if __name__ == "__main__":
    file_path = "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro//rasta"

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

        if data_count % 4 == 0:
            P = data_count
            D = data_count
        elif data_count % 4 == 1:
            P = data_count + 3
            D = data_count
        elif data_count % 4 == 2:
            P = data_count + 2
            D = data_count
        else:
            P = data_count + 1
            D = data_count
        PM1 = P // 4
        PM2 = P // 2
        PM3 = P - P // 4
        # off = []
        #
        # for i in range(PM):
        #     off.append(i)
        # for i in range(PM):
        #     off.append(i)
        access = copy.deepcopy(data)

    content = []
    middle = []
    tmp = []
    sides = []
    with open(file_path + "//rasta4.txt") as file_object:
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

    sch,place1 = grouping( access)
    print(sch)
    print(place)
    sumShift(sch, place1)
    # sch,data_sch = generate_sch(nodes, sides,access)
    # print(sch)
    # print(data_sch)
