from utils.maze_gui import MazeGui
from PyQt5.QtCore import Qt
import time

ifWeAchieve = 0


class DfsQMaze(MazeGui):
    def __init__(self, a=5, b=20):
        super(DfsQMaze, self).__init__(a, b)  # 父类初始化
        # print("start:{},end:{}".format(self.ENTRANCE, self.EXIT))
        # print(self.MAZE)

    def paintEvent(self, paintEvent):
        """
        【注】QWidigets类的方法，所有画图的操作放在这里。实例化时，会自动调用这个方法。
        """
        super(DfsQMaze, self).paintEvent(paintEvent)  # 父类绘画界面初始化
        self.paintDfs()

    def paintDfs(self):
        stackAll = []  # 用于保存走过的路  没走过0 走过1
        ppp = 0
        """将递归的过程画出来，必须通过`paintEvent()`方法调用
        【注】如果在`dfs()`中使用了相关画图、画线等函数，即可在窗口中绘制出来
        """
        # stackAll 记录该点是否走过
        for i in range(len(self.MAZE)):
            stackAll.append([])
            for j in range(len(self.MAZE)):
                stackAll[i].append(0)
        stackAll[1][0] = 1
        self.dfs(1, 0)  # 起始点坐标
        print(ppp, "finish")
        ppp = ppp + 1

        self.draw_point(self.ENTRANCE, self.pen, self.painter, _color=Qt.blue)
        self.draw_point(self.EXIT, self.pen, self.painter, _color=Qt.red)
        del self.pen, self.painter

        '''
        ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        助教，这儿不知道为什么本函数进行了多次？会发生覆盖，所以我停止进程让图像显示一会儿
        '''

    def ifItIsRight(self, x, y):
        global stackAll
        if (x < 0 or x > len(self.MAZE) - 1 or y < 0 or y > len(self.MAZE) - 1):
            print("oho,we can't go to:", x, y)
            return 0
        else:
            if (self.MAZE[x][y] == 1):
                print("here is a wall")
                return 0

            if (stackAll[x][y] == 0):
                print("yep,we can go to:", x, y)
                return 1
            else:
                print("i had go here", x, y)
                return 0

    def dfs(self, x, y):
        global ifWeAchieve, stackAll
        if (ifWeAchieve == 0):
            print("from ", x, y)
        if (x == len(self.MAZE) - 2 and y == len(self.MAZE) - 1):
            print("aaaaa ,we achieve the finishing point,not easy..!!god job!!")
            ifWeAchieve = 1
            return

        if (ifWeAchieve == 0 and self.ifItIsRight(x + 1, y)):  # 下
            self.drawLine([x, y], [x + 1, y], color=Qt.green)
            stackAll[x + 1][y] = 1
            self.dfs(x + 1, y)
            if (ifWeAchieve == 0):
                print("draw the way wrong..")
                self.drawLine([x, y], [x + 1, y], color=Qt.yellow)
            else:
                stackAll[x + 1][y] = 2
        if (ifWeAchieve == 0 and self.ifItIsRight(x - 1, y)):  # 上
            self.drawLine([x, y], [x - 1, y], color=Qt.green)
            stackAll[x - 1][y] = 1
            self.dfs(x - 1, y)
            if (ifWeAchieve == 0):
                print("draw the way wrong..")
                self.drawLine([x, y], [x - 1, y], color=Qt.yellow)
            else:
                stackAll[x - 1][y] = 2
        if (ifWeAchieve == 0 and self.ifItIsRight(x, y + 1)):  # 右
            self.drawLine([x, y], [x, y + 1], color=Qt.green)
            stackAll[x][y + 1] = 1
            self.dfs(x, y + 1)
            if (ifWeAchieve == 0):
                print("draw the way wrong..")
                self.drawLine([x, y], [x, y + 1], color=Qt.yellow)
            else:
                stackAll[x][y + 1] = 2
        if (ifWeAchieve == 0 and self.ifItIsRight(x, y - 1)):  # 左
            self.drawLine([x, y], [x, y - 1], color=Qt.green)
            stackAll[x][y - 1] = 1
            self.dfs(x, y - 1)
            if (ifWeAchieve == 0):
                print("draw the way wrong..")
                self.drawLine([x, y], [x, y - 1], color=Qt.yellow)
            else:
                stackAll[x][y - 1] = 2


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    application = QApplication(sys.argv)
    solver = DfsQMaze()
    sys.exit(application.exec_())
