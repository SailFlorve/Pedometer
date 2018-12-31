import copy
import math

import numpy

import filter


class DataSeriesProcessor:
    data = []

    def __init__(self, data):
        self.data = data

    def get_current(self):
        return copy.copy(self.data)

    def set_current(self, data):
        self.data = data

    def log(self, base=10):
        for i, val in enumerate(self.data):
            self.data[i] = math.log(val) / math.log(base)
        return self

    def low_pass_filter(self, weight=0.1):
        self.data = filter.low_pass_filter(self.data, weight)
        return self

    def diff(self):
        self.data = get_diff(self.data)
        return self

    def sigmoid(self):
        self.data = get_sigmoid(self.data)
        return self

    def __sub__(self, other):
        for i, val in enumerate(self.data):
            self.data[i] = val - other
        return self.data

    def __mul__(self, other):
        for i, val in enumerate(self.data):
            self.data[i] = val * other
        return self


def sqrt_quadratic_sum(list):
    """
    将测量数据平方相加，再开根号\n
    :param list: 含有xyz数组的list:[[x1,y1,z1],[x2,y2,z2],...]
    :return: [sqrt(x1^2 + y1^2 + z1^2), sqrt(x2^2 + y2^2 + z2^2), ...]
    """
    result = []
    for child_list in list:
        result.append(math.sqrt(child_list[0] ** 2 + child_list[1] ** 2 + child_list[2] ** 2))
    return result


def get_sigmoid(list, mid=0):
    return [1 / (1 + math.exp(-(val - mid) * 1.5)) for i, val in enumerate(list)]


def get_normalization(list):
    arr = numpy.array(list)
    return []


def reduce_gravity(triaxial):
    alpha = 0.8
    gravity = [0, 0, 0]
    result = []
    for i, val in enumerate(triaxial):
        temp_result = [0, 0, 0]
        gravity[0] = alpha * gravity[0] + (1 - alpha) * val[0]
        gravity[1] = alpha * gravity[1] + (1 - alpha) * val[1]
        gravity[2] = alpha * gravity[2] + (1 - alpha) * val[2]
        temp_result[0] = val[0] - gravity[0]
        temp_result[1] = val[1] - gravity[1]
        temp_result[2] = val[2] - gravity[2]
        result.append(temp_result)
    return result


def get_log(data_list):
    result = []
    for i, val in enumerate(data_list):
        result.append(math.log(val))
    return result


def get_diff(data_list):
    result = []
    for i in range(1, len(data_list)):
        result.append(data_list[i] - data_list[i - 1])
    return result


def count_step(diff_list, origin_data, cross_num=0):
    result = 0

    cross = 0
    cross_count = 0
    interval = 0

    start_record_interval = False

    last_value = 0

    for j, val in enumerate(diff_list):
        if j == 0:
            continue

        # 1.刚穿了一个点，cross = 0，cross + 1, 开始记录间隔。
        # 2.穿了第二个点，如果间隔正确，步数+1。清除穿越数字。

        if start_record_interval:
            interval += 1

        if diff_list[j] < cross_num < diff_list[j - 1] or diff_list[j] > cross_num > diff_list[j - 1]:
            if cross == 0:
                last_value = origin_data[j]
                cross += 1
                start_record_interval = True

            elif cross == 1:
                # print(cross_count + 1, interval, abs(last_value - origin_data[j]), end=' ')
                cross_count += 1
                if 3 <= interval <= 15 and 0.00 <= abs(last_value - origin_data[j]) <= 2:
                    result += 1
                    # print('')
                else:
                    pass
                    # print('无效')

                cross = 0
                interval = 0
                start_record_interval = False

    # if cross != 0:
    #     # print("剩余一点未穿，步数+1.")
    #     result += 1

    return result
