import numpy


def sqrt_quadratic_sum(x, y, z):
    """
    返回 [sqrt(x1^2 + y1^2 + z1^2), sqrt(x2^2 + y2^2 + z2^2), sqrt(x3^2 + y3^2 + z3^2)]
    :param x:
    :param y:
    :param z:
    :return:
    """
    return numpy.sqrt(x ** 2 + y ** 2 + z ** 2)


def sigmoid(data):
    """
    应用sigmoid函数
    :param data: 一维数组
    :return:
    """
    return 1 / (1 + numpy.exp(-(data - 0.5)))


def diff(data):
    """
    对data差分
    :param data: 一维数组
    :return:
    """
    result = numpy.zeros(len(data) - 1)
    for i in range(1, len(data)):
        result[i - 1] = data[i] - data[i - 1]
    return result


def accuracy(real, count):
    """
    计算准确率
    :param real: 实际值
    :param count: 测量值
    :return:
    """
    return 1 - abs(real - count) / real


def normalization(data):
    size = 12
    result = []

    for i in range(0, len(data), size):
        child = data[i:i + size]
        m = numpy.min(child)
        result.extend(((child - m) / (numpy.max(child) - m)).tolist())

    return numpy.array(result)


def zero_cross(cross_list, origin_data, cross_num=0, show_log=False):
    """
    应用零点穿越算法
    :param cross_list: 穿越的数组
    :param origin_data: 原始数组
    :param cross_num: 穿越值 y
    :param show_log: 是否打印日志
    :return:
    """

    def log(*info):
        if show_log:
            for i, s in enumerate(info):
                print(s, '' if i == len(info) - 1 else ' ', sep='', end='')

    # 结果
    result = 0
    # 穿越状态标记
    cross_flag = 0
    # 总穿越次数
    cross_count = 0
    # 数据点间隔
    interval = 0

    time_fly = 0

    # 是否开始记录间隔
    start_record_interval = False
    # 上次穿越时对应原数据的值
    last_value = 0

    # 走过的数据点间隔阈值
    INTERVAL_MIN = 4
    INTERVAL_MAX = 22

    # 两次穿越间隔阈值
    CROSS_INTERVAL_MIN = 0
    CROSS_INTERVAL_MAX = 0

    # 值差阈值
    DIFF_MIN = 0.00
    DIFF_MAX = 10.5

    for j, val in enumerate(cross_list):
        if j == 0:
            continue

        if j % 20 == 0:
            valid = True

        if start_record_interval:
            interval += 1

        if cross_list[j] < cross_num < cross_list[j - 1] or cross_list[j] > cross_num > cross_list[j - 1]:
            if cross_flag == 0:
                last_value = origin_data[j]
                cross_flag += 1
                start_record_interval = True

            elif cross_flag == 1:
                log('穿越次数', cross_count + 1, '间隔', interval, '差值', abs(last_value - origin_data[j]))
                cross_count += 1

                # 阈值筛选
                if INTERVAL_MIN <= interval <= INTERVAL_MAX and DIFF_MIN <= abs(
                        last_value - origin_data[j]) <= DIFF_MAX:
                    result += 1
                else:
                    log('无效')

                log('\n')
                cross_flag = 0
                interval = 0
                start_record_interval = False

    return result
