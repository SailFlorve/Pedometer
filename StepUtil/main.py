import functools
import os

import numpy

from sail.util.plot_util import PlotUtil
from sail.util.step_util import StepUtil

# su = StepUtil().from_path("stepdata/diyizu/手上200步3.xls")
# su.set_real(200)
# su.print_info()
# PlotUtil().plot(su.data, su.data_filtered, su.data_nor, su.nor_sigmoid, su.nor_sigmoid_filtered) \
#     .label("data", "data f") \
#     .line_prop('-', '-') \
#     .show()
# real, count, acc = su.count(show_log=True)
# print('真实步数', real, '测试步数', count, '精确率', acc, '\n')
#
# exit(3)

dir = os.listdir('stepdata/diyizu')
acc_all = 0
file_num = 0
for file in dir:
    path = os.path.join('stepdata/diyizu', file)

    if os.path.basename(path).split('.')[-1] != 'xls':
        continue
    # 创建StepUtil对象

    su = StepUtil().from_path(path)

    su.print_info()

    real, count, acc = su.count(show_log=False)
    print('实际步数', real, '测试步数', count, '精确率', acc, '\n')
    acc_all += acc
    file_num += 1
    # 使用绘图工具
    # PlotUtil().plot(su.data, su.data_filtered,su.data_diff,su.diff_filtered) \
    #     .label('data') \
    # .show()
print("总精确率:", acc_all / file_num)
