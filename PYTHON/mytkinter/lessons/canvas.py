import tkinter as tk
from tkinter import colorchooser as cc

WIDTH = 400
HEIGHT = 400


'''
how 50, 50, 100, 50 is drawn
    x1  y1   x2  y2

                 
             y1      y2
             |       |
             |       |
           50|       |50
             |       |
    x1-------|-------|x2
     --><---  
       50           
     -------><--------
           100
'''

class CanvasPractice:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg='#999')
        self.root.geometry('{}x{}+850+10'.format(WIDTH, HEIGHT))

        self.canvas = self.create_canvas()
        self.drawline()
        self.text = self.write_on_canvas(x=150, y=20, font='Arial 15 bold', fill='lightgreen', text='Hello world')
        self.move(self.text, x=0, y=5, sec=400)
        self.box = self.create_box()
        self.move(self.box, x=0, y= 10, sec=350)
        
        
    def drawline(self):
        # self.canvas.create_line(40, 0, 40, 300) 
        for x in range(100, WIDTH, 100):
            self.canvas.create_line(x, 0, x, WIDTH)
        else:
            for y in range(100, HEIGHT, 100):
                self.canvas.create_line(0, y, HEIGHT, y)

    def move(self, obj, x, y, sec):
        """move object on canvas.
        param:
           obj: object to be moved.
           x(int): move in x-coordinate
           y(int): move in y-coodinate
           sec(int): secs wait before the next move"""
        self.canvas.move(obj, x, y)
        # call 
        self.canvas.after(sec, lambda: self.move(obj, x, y, sec))
        
    def create_box(self):
        box = self.canvas.create_rectangle(50, 50, 100, 100, fill='lightgreen')
        print(box)
        return box
    
    def write_on_canvas(self, text='', x=0, y=0, fill='#666', font='Arial 10'):
        '''write on canvas.
        param: text='', x=0, y=0, fill='#666', font='Arial 10'''
        text = self.canvas.create_text(x, y, text=text, fill=fill, font=font)
        return text
    
    def create_canvas(self):
        canvas = tk.Canvas(self.root, bg='#777', width=300, height=300)
        canvas.pack(expand=True)
        return canvas
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    canvaspractice = CanvasPractice()
    canvaspractice.run()
