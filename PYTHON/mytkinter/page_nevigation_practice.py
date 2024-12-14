

import tkinter as tk

WIDTH = 500
HEIGHT = 500
    
class Page:

    def home_page(self):
        self.home_frame = tk.Frame(self.main_frame)

        label = tk.Label(self.home_frame,text="\nHome Page\n\nPage 1",
                         font=("Times New Roman",14,"bold"),bg='azure',fg="red")
        label.pack()
        
        self.home_frame.pack()

    def menu_page(self):
        self.menu_frame = tk.Frame(self.main_frame)

        label = tk.Label(self.menu_frame,text="\nMenu Page\n\nPage 2",
                         font=("Times New Roman",14,"bold"),bg='azure',fg="red")
        label.pack()
        
        self.menu_frame.pack()

    def content_page(self):
        self.content_frame = tk.Frame(self.main_frame)

        label = tk.Label(self.content_frame,text="\nContent Page\n\nPage 3",
                         font=("Times New Roman",14,"bold"),bg='azure',fg="red")
        label.pack()
        
        self.content_frame.pack()

    def about_page(self):
        self.about_frame = tk.Frame(self.main_frame)

        label = tk.Label(self.about_frame,text="\nAbout Page\n\nPage 4",
                         font=("Times New Roman",14,"bold"),bg='azure',fg="red")
        label.pack()
        
        self.about_frame.pack()

    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def hide_indicator(self):
        self.home_btn_indicator.config(bg="grey")
        self.menu_btn_indicator.config(bg="grey")
        self.content_btn_indicator.config(bg="grey")
        self.about_btn_indicator.config(bg="grey")
        
    def show_indicator(self,botton,page):
        self.hide_indicator()
        botton.config(bg="blue")
        self.delete_page()
        page()
    
    def __init__(self,root):
        
        self.root = root
        root.title("Page Nevigating Practice")
        self.root.geometry("{}x{}+{}+{}".format(WIDTH,HEIGHT,int(root.winfo_screenwidth()/2+100),int(root.winfo_screenheight()/2 -500)))
        self.root.resizable(False,False)

        # Option frame
        self.option_frame = tk.Frame(self.root,bg="grey",highlightbackground="blue",
                                     highlightthickness=3)

        # Option buttons
        self.home_btn= tk.Button(self.option_frame, fg="blue", bg="grey",bd=0,text="Home",
                                 font=("Comic Sans MS", 14, "bold"),cursor="hand2",
                                 command=lambda:self.show_indicator(self.home_btn_indicator,self.home_page))
        self.home_btn.place(x=10,y=100)
        
        self.home_btn_indicator = tk.Label(self.option_frame,text="",height=2,bg="grey")
        self.home_btn_indicator.place(x=3,y=100)

        

        self.menu_btn= tk.Button(self.option_frame,fg="blue",bg="grey",bd=0,text="Menu",
                                 font=("Comic Sans MS",14,"bold"),cursor="hand2",
                                 command=lambda:self.show_indicator(self.menu_btn_indicator,self.menu_page))
        self.menu_btn.place(x=10,y=160)

        self.menu_btn_indicator = tk.Label(self.option_frame,text="",height=2,bg="grey")
        self.menu_btn_indicator.place(x=3,y=160)



        self.content_btn= tk.Button(self.option_frame,fg="blue",bg="grey",bd=0,text="Content",
                                 font=("Comic Sans MS",14,"bold"),cursor="hand2",
                                 command=lambda:self.show_indicator(self.content_btn_indicator,self.content_page))
        self.content_btn.place(x=10,y=210)
        
        self.content_btn_indicator = tk.Label(self.option_frame,text="",height=2,bg="grey")
        self.content_btn_indicator.place(x=3,y=210)



        self.about_btn= tk.Button(self.option_frame,fg="blue",bg="grey",bd=0,text="About",
                                 font=("Comic Sans MS",14,"bold"),cursor="hand2",
                                 command=lambda:self.show_indicator(self.about_btn_indicator,self.about_page))
        self.about_btn.place(x=10,y=260)
        
        self.about_btn_indicator = tk.Label(self.option_frame,text="",height=2,bg="grey")
        self.about_btn_indicator.place(x=3,y=260)



        # allow option_frame to be congigured
        self.option_frame.pack_propagate(False)
        self.option_frame.config(width=120,height=HEIGHT)
        self.option_frame.pack(side=tk.LEFT)

        #main page frame
        self.main_frame= tk.Frame(self.root,bg="azure",highlightbackground="black",
                                  highlightthickness=3)


        # allow main_frame to be  configured(edited)
        self.main_frame.pack_propagate(False)
        self.main_frame.config(width=400,height=HEIGHT)
        self.main_frame.pack(side=tk.LEFT)

   
def main():
    root = tk.Tk()
    
    p = Page(root)

    root.mainloop()


if __name__ == "__main__":
    main()



