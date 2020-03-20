from utils.maze_gui import MazeGui
from PyQt5.QtCore import Qt


class DfsQMaze(MazeGui):
    def __init__(self, a=5, b=20):
        super(DfsQMaze, self).__init__(a, b) # 父类初始化
        # print("start:{},end:{}".format(self.ENTRANCE, self.EXIT))
        # print(self.MAZE)

    def paintEvent(self, paintEvent):
        """
        【注】QWidigets类的方法，所有画图的操作放在这里。实例化时，会自动调用这个方法。
        """
        super(DfsQMaze, self).paintEvent(paintEvent) #父类绘画界面初始化
        self.paintDfs()

    def paintDfs(self):
        """将递归的过程画出来，必须通过`paintEvent()`方法调用
        【注】如果在`dfs()`中使用了相关画图、画线等函数，即可在窗口中绘制出来
        """
        self.dfs()
        self.draw_point(self.ENTRANCE, self.pen, self.painter, _color=Qt.blue)
        self.draw_point(self.EXIT, self.pen, self.painter, _color=Qt.red)
        del self.pen, self.painter

    def dfs(self):
        """在此写下代码
        """
        pass


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    application = QApplication(sys.argv)
    solver = DfsQMaze()
    sys.exit(application.exec_())
