import numpy


def kalman_filter(value_list, Q=1e-5, R=0.01):
    """
    卡尔曼滤波\n
    :param value_list: 测量数据
    :param Q: 对模型的信任程度
    :param R: 对测量的信任程度
    :return: 滤波后的数据
    """
    n_iter = len(value_list)

    sz = (n_iter,)  # size of array

    # allocate space for arrays
    xhat = numpy.zeros(sz)  # a posteri estimate of x
    P = numpy.zeros(sz)  # a posteri error estimate
    xhatminus = numpy.zeros(sz)  # a priori estimate of x
    Pminus = numpy.zeros(sz)  # a priori error estimate
    K = numpy.zeros(sz)  # gain or blending factor

    # intial guesses
    xhat[0] = value_list[0]
    P[0] = 1.0

    for k in range(1, n_iter):
        # time update
        xhatminus[k] = xhat[k - 1]  # X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
        Pminus[k] = P[k - 1] + Q  # P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1

        # measurement update
        K[k] = Pminus[k] / (Pminus[k] + R)  # Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
        xhat[k] = xhatminus[k] + K[k] * (
            value_list[k] - xhatminus[k])  # X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
        P[k] = (1 - K[k]) * Pminus[k]  # P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1
    return xhat


def low_pass_filter(value_list, weight=0.1):
    """
    低通滤波\n
    :param value_list: 测量数据
    :param weight: 权值
    :return: 滤波后的数据
    """
    result = numpy.zeros(len(value_list))

    last = value_list[0]
    for i in range(len(value_list)):
        result[i] = last * (1.0 - weight) + value_list[i] * weight
        last = result[i]

    return result.tolist()
