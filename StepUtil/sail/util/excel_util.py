import numpy
import xlrd
import os


class ExcelUtil:

    def __init__(self, path):
        data = xlrd.open_workbook(path)
        self.table = data.sheet_by_index(0)
        self.real_step = 100
        self.path = path

    def get_triaxial(self):
        len_row = self.table.nrows

        x = numpy.zeros(len_row - 1)
        y = numpy.zeros(len_row - 1)
        z = numpy.zeros(len_row - 1)

        for i in range(1, self.table.nrows):
            x[i - 1] = float(self.table.row_values(i)[1])
            y[i - 1] = float(self.table.row_values(i)[2])
            z[i - 1] = float(self.table.row_values(i)[3])
        return x, y, z

    def print_info(self):
        print(os.path.basename(self.path))
