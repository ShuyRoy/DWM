import copy


file_path = "D:\研究生学习\研究生基础知识储备\数据存储讨论班\论文\exp-1-puremacro\jpeg"

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
    L = len(data)
    print(data_count)
    print(data)

    if data_count%2 == 0:
        P = data_count
        D = data_count
    else:
        P = data_count + 1
        D = data_count
    PM = P // 2
    print(data)

    off = []

    for i in range(PM):
        off.append(i)
    for i in range(PM):
        off.append(i)
    access = data
    print(N,P,D,off)
    print(len(access),access)

# former latter: latter depend on former
content = []
middle = []
former = []
latter = []
with open(file_path + "//jpeg.txt") as file_object:
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
    print(former)
    print(latter)

# layer = []
# used = []
# rest = []
# temp_data = copy.deepcopy(data)
# temp_former = copy.deepcopy(former)
# temp_latter = copy.deepcopy(latter)
# print(len(temp_former))
# print(len(temp_latter))
