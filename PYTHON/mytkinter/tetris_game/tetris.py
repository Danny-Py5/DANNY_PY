import tkinter as tk
from random import choice


class Setting:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tetris Game')
        self.root.config(bg='grey')

        self.WIDTH = 500
        self.HEIGHT = 720
        self.CANVAS_WIDTH = 320
        self.CANVAS_HEIGHT = self.HEIGHT
        self.CANVAS_BG = 'lightblue'
        self.COLOR = ['red', 'green', 'blue', 'pink', 'orange']
        self.BLOCK_OUTLINE = '#000'
        self.TETROMINO_SPEED = 500
        self.create_geometry()

    def create_geometry(self):
        self.X = (self.root.winfo_screenwidth() - self.WIDTH) // 2
        self.Y = (self.root.winfo_screenheight() - self.HEIGHT) // 2
        self.root.geometry('{}x{}+{}+{}'.format(self.WIDTH, self.HEIGHT, self.X, self.Y))


class Teromino:
    
    def get_shape(self):
        shapes = [
            [[1, 1, 1, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]]
            ]
        return shapes
         
class Tetris(Setting):

    teromino = Teromino()
    
    def __init__(self):
        super().__init__()

        self.row = 0
        self.column = 2
        self.row = 3

        self.canvas = self.create_canvas()

        self.draw_line()
        self.create_box()
        self.move_teromino()
        

    def draw_line(self):
        for x in range(0, self.HEIGHT, 40):
            self.canvas.create_line(0, x, self.WIDTH, x, fill='red')
        for y in range(0, self.HEIGHT, 40):
            self.canvas.create_line(y, 0, y, self.HEIGHT, fill='red')
           

    def create_box(self):
        teromino = Tetris.teromino.get_shape()
        shape = choice(teromino)
        color = choice(self.COLOR)
        self.blocks = [self.canvas.create_rectangle(
            (self.column + j) * 40, (self.row + i) * 40,
            (self.column + j + 1) *40, (self.row + i + 1) * 40,
            fill=color, outline=self.BLOCK_OUTLINE)\
            for i, row in enumerate(shape) for j, cell in enumerate(row) if cell]

    def move_down(self):
        self.row += 1
        self.update_position()

    def update_position(self):
        for block in self.blocks:
            self.canvas.move(block, 0, 40)

    def move_teromino(self):
        self.move_down()
        self.canvas.after(self.TETROMINO_SPEED, self.move_teromino)
        
        
    def create_canvas(self):
        canvas = tk.Canvas(self.root, bg=self.CANVAS_BG, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        canvas.pack(side=tk.LEFT)
        return canvas
    
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    t = Tetris()
    t.run()
    
