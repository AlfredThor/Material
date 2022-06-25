#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/5/24 19:29
# @Author : kevin
# @Site :
# @File : 输入对话框.py
# @Software: PyCharm
"""
输入对话框：QInputDialog

QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt

"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import xlrd
import re
import xlwt

class QInputDialogDemo(QWidget):
    def __init__(self):
        self.pathsss = 'C:\\project\\Widgets\\files\\A0.T6PROXX.6012-V11-0000.xls'
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框')
        layout = QFormLayout()

        self.button2 = QPushButton('输入参数一和参数二')
        self.button2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.button2, self.lineEdit2)
        self.resize(800, 600)
        self.setLayout(layout)



    def getText(self):
        text, ok = QInputDialog.getText(self, '文本输入框', '输入参数一和参数二')
        if ok and text:
            value = text.split()

            read_repe_file = xlrd.open_workbook(self.pathsss)
            sheet = read_repe_file.sheets()[0]
            rows = sheet.nrows
            lists = []
            for i in range(2, rows):

                datas = sheet.row_values(i)
                # print(datas)
                result = re.search('{}'.format(value[0]),datas[2])
                if result is not None:
                    res = re.search('{}'.format([1]),datas[2])
                    if res is not None:
                        lists.append(datas[0])
                        lists.append(datas[1])
                        lists.append(datas[2])
            print(lists)
            # self.lineEdit2.setText(text)
            self.lineEdit2.setText(lists[0])

    def write(self):
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('物料详情')

        # 行列值
        sheet.write(1, 0, label='this is test')


if __name__ == '__main__':
    # 测试数据 422K ROHS
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())
