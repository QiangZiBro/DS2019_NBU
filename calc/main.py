import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from src.myCalcUI import Ui_MainWindow


class MyCalcWindow(Ui_MainWindow, QMainWindow):
    # 请按教程实现这个类的方法
    def __init__(self):
        pass

    def connecter(self):

        pass

    def press_equal(self):
        text = self.lineEdit.text()
        if text.startswith("0"):
            text = text[1:]
        try:
            # 注意，请用栈来实现python内带的eval（）函数
            result = eval(text)
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText("Invalid syntax, check your input!")


def main():
    app = QApplication(sys.argv)
    Calc = MyCalcWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
