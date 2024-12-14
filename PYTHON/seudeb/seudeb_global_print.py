import tkinter as tk
from tkinter import colorchooser as ch

#print(ch.askcolor())

HEIGHT = 800
WIDTH = 900
ROOT_BG = '#92784e'
CANVAS_OUTLINE = 'red'
CANVAS_BG = 'black'


def create_frame(root, padx=0, pady=0, fill=None, bg='white'):
    frame = tk.Frame(root, bg=bg)
    frame.pack(pady=pady, padx=padx, expand=True, fill= fill if fill else tk.X)
    return frame

def create_canvas(root, height=100, width=300, bg=CANVAS_BG, highlightbackground=CANVAS_OUTLINE, side=None):
    canvas = tk.Canvas(root, highlightbackground=highlightbackground, bg=bg, width=400, height=height)
    canvas.pack()
    return canvas

class SeudebGlobalPrint:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title('Seudeb Global Print')
        self.root.config(bg=ROOT_BG)
        self.set_geometry()

        self.welcome_frame = create_frame(self.root, bg=ROOT_BG)
        self.welcome_label = self.welcome()

    def kill(self, widget, time=1000):
        widget.after(3000, widget.destroy)
        
    def welcome(self):
        label = tk.Label(self.welcome_frame, bg=ROOT_BG,  text='Welcome to Seudeb Global Print', font='Arial 30 bold')
        label.pack()
        return label
    
    def set_geometry(self):
        x = (self.root.winfo_screenwidth() - WIDTH) // 2 
        y = (self.root.winfo_screenheight() - HEIGHT) // 2 - 50
        self.root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    def main():

        sgp = SeudebGlobalPrint()

        sgp.run()

    main()
