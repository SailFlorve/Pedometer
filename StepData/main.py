import pylab
import os

import json_parser
from data_processor import *


def do(path):
    triaxial, real_count = json_parser.get_data(path)
    xyz_data = sqrt_quadratic_sum(triaxial)

    sigmoid = get_sigmoid(xyz_data, 10)
    sigmoid_filtered = filter.low_pass_filter(sigmoid, 0.5)
    sigmoid_diff = get_diff(sigmoid_filtered)
    sigmoid_diff_filtered = filter.low_pass_filter(sigmoid_diff, 0.25)

    # 对三轴取模数据处理类
    processor = DataSeriesProcessor(copy.copy(xyz_data))

    data_filtered = processor.low_pass_filter(0.1).get_current()

    diff = processor.diff().get_current()

    diff_filtered = processor.low_pass_filter(0.2).get_current()

    count = count_step(sigmoid_filtered, data_filtered, 0.5)

    print(path.split("\\")[-1])
    print("Real:", real_count, "Count:", count)
    rate = 1 - abs(real_count - count) / real_count
    print("正确率", rate)
    print()

    pylab.plot(xyz_data, label='origin')
    # pylab.plot(data_filtered)
    pylab.plot(sigmoid, label='sigmoid')
    pylab.plot(sigmoid_filtered, label='sigmoid filtered')
    pylab.plot(sigmoid_diff_filtered)

    pylab.grid(True)
    pylab.legend()
    # pylab.show()
    return rate


# do('E:\Documents\资料\stepdata\zwh 100.txt')
# exit(0)

root_path = 'E:\Documents\资料\stepdata\old'
data_dir = os.listdir(root_path)
count = 0
all_rate = 0
for filename in data_dir:
    if filename.split(".")[-1] != 'txt':
        continue
    count += 1
    path = os.path.join(root_path, filename)
    all_rate += do(path)
print("平均正确率:", all_rate / count)
