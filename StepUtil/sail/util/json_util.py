import json
import os

import numpy


class JsonUtil:
    json_dict = {}
    is_path = False

    # 路径或者Json字符串
    s = None

    # 实际步数
    real_step = 0

    def __init__(self, s, from_path=True):
        self.s = s
        if from_path:
            self.is_path = True
            self.json_dict = json.load(open(s))
        else:
            self.json_dict = json.loads(s)

    def get_triaxial(self):
        """
        初始化实际步数，返回x, y, z数据
        :return: x、y和z
        """
        if self.json_dict is None:
            return

        self.real_step = self.json_dict['stepNumbers']
        data_obj = json.loads(self.json_dict['data'])
        ori = []
        for i in range(len(data_obj)):
            arr = json.loads(data_obj[i])
            ori.append(arr)

        # Json中的原始数据
        data_array = numpy.array(ori)

        return [val.ravel() for i, val in enumerate(numpy.hsplit(data_array, 3))]

    def print_info(self):
        if self.is_path:
            print(os.path.basename(self.s))
        else:
            print('Read from string')

        print('实际步数:', self.real_step)
