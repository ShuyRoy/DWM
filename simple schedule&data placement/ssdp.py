'''
简单调度和放置
就是纯顺序
2个port
'''
import copy

def dataplacement(access,port_p):
    data1 = list(set(access))
    # print("len_access",len(access),len(data1))
    for i in range(len(data1)):
        if i% 2 == 0:
            place[port_p] = data1[i]
        else:
            place[port_p+PM] =data1[i]
            port_p += 1
    return place

def sum_shift(sch,place):
    index = 0  # 记录port当前位置
    shift = 0 # 记录次数
    for i in sch:
        tmp_index = place.index(i)    #找到当前指令访问数据的位置
        if tmp_index >= PM:
            tmp_index = tmp_index -PM
            shift =shift + abs(index - tmp_index)    # 用当前头所指位置减去此时要找的数据的位置得到本次要移动的次数
        else:
            shift = shift + abs(index - tmp_index)
        index = tmp_index      # 更新此时头所指的位置
    print("shift",shift)


if __name__ == "__main__":
    # sch = []
    # shift0 = []  # 存放连续两个数据需要移动的次数
    # shift_D = []  # 存放需要移动的连续的两个数据对
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

        # off = []
        #
        # for i in range(PM):
        #     off.append(i)
        # for i in range(PM):
        #     off.append(i)
        access = data      # 数据访问顺序
        sch = copy.deepcopy(access)

    content = []
    middle = []
    tmp = []
    sides = []                   # 存依赖
    with open(file_path + "//rasta16.txt") as file_object:
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
    place1 = dataplacement(access,port_p)
    sum_shift(sch, place1)
    # print("sch",sch)
    # print("place",place)