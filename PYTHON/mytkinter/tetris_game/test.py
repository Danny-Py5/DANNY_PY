import tkinter as tk



def draw_on_canvas(canvas):
    re = canvas.create_rectangle(10, 20, 60, 70, fill='green', outline='white')
    return re

def move_box(block=1, direction=''):
    canvas.move(block, 0, 50)

def move():
    canvas.after(500, move_box)
    
def center_window(root, width, height):
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2

    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    


root = tk.Tk()


width = 400
height = 600
    
canvas = tk.Canvas(root, width=width-100, height=height, bg='#555')
canvas.pack(side=tk.LEFT)
center_window(root, width, height)

block = draw_on_canvas(canvas)

move() 
root.bind('<Down>', lambda event: move_box(block, 'down'))


tk.mainloop()
