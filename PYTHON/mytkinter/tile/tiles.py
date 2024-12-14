'''
Tile module.
'''


__author__ = "DannyPy"
__date__ = "15th March, 2023"
__status__ = "Productive"

__version__ = "1.1.0"


import tkinter as tk
import random
from tkinter import colorchooser as cc
import threading
import sys 


# increase the recoursion limit
sys.setrecursionlimit(5000)


# print(cc.askcolor())

WIDTH = 650
HEIGHT = 800
TITLE = 'Tile\nChallenge'
TITLE_COLOR = 'LIGHTPINK'
CANVAS_BG = '#444'
BACKGROUND_COLOR = '#002f91'
TILE_OUTLINE_COLOR = '#f57c8e'
TILE_COLOR = 'GREEN'
CANVAS_OUTLINE= 'black'
CLICKED_TILE_COLOR = 'LIGHTPINK'
COLUMN_LINE_COLOR = TILE_OUTLINE_COLOR
COLUMN_WIDTH = 100
TILE_SPEED = 20



class Tile:
    """class TIles
    class attributes:
    ----------------
       - tile_height(list): list of tile heights of the tile
       - tile_col(list): the column on the canvas which the tile is placed
       - score(int)->0: the score
       - clicked_tile(None): the tile that has been clicked.
       - game_over(bool)->False: used to check if the game is over.
       - tile_ids(list): created tiles"""

    tile_height = [150, 200, 250, 250, 250, 200, 200, 250, 200, 250]
    tile_col = [1, 2, 3, 4]
    score = 0
    clicked_tile = None
    is_game_over = False
    tile_ids = []
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg=BACKGROUND_COLOR)

        x = (self.root.winfo_screenwidth()-WIDTH) // 2
        y = (self.root.winfo_screenheight()-HEIGHT - 80) // 2 
        
        self.root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))
        self.root.title(TITLE)
        self.create_menu()
        self.canvas = self.create_canvas()
        self.display_title()
        self.score_label = self.create_score_label()
        self.drawline()

        self.play_tile()

        
        
    def play_tile(self):
        # named: created_tile or tile_id
        while True:
            tile_id = self.draw_tile()
            Tile.tile_ids.append(tile_id)
            self.root.after(900)

    def restart(self):
        '''restart the game'''

        self.root.destroy()
        tile = Tile()
        tile.score_label.config(text='Score: 0')
        self.play_tile()
        tile.run()
        
    def update_score(self, tile):
        # return if tile already cliced not to increase score again.
        if tile == Tile.clicked_tile:
            return
        Tile.clicked_tile = tile
        Tile.score += 5
        self.score_label.config(text='Score: ' + str(Tile.score))
        
    def change_color(self, event, tile):
        '''change the color of the clicked tile'''
        self.canvas.itemconfig(tile, fill=CLICKED_TILE_COLOR)
        # update score
        self.update_score(tile)

    def check_land(self, tile):
        '''delete all tile on canvas if any tile landed without been clicked.'''
        try:
            x1, y1, x2, y2 = self.canvas.coords(tile)
            if y2 > self.canvas.winfo_height() + 40:
                if self.canvas.itemcget(tile, 'fill') == TILE_COLOR:
                    for tile_id in Tile.tile_ids:
                        self.canvas.delete(tile_id)
                        Tile.tile_height.clear()
                        game_over = self.write_on_canvas(text='Game Over', font='Arial 30 bold', x=200, y=0,  fill='lightpink')
                        self.move(game_over, x=0, y=2, sec=10)
                        self.canvas.after(6000, self.canvas.destroy)                    
        except ValueError: return 
        except tk._tkinter.TclError: return 
        

    def draw_tile(self):
        '''Draw tile on canvas'''
        try:col = random.choice(Tile.tile_col)
        except IndexError: return
        Tile.tile_col.remove(col)
        x1 = (col * COLUMN_WIDTH) - COLUMN_WIDTH
        y1 = 0
        x2 = x1 + COLUMN_WIDTH
        try: y2 = -(random.choice(Tile.tile_height)) # has been cleared in self.check_land()
        except IndexError: return
        # tile_row.remove(col) if Tile.tile_col in Tile.tile_col else None
        created_tile = self.create_tile(x1, y1, x2, y2)
        self.move(created_tile, x=0, y=10, sec=TILE_SPEED)
        if len(Tile.tile_col) == 0: 
            Tile.tile_col.extend([1, 2, 3, 4])
        return created_tile
        
 
    def call_two_tiles(self):
        tile1 = self.create_tile(0, 0, COLUMN_WIDTH, 200)
        self.move(tile1, x=0, y=10, sec=TILE_SPEED)
        tile2 = self.create_tile(COLUMN_WIDTH*2, -200, COLUMN_WIDTH, 0)
        self.move(tile2, x=0, y=10, sec=TILE_SPEED)
        return tile1, tile2
        
    def drawline(self): 
        for x in range(COLUMN_WIDTH, WIDTH, COLUMN_WIDTH):
            self.canvas.create_line(x, 0, x, HEIGHT, fill=COLUMN_LINE_COLOR, width=4)

    def move(self, tile, x, y, sec):
        """move object on canvas.
        param:
           tile: tile to be moved.
           x(int): move in x-coordinate
           y(int): move in y-coodinate
           sec(int): secs wait before the next tile moves"""
        try:self.canvas.move(tile, x, y)
        except tk._tkinter.TclError: return 
        # check if a tile has landed and not filled
        self.check_land(tile)
        # call recursively
        self.canvas.after(sec, lambda: self.move(tile, x, y, sec))
        
    def create_tile(self, x1, y1, x2, y2,):
        '''draw tile in x1, y1, x2, y2'''
        try:
            tile = self.canvas.create_rectangle(x1, y1, x2, y2, fill=TILE_COLOR, outline=TILE_OUTLINE_COLOR)
            self.canvas.tag_bind(tile, '<Button-1>', lambda event:self.change_color(event, tile))
            return tile
        except tk._tkinter.TclError: return 
    
    def write_on_canvas(self, text='', x=0, y=0, fill='#666', font='Arial 10'):
        '''write on canvas.
        param: text='', x=0, y=0, fill='#666', font='Arial 10'''
        text = self.canvas.create_text(x, y, text=text, fill=fill, font=font)
        return text

    def display_title(self):
        '''display Tile Mystry and score
        return(int): score label'''
        
        label = tk.Label(self.root, text=TITLE, font='Arial 25 bold', bg=BACKGROUND_COLOR
                         ,fg=TITLE_COLOR)
        label.pack(pady=50)

    def create_score_label(self):
        score = tk.Label(self.root, text='Score: {}'.format(Tile.score), font='Arial 14 bold', bg=BACKGROUND_COLOR,
                         fg='#fff', pady=50)
        score.pack(pady=50)
        return score

    def create_menu(self): 
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="Option", menu=file_menu)
        file_menu.add_command(label="Restart", command=self.restart)
        file_menu.add_command(label='Exit',command=self.root.destroy)
        self.root.config(menu=menu_bar)
        
    def create_canvas(self):
        canvas = tk.Canvas(self.root, highlightbackground=CANVAS_OUTLINE, bg=CANVAS_BG, width=400, height=HEIGHT)
        canvas.pack(side=tk.LEFT)
        return canvas
        
    def run(self):
        self.root.mainloop()
    

if __name__ == '__main__':
    def main():
        tile = Tile()
        game = tile.run()
    main()
        
        
        
    
