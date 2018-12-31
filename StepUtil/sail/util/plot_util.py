import pylab as pl


# 使用: PlotUtil().plot(...).label(...).line_prop(...).show()
class PlotUtil:
    plot_data = []
    labels = []
    prop = []

    def __init__(self):
        self.plot_data = []
        self.labels = []
        self.prop = []
        pl.grid(True)

    def plot(self, *data_set):
        """
        :param data_set: 绘图数据集合
        :return:
        """
        for data in data_set:
            self.plot_data.append(data)
        return self

    def label(self, *labels):
        """
        :param labels: 图例集合，对应绘图数据集
        :return:
        """
        self.labels.extend(list(labels))
        return self

    def line_prop(self, *props):
        """
        绘图属性设置。

        线属性
        ‘-‘ 实线
        ‘:’ 虚线
        ‘–‘ 破折线
        ‘-.’ 点划线
        ‘None’ 什么都不画

        点标记
        ‘o’	圆圈
        ‘.’	点
        ‘D’	菱形
        ‘s’	正方形
        ‘h’	六边形1
        ‘*’	星号
        ‘H’	六边形2
        ‘d’	小菱形
        ‘_’	水平线
        ‘v’	一角朝下的三角形
        ‘8’	八边形
        ‘p’	五边形
        ‘>’	一角朝右的三角形
        ‘,’	像素
        ‘^’	一角朝上的三角形
        ‘+’	加号
        ‘x’	X
        ‘None’ 无

        颜色
        b 蓝色
        g 绿色
        r 红色
        y 黄色
        c 青色
        k 黑色
        m 洋红色
        w 白色

        属性任意组合。例如：白色虚线，每个点用星号标记，则为':*b'

        :param props: 属性集合，对应绘图数据
        :return:
        """
        self.prop.extend(props)
        return self

    def show(self):
        for i, val in enumerate(self.plot_data):
            if len(self.labels) - 1 >= i:
                label = self.labels[i]
            else:
                label = 'data ' + str(i)

            if len(self.prop) - 1 >= i:
                pro = self.prop[i]
            else:
                pro = '-'

            pl.plot(val, pro, label=label)
        pl.legend()
        pl.show()
        pl.close('all')