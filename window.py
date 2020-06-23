from tkinter import *
from cube import Cube


class Window(Frame):
    length = 50

    colors = {
        'W': "#FFF",
        'R': "#F00",
        'B': "#00F",
        'Y': "#FF0",
        'O': "#FA0",
        'G': "#0F0"
    }

    def __init__(self):
        super().__init__()

        self.initUI()

    def paintSquare(self, canvas, y, x, color):

        canvas.create_rectangle(y, x, y + self.length, x + self.length, outline="#000", fill=color)

    def paintSide(self, canvas, side, y, x):

        for j in range(len(side)):
            for i in range(len(side[0])):
                self.paintSquare(canvas, y + j * self.length, x + i * self.length, self.colors[side[i][j]])

    def paintCube(self, canvas, cube, y, x):

        self.paintSide(canvas, cube.FRONT, y, x)
        self.paintSide(canvas, cube.LEFT, y - 3 * self.length, x)
        self.paintSide(canvas, cube.RIGHT, y + 3 * self.length, x)
        self.paintSide(canvas, cube.BACK, y + 6 * self.length, x)
        self.paintSide(canvas, cube.UP, y, x - 3 * self.length)
        self.paintSide(canvas, cube.DOWN, y, x + 3 * self.length)

    def initUI(self):

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        c = Cube()
        canvas = Canvas(self)
        x, y = 200, 200
        self.paintCube(canvas, c, y, x)
        font = 'Helvetica 18 bold'
        canvas.create_text(y + 3 * self.length / 2, y + 3 * self.length / 2, text='F', font=font)
        canvas.create_text(y + 3 * self.length / 2 + 3 * self.length, y + 3 * self.length / 2, text='R', font=font)
        canvas.create_text(y + 3 * self.length / 2 + 6 * self.length, y + 3 * self.length / 2, text='B', font=font)
        canvas.create_text(y + 3 * self.length / 2 - 3 * self.length, y + 3 * self.length / 2, text='L', font=font)
        canvas.create_text(y + 3 * self.length / 2, y + 3 * self.length / 2 + 3 * self.length, text='D', font=font)
        canvas.create_text(y + 3 * self.length / 2, y + 3 * self.length / 2 - 3 * self.length, text='U', font=font)

        canvas.pack(fill=BOTH, expand=1)
