import tkinter as tk

from login import Login
from setting import Constants


class MyApp(Constants):

    create = Login()
    # this function should be called to delete the window of the login
    # comment it out to see it behavior.
    create.onclick_close_window()
    
    def __init__(self):
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 800
        self.root = tk.Tk()
        self.root.config(bg=self.LIGHT_GREY)
        self.create_geometry()
        
        self.welcome = MyApp.create.create_label(self.root, bg=self.LIGHT_GREY, text='You are Welcome!\nNothing is implemented.')

    def create_canvas(self):
        pass
    
    def create_geometry(self):
        x = (self.root.winfo_screenwidth() - self.WIDTH) // 2
        y = (self.root.winfo_screenheight() - self.HEIGHT) // 2
        self.root.geometry('{}x{}+{}+{}'.format(self.WIDTH, self.HEIGHT, x, y))

    def run(self):
        self.root.mainloop()

        
if __name__ == '__main__':
    m = MyApp()
    m.run()
    
        
