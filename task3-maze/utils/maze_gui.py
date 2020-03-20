from PyQt5.QtCore import Qt, QSize, QPoint, QTimer
from PyQt5.QtGui import QPainter, QPen, QResizeEvent
from PyQt5.QtWidgets import QWidget
from . import CellType, generate_maze, random_maze_size


class MazeGui(QWidget):
    def __init__(self, a, b):
        super(MazeGui, self).__init__()
        self.timer = QTimer(self)
        self.size = random_maze_size(a, b)
        self.MAZE, self.ENTRANCE, self.EXIT = generate_maze(self.size, self.size)
        self.paintStep = 0
        self.paintOffset = 0
        self.initUI()
        self.show()

    # 重写父类QWidgets方法paintEvent 否则不能使用样式表定义外观
    def paintEvent(self, paintEvent):
        self.pen, self.painter = self.draw_set(color=Qt.darkBlue)
        visited = list()

        def paint(coordinate):
            x, y = coordinate
            if self.__is_path__(coordinate):
                if coordinate in visited:
                    return

                visited.append(coordinate)
                neighbor_coordinates = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
                for nc in neighbor_coordinates:
                    if self.__is_path__(nc) and nc not in visited:
                        self.drawLine(coordinate, nc, color=Qt.darkBlue)
                        paint(nc)

        paint(self.ENTRANCE)
        self.draw_point(self.ENTRANCE, self.pen, self.painter, _color=Qt.blue)
        self.draw_point(self.EXIT, self.pen, self.painter, _color=Qt.red)

    def initUI(self):
        self.setWindowTitle(self.tr("Maze"))

    def draw_set(self, color=Qt.blue):
        """ PyQt绘画基本套装

        """
        pen = QPen()
        pen.setJoinStyle(Qt.RoundJoin)
        pen.setCapStyle(Qt.RoundCap)
        painter = QPainter(self)
        painter.translate(self.paintOffset)
        painter.setBackgroundMode(Qt.TransparentMode)
        painter.setRenderHint(QPainter.Antialiasing)
        pen.setWidth(0.5 * self.paintStep)
        pen.setColor(color)
        painter.setPen(pen)
        return pen, painter

    def __is_path__(self, coordinate: list):
        x, y = coordinate
        return (0 <= x < self.size and
                0 <= y < self.size and
                self.MAZE[x][y] == CellType.ROAD)

    def drawLine(self, coor1, coor2, color=Qt.yellow, width_scale=0.5):
        """ 在两个坐标点之间画线，我们提供了更高层的api，坐标点直接输入方格坐标就可绘制，
        不用担心过多绘图细节。
        """
        pen = self.pen
        painter = self.painter
        pen.setWidth(self.paintStep * width_scale)
        pen.setColor(color)
        painter.setPen(pen)
        x, y = coor1
        xq, yq = coor2
        painter.drawLine(y * self.paintStep, x * self.paintStep,
                         yq * self.paintStep, xq * self.paintStep)

    def draw_point(self, coor: list, pen, painter, _color=Qt.green, width_scale=1):
        """ 画点
        """
        x, y = coor
        pen.setColor(_color)
        pen.setWidth(self.paintStep * width_scale)
        painter.setPen(pen)
        painter.drawPoint(y * self.paintStep, x * self.paintStep)

    def resizeEvent(self, resizeEvent: QResizeEvent):
        self.paintStep = min(self.width() / self.size, self.height() / self.size)

        self.paintOffset = QPoint((self.paintStep + (self.width() - self.paintStep * self.size)) / 2,
                                  (self.paintStep + (self.height() - self.paintStep * self.size)) / 2)

    def sizeHint(self) -> QSize:
        paintStepHint = 200
        return QSize(self.size * paintStepHint, self.size * paintStepHint)
