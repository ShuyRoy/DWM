'''
贪心算法
class group 改进
增加 shift
重写 placement 算法，遍历 data placement环 所有情况
增加单独循环右移函数

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
从文本中读取输入
将输入换成：顶点所访问的数据集，所有的边集（依赖）
重写图函数
重写 former latter 生成函数
重写 生成顶点 函数
重写 生成层数 函数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

'''
benchmark: jpeg

ILP
obj: 
running time: 
'''


import copy


def initiate():
    file_path = "D://课程学习//研一下//系统结构与数据存储讨论班//benchmark//exp-1-puremacro//jpeg"

    # 读取 data
    data = []
    with open(file_path + "//DataA.txt") as file_object:
        for line in file_object:
            data.extend(line.rsplit())
        data = list(map(int, data))

    # former latter: latter depend on former
    content = []
    middle = []
    local_former = []
    local_latter = []
    with open(file_path + "//jpeg.txt") as file_object:
        for line in file_object:
            content.extend(line.rsplit())
        for i in range(len(content)):
            middle.extend(content[i].split(','))
        middle = list(map(int, middle))

        index = 0
        while index < len(middle) - 1:
            local_former.append(middle[index])
            local_latter.append(middle[index + 1])
            index += 2

    layer = []
    used = []
    temp_former = copy.deepcopy(local_former)
    temp_latter = copy.deepcopy(local_latter)

    # 输出第一层data
    def first_layer():
        temp = []
        for i in range(len(data)):
            if i not in local_latter and i not in used:
                temp.append(i)

        return temp

    layer.append(first_layer())
    used.extend(first_layer())

    # 更新 former latter
    def update_former_latter(temp_former, temp_latter):
        for i in range(len(data)):
            while i in used and i in temp_former:
                temp_latter.pop(temp_former.index(i))
                temp_former.remove(i)

    update_former_latter(temp_former, temp_latter)

    # 输出剩余层的data
    def rest_layer():
        temp = []
        for i in range(len(data)):
            if i not in temp_latter and i not in used:
                temp.append(i)
        return temp

    while len(used) < len(data):
        update_former_latter(temp_former, temp_latter)
        layer.append(rest_layer())
        used.extend(rest_layer())

    return data, layer


def generate_dic(pair_list):                            # 生成所有顶点对之间的关联度，存在在字典中
    dic = {}
    for i in range(len(pair_list)):
        for f in range(len(pair_list[i])):
            # 遍历同层顶点对
            for s in range(f, len(pair_list[i])):
                if pair_list[i][s] != pair_list[i][f] and (pair_list[i][s], pair_list[i][f]) not in dic \
                        and (pair_list[i][f], pair_list[i][s]) not in dic:
                    dic.update({(pair_list[i][f], pair_list[i][s]): 1})
                elif pair_list[i][s] != pair_list[i][f] and (pair_list[i][s], pair_list[i][f]) in dic:
                    dic.update({(pair_list[i][s], pair_list[i][f]): dic[(pair_list[i][s], pair_list[i][f])] + 1})
                elif pair_list[i][s] != pair_list[i][f] and (pair_list[i][f], pair_list[i][s]) in dic:
                    dic.update({(pair_list[i][f], pair_list[i][s]): dic[(pair_list[i][f], pair_list[i][s])] + 1})
            # 遍历本层与下一层顶点对
            if i + 1 < len(pair_list):
                for s in pair_list[i + 1]:
                    if s != pair_list[i][f] and (s, pair_list[i][f]) not in dic and (pair_list[i][f], s) not in dic:
                        dic.update({(pair_list[i][f], s): 1})
                    elif s != pair_list[i][f] and (s, pair_list[i][f]) in dic:
                        dic.update({(s, pair_list[i][f]): dic[(s, pair_list[i][f])] + 1})
                    elif s != pair_list[i][f] and (pair_list[i][f], s) in dic:
                        dic.update({(pair_list[i][f], s): dic[(pair_list[i][f], s)] + 1})
    return dic


def generate_vertex(data):
    temp = []
    for i in data:
        if i not in temp:
            temp.append(data[i])
    # print("temp: ", temp)
    # print(len(temp))
    return temp


def max_pair(vertex, pair_list):        # 贪心算法计算数据对
    pair_num = len(vertex) // 2
    result = []

    order_list = sorted(pair_list.items(), key=lambda x: x[1], reverse=True)
    print(order_list)
    i = 0
    former = order_list[i][0][0]
    latter = order_list[i][0][1]
    while pair_num > 1:
        i += 1
        if former in vertex and latter in vertex:
            pair_num -= 1
            result.append([former, latter])
            vertex.remove(former)
            vertex.remove(latter)
            # print("former = ", former, "latter = ", latter)
        former = order_list[i][0][0]
        latter = order_list[i][0][1]
        if i >= len(pair_list):
            break

    if not len(vertex):
        return result
    else:
        while len(vertex):
            a = vertex.pop()
            b = vertex.pop()
            result.append([a, b])
        return result


def sumShift(layer_list, max_result):        # 计算总的shift距离
    shift = 9999
    sch = []

    data1, data2 = init_data_placement(max_result)
    # print("data1: ", data1)
    # print("data2: ", data2)
    # print(len(data1))
    # print(len(data2))

    frequency = 0
    while frequency < 2 * len(max_result) - 1:                   # 2 * len(max_result) - 1
        temp = 0
        index = 0
        new_temp_list = copy.deepcopy(layer_list)
        temp_sch = []
        for layer in range(len(new_temp_list)):
            i = 0
            while len(new_temp_list[layer]):
                if index + i < len(data1) and data1[index + i] in new_temp_list[layer]:
                    temp_sch.append(data1[index + i])                       # 保留此次访问顺序
                    new_temp_list[layer].remove(data1[index + i])           # 去除本层已访问过的节点
                    index += i                                              # 指示目前port的位置
                    temp += i                                               # 记录本次移动的距离
                    i = 0                                                   # 步长归零
                elif index + i < len(data2) and data2[index + i] in new_temp_list[layer]:
                    temp_sch.append(data2[index + i])
                    new_temp_list[layer].remove(data2[index + i])
                    index += i
                    temp += i
                    i = 0
                elif index - i >= 0 and data1[index - i] in new_temp_list[layer]:
                    temp_sch.append(data1[index - i])
                    new_temp_list[layer].remove(data1[index - i])
                    index -= i
                    temp += i
                    i = 0
                elif index - i >= 0 and data2[index - i] in new_temp_list[layer]:
                    temp_sch.append(data2[index - i])
                    new_temp_list[layer].remove(data2[index - i])
                    index -= i
                    temp += i
                    i = 0
                else:
                    i += 1
                # print(i)

        if temp < shift:
            shift = temp
            sch = copy.deepcopy(temp_sch)

        data1, data2 = dataPlacement(data1, data2, frequency)
        del new_temp_list
        del temp_sch

        frequency += 1

    print("scheduling sequence: ", end='')
    for i in range(len(sch)):
        print(sch[i], end=' ')
    print()
    print("sch lenth: ", len(sch))

    return shift


def init_data_placement(max_result):            # 初始化data的放置
    data1 = []
    data2 = []
    for i in range(len(max_result)):
        data1.append(max_result[i][0])
        if len(max_result[i]) > 1:
            data2.append(max_result[i][1])
        else:
            data2.append(999)

    return data1, data2


# 随机变异放置
def dataPlacement(data1, data2, count):
    if count < len(data1) - 1:
        return all_loop_right_shift(data1, data2)
    else:
        return single_loop_right_shift(data1, data2)


# 整体循环右移
def all_loop_right_shift(data1, data2):
    for i in range(1):
        data1.insert(0, data1.pop())
        data2.insert(0, data2.pop())

    return data1, data2


# 单个循环右移
def single_loop_right_shift(data1, data2):
    for i in range(1):
        data1.insert(0, data1.pop())
        # data2.insert(0, data2.pop())

    return data1, data2


# 对ILP来说++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 自动生成依赖关系
def generate_former_latter(new_layer_list):
    former = []
    latter = []

    index = 1
    for layer in range(len(new_layer_list) - 1):
        for i in range(index + len(new_layer_list[layer]), len(new_layer_list[layer + 1]) + index + len(new_layer_list[layer])):
            for j in range(index, len(new_layer_list[layer]) + index):
                former.append(j - 1)
                latter.append(i - 1)
        index += len(new_layer_list[layer])

    return former, latter


if __name__ == "__main__":
    data, layer_list = initiate()
    print("data: ", data)
    # print("layer list: ", layer_list)
    temp_data = copy.deepcopy(data)

    for i in range(len(layer_list)):
        for j in range(len(layer_list[i])):
            layer_list[i][j] = data[layer_list[i][j]]

    new_layer_list = copy.deepcopy(layer_list)

    # 每层去重
    temp = []
    for i in range(len(layer_list)):
        temp.append(list(set(layer_list[i])))
    # print("temp: ", temp)

    # print("layer list: ", layer_list)
    temp_list = copy.deepcopy(temp)  # 保存temp副本

    pair_list = generate_dic(temp_list)  # 所有顶点对的相关度
    vertex = generate_vertex(temp_data)  # 所有顶点
    vertex.sort()
    temp_vertex = copy.deepcopy(vertex)  # 保存vertex副本
    # print(vertex)
    max_result = max_pair(temp_vertex, pair_list)  # 局部最大相关对

    print(max_result)

    print()
    sum_shift = sumShift(layer_list, max_result)  # 计算shift次数
    print("Sum of shifting operations: ", sum_shift)

    former, latter = generate_former_latter(new_layer_list)
    print("former: ", former)
    print("latter: ", latter)
    print(len(former))
    print(len(latter))