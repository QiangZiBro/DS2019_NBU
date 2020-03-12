import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from statics.friendship_UI import Ui_MainWindow
from util.LinkedList import *
from util.Student import Student
import qtmodern.styles
import qtmodern.windows

from PyQt5 import QtWidgets

op = QtWidgets.QGraphicsOpacityEffect()
op.setOpacity(0.5)


class Friendship(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Friendship, self).__init__()
        self.setupUi(self)
        self.pushButton_clear.setGraphicsEffect(op)
        self.connecter()
        self.show()

    def connecter(self):
        self.pushButton_add_input.clicked.connect(self.press_add)
        self.pushButton_clear.clicked.connect(self.press_clear)
        self.pushButton_close.clicked.connect(self.press_close)
        self.pushButton_delete.clicked.connect(self.press_delete)
        self.pushButton_upload_input.clicked.connect(self.press_upload)
        self.pushButton_search.clicked.connect(self.press_search)

    def press_add(self):
        # 获取表单数据
        stu = Student()
        stu.name = self.lineEdit_name_input.text()
        stu.sno = self.lineEdit_sno_input.text()
        stu.birthday = self.lineEdit_birthday_input.text()
        stu.sex = self.comboBox_sex_input.currentText()
        stu.pic = self.imgName
        # stu.pic = None
        pos = int(self.lineEdit_pos_input.text())

        # 新建学生节点并插入到链表
        node = Node(data=stu)
        if ls.isEmpty():
            if self.lineEdit_pos_input.text() == '0':
                ls.append(node)
                # ls.append(stu)
            else:
                pos = 0
                print('empty list, change input position to 0')
        else:
            ls.insert(pos, node)
            # ls.insert(pos, stu)

        self.lineEdit_num_info.setText(str(ls.length))
        # 将新的学生数据存入文件中

    def press_clear(self):
        ls.clear()
        self.lineEdit_num_info.setText(str(ls.length))

    def press_close(self):
        sys.exit()

    def press_delete(self):
        pos = self.lineEdit_pos_delete.text()
        ls.delete(int(pos))
        self.lineEdit_num_info.setText(str(ls.length))

    def press_upload(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(self.imgName).scaled(self.label_pic_input.width(), self.label_pic_input.height())
        self.label_pic_input.setPixmap(jpg)

    def press_search(self):
        name_search = self.lineEdit_name_search.text()
        item = ls.head
        while item != None and name_search != item.data.name:
            item = item._next

        if item != None:
            name = item.data.name
            sno = item.data.sno
            birthday = item.data.birthday
            sex = item.data.sex
            pic = item.data.pic
            self.lineEdit_name_find.setText(name)
            self.lineEdit_sno_find.setText(sno)
            self.lineEdit_birthday_find.setText(birthday)
            self.lineEdit_sex_find.setText(sex)

            imgName = pic
            jpg = QtGui.QPixmap(pic).scaled(self.label_pic_find.width(), self.label_pic_find.height())
            self.label_pic_find.setPixmap(jpg)

        else:
            print('No student named ', name_search)


def main():
    stu_list = ls
    app = QApplication(sys.argv)
    w = Friendship()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
