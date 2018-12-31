from sail.algorithm import data_util
from sail.algorithm.filter import *
from sail.util.excel_util import ExcelUtil
from sail.util.json_util import JsonUtil
import os


# 使用:
# su = StepUtil().from_path(...)
# su.xxx()
class StepUtil:
    # JsonUtil/ExcelUtil对象
    ut = None

    x = []
    y = []
    z = []

    # 平方和开平方后的数据，一维数组
    data = []
    data_filtered = []

    # 应用sigmoid函数后的数据
    data_sigmoid = []
    sigmoid_filtered = []

    # 差分后的数据
    data_diff = []
    diff_filtered = []

    data_log = []
    data_nor = []

    nor_filtered = []

    def __init__(self):
        pass

    def __from__(self, s, is_path):
        if os.path.basename(s).split('.')[-1] == 'xls':
            self.ut = ExcelUtil(s)
        else:
            self.ut = JsonUtil(s, is_path)
        self.x, self.y, self.z = self.ut.get_triaxial()
        self.__generate_data__()

    def from_path(self, path):
        """
        从路径读入文件中的Json
        :param path:
        :return:
        """
        self.__from__(path, True)
        return self

    def from_str(self, str):
        """
        直接读入json字符串
        :param str:
        :return:
        """
        self.__from__(str, False)
        return self

    def __generate_data__(self):
        """
        根据x y z数据生成其他数据
        """
        self.data = data_util.sqrt_quadratic_sum(self.x, self.y, self.z)
        self.data_filtered = low_pass_filter(self.data, 0.5)
        # self.data_sigmoid = data_util.sigmoid(self.data)
        # self.data_diff = data_util.diff(self.data_filtered)
        # self.diff_filtered = low_pass_filter(self.data_diff, 0.5)
        # self.sigmoid_filtered = low_pass_filter(self.data_sigmoid, 0.2)
        # self.data_log = numpy.log10(self.data) * 10
        self.data_nor = data_util.normalization(self.data)
        self.nor_filtered = low_pass_filter(self.data_nor, 0.4)
        self.nor_sigmoid = data_util.sigmoid(self.data_nor)
        self.nor_sigmoid_filtered = low_pass_filter(self.nor_filtered, 0.25)

    def print_info(self):
        """
        输出文件名和实际步数。
        """
        self.ut.print_info()

    def real(self):
        """
        输出真实步数
        :return:
        """
        return int(self.ut.real_step)

    def set_real(self, real):
        self.ut.real_step = real

    def count(self, show_log=False):
        """
        开始计算步数
        :param show_log: 是否输出log
        :return:
        """
        result = data_util.zero_cross(self.nor_sigmoid_filtered, self.nor_filtered, 0.5 , show_log)
        return self.real(), result, data_util.accuracy(self.real(), result)
