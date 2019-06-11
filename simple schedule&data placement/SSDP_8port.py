'''
简单调度和放置
就是纯顺序
8个port
'''
import copy

def dataplacement(access,port_p):
    data1 = list(set(access))
    # print("len_access",len(access),len(data1))
    for i in range(len(data1)):
        if i% 8 == 0:
            place[port_p] = data1[i]
        elif i% 8 == 1:
            place[port_p+PM1] = data1[i]
            # port_p += 1
        elif i%8 == 2:
            place[port_p + PM2] = data1[i]
            # port_p += 1
        elif i%8 == 3:
            place[port_p + PM3] = data1[i]
        elif i % 8 == 4:
            place[port_p + PM4] = data1[i]
        elif i % 8 == 5:
            place[port_p + PM5] = data1[i]
        elif i % 8 == 6:
            place[port_p + PM6] = data1[i]
        elif i % 8 == 7:
            place[port_p + PM7] = data1[i]
            port_p += 1
    return place

def sum_shift(sch,place):
    index = 0  # 记录port当前位置
    shift = 0 # 记录次数
    for i in sch:
        tmp_index = place.index(i)    #找到当前指令访问数据的位置
        if PM1 <= tmp_index < PM2:
            tmp_index = tmp_index -PM1
            shift =shift + abs(index - tmp_index)    # 用当前头所指位置减去此时要找的数据的位置得到本次要移动的次数
        elif PM2<= tmp_index <PM3:
            tmp_index = tmp_index - PM2
            shift = shift + abs(index - tmp_index)  # 用当前头所指位置减去此时要找的数据的位置得到本次要移动的次数
        elif PM3<= tmp_index <PM4:
            tmp_index = tmp_index - PM3
            shift = shift + abs(index - tmp_index)
        elif PM4<= tmp_index <PM5:
            tmp_index = tmp_index - PM4
            shift = shift + abs(index - tmp_index)
        elif PM5<= tmp_index <PM6:
            tmp_index = tmp_index - PM5
            shift = shift + abs(index - tmp_index)
        elif PM6<= tmp_index <PM7:
            tmp_index = tmp_index - PM6
            shift = shift + abs(index - tmp_index)
        elif tmp_index>=PM7:
            tmp_index = tmp_index - PM7
            shift = shift + abs(index - tmp_index)  # 用当前头所指位置减去此时要找的数据的位置得到本次要移动的次数
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

        if data_count%8 == 0:
            P = data_count
            D = data_count
        elif data_count%8 == 1:
            P = data_count + 7
            D = data_count
        elif data_count%8 == 2:
            P = data_count + 6
            D = data_count
        elif data_count%8 == 3:
            P = data_count + 5
            D = data_count
        elif data_count%8 == 4:
            P = data_count + 4
            D = data_count
        elif data_count%8 == 5:
            P = data_count + 3
            D = data_count
        elif data_count%8 == 6:
            P = data_count + 2
            D = data_count
        else:
            P = data_count + 1
            D = data_count
        PM1 = P // 8
        PM2 = 2*(P // 8)
        PM3 = 3*(P // 8)
        PM4 = 4*(P // 8)
        PM5 = 5*(P // 8)
        PM6 = 6*(P // 8)
        PM7 = 7*(P // 8)
        print(PM1,PM2,PM3,PM4,PM5,PM6,PM7)

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
    place1 = dataplacement(access,port_p)
    sum_shift(sch, place1)
    # print("sch",sch)
    # print("place",place)