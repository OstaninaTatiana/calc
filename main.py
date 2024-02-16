# Лабораторная работа №1
# Гарипова, Останина
# БПМ-22-4

from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QPushButton, QLCDNumber, QRadioButton, QButtonGroup, QLabel, QLineEdit


def converter_2_4_8_10(number, f, t):
    number = int(number)
    res1 = 0
    c = 0
    while number != 0:
        res1 += number % 10 * (f ** c)
        c += 1
        number //= 10

    res = ''
    while res1 != 0:
        res = str(res1 % t) + res
        res1 //= t

    return res


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sys = 10
        self.text = ''
        self.task = ''
        self.resize(450, 500)
        self.setWindowTitle('Калькулятор')

        self.sm = QLabel(self)
        self.sm.setText('Сантиметры:')
        self.sm.setGeometry(312, 100, 300, 40)

        self.sm_text = QLineEdit(self)
        self.sm_text.setGeometry(312, 140, 100, 20)

        self.ft = QLabel(self)
        self.ft.setText('Футов:')
        self.ft.setGeometry(312, 250, 300, 40)

        self.dm = QLabel(self)
        self.dm.setText('Дюймов:')
        self.dm.setGeometry(312, 290, 200, 40)

        self.but1 = QPushButton(self)
        self.but1.setText('Перевести')
        self.but1.setGeometry(312, 180, 100, 60)
        self.but1.clicked.connect(self.convert_sm)

        self.but1 = QPushButton(self)
        self.but1.setText('1')
        self.but1.setGeometry(12, 356, 60, 60)
        self.but1.clicked.connect(self.get_1)

        self.but2 = QPushButton(self)
        self.but2.setText('2')
        self.but2.setGeometry(84, 356, 60, 60)
        self.but2.clicked.connect(self.get_2)

        self.but3 = QPushButton(self)
        self.but3.setText('3')
        self.but3.setGeometry(156, 356, 60, 60)
        self.but3.clicked.connect(self.get_3)

        self.but4 = QPushButton(self)
        self.but4.setText('4')
        self.but4.setGeometry(12, 284, 60, 60)
        self.but4.clicked.connect(self.get_4)

        self.but5 = QPushButton(self)
        self.but5.setText('5')
        self.but5.setGeometry(84, 284, 60, 60)
        self.but5.clicked.connect(self.get_5)

        self.but6 = QPushButton(self)
        self.but6.setText('6')
        self.but6.setGeometry(156, 284, 60, 60)
        self.but6.clicked.connect(self.get_6)

        self.but7 = QPushButton(self)
        self.but7.setText('7')
        self.but7.setGeometry(12, 212, 60, 60)
        self.but7.clicked.connect(self.get_7)

        self.but8 = QPushButton(self)
        self.but8.setText('8')
        self.but8.setGeometry(84, 212, 60, 60)
        self.but8.clicked.connect(self.get_8)

        self.but9 = QPushButton(self)
        self.but9.setText('9')
        self.but9.setGeometry(156, 212, 60, 60)
        self.but9.clicked.connect(self.get_9)

        self.but0 = QPushButton(self)
        self.but0.setText('0')
        self.but0.setGeometry(12, 140, 60, 60)
        self.but0.clicked.connect(self.get_0)

        self.but_plus = QPushButton(self)
        self.but_plus.setText('+')
        self.but_plus.setGeometry(228, 356, 60, 60)
        self.but_plus.clicked.connect(self.get_plus)

        self.but_minus = QPushButton(self)
        self.but_minus.setText('-')
        self.but_minus.setGeometry(228, 284, 60, 60)
        self.but_minus.clicked.connect(self.get_minus)

        self.but_mult = QPushButton(self)
        self.but_mult.setText('*')
        self.but_mult.setGeometry(228, 212, 60, 60)
        self.but_mult.clicked.connect(self.get_mult)

        self.but_split = QPushButton(self)
        self.but_split.setText('/')
        self.but_split.setGeometry(228, 140, 60, 60)
        self.but_split.clicked.connect(self.get_split)

        self.but_res = QPushButton(self)
        self.but_res.setText('=')
        self.but_res.setGeometry(12, 428, 280, 60)
        self.but_res.clicked.connect(self.get_res)

        self.but_dot = QPushButton(self)
        self.but_dot.setText('.')
        self.but_dot.setGeometry(84, 140, 60, 60)
        self.but_dot.clicked.connect(self.get_dot)

        self.but_del = QPushButton(self)
        self.but_del.setText('del')
        self.but_del.setGeometry(156, 140, 60, 60)
        self.but_del.clicked.connect(self.get_del)

        self.lable = QLCDNumber(self)
        self.lable.setDigitCount(15)
        self.lable.display('0')
        self.lable.setGeometry(12, 50, 280, 80)

        self.s2 = QRadioButton(self)
        self.s2.setText('2')
        self.s2.setGeometry(12, 20, 45, 15)

        self.s4 = QRadioButton(self)
        self.s4.setText('4')
        self.s4.setGeometry(84, 20, 45, 15)

        self.s8 = QRadioButton(self)
        self.s8.setText('8')
        self.s8.setGeometry(156, 20, 45, 15)

        self.s10 = QRadioButton(self)
        self.s10.setText('10')
        self.s10.setGeometry(228, 20, 45, 15)
        self.s10.setChecked(True)

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.s2)
        self.button_group.addButton(self.s4)
        self.button_group.addButton(self.s8)
        self.button_group.addButton(self.s10)
        self.button_group.buttonClicked.connect(self.convert)

    def get_number(self, number):
        if len(self.task) == 0:
            self.text += str(number)
            self.task += str(number)
        else:
            if self.task[-1].isdigit():
                self.text += str(number)
                self.task += str(number)
            else:
                self.text = str(number)
                self.task += str(number)
        self.lable.display(self.text)

    def get_1(self):
        self.get_number(1)

    def get_2(self):
        self.get_number(2)

    def get_3(self):
        self.get_number(3)

    def get_4(self):
        self.get_number(4)

    def get_5(self):
        self.get_number(5)

    def get_6(self):
        self.get_number(6)

    def get_7(self):
        self.get_number(7)

    def get_8(self):
        self.get_number(8)

    def get_9(self):
        self.get_number(9)

    def get_0(self):
        self.get_number(0)

    def get_sign(self, sign):
        if len(self.task) == 0:
            self.task += '0' + str(sign)
        else:
            if self.task[-1].isdigit():
                if not self.task.isdigit():
                    self.text = str(eval(self.task))
                    self.task = self.text
                self.task += str(sign)
            else:
                self.task = self.task[:-1] + str(sign)
            self.lable.display(self.text)

    def get_plus(self):
        self.get_sign('+')

    def get_minus(self):
        self.get_sign('-')

    def get_mult(self):
        self.get_sign('*')

    def get_split(self):
        self.get_sign('/')

    def get_res(self):
        self.text = str(eval(self.task))
        self.lable.display(self.text)
        self.task = self.text + '='

    def get_del(self):
        self.text = ''
        self.task = ''
        self.lable.display('0')

    def get_dot(self):
        self.text += '.'
        self.task += '.'
        self.lable.display(self.text)

    def convert(self):
        new_sys = 10
        if self.s2.isChecked():
            new_sys = 2
        if self.s4.isChecked():
            new_sys = 4
        if self.s8.isChecked():
            new_sys = 8
        self.lable.display(converter_2_4_8_10(self.text, self.sys, new_sys))

    def convert_sm(self):
        sm = int(self.sm_text.text())
        ft = sm * 100 // 3048
        sm = sm * 100 % 3048
        dm = sm / 254
        self.ft.setText('Футов:' + str(ft))
        self.dm.setText('Дюймов:' + str(round(dm, 5)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window()
    ex.show()

    sys.exit(app.exec())


