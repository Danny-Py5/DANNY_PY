"""Calculator"""

import tkinter as tk


class Calculator:
    '''
        class calculator

        Args:
            - root (tk window): main window of calculator
         
        Attributes:
            - entry(Text widget): Text widget to display button value
            - operatorframe(Frame widget): contains (+, -, *, /) buttons
            - buttonframe(Frame widget): contains (1 - 9) buttons
            - ezc->[equal-to, zero, clear](Frame widget): contains (=,0,C) buttons 
            - on_answer(bool)-> False;
                 if False:
                    it allows any button value to be shown on the screen
                 else:
                    helps to allow deletion of integer value on the screen

                 on_answer does it work in answer() and show().
                 ----------------------------------------------

        methods:
            - show(self): shows  button's value on the screen
            - answer(self): get and evaluate screen expression
            - clear(self): clears screen  expression
           
    '''
    
    def __init__(self,root):
        """construtor of the  calculator class"""
        
        root.title("Calculator")
        root.config(bg="black")
        root.geometry("200x290+500+300")
        #root.wm_attributes("-fullscreen",True)
        self.root = root
        self.root.resizable(False,False)
        self.on_answer = False
        
        self.entry = tk.Text(self.root,width=50,height=3, font=("Times New Roman",12),bg="black",fg="lightblue",state=tk.DISABLED)
        self.entry.pack(padx=5,pady=10)

        # operator frame
        self.operatorframe = tk.Frame(self.root,bg= "black")
        self.operatorframe.columnconfigure(0,weight=1)
        self.operatorframe.columnconfigure(1,weight=1)
        self.operatorframe.columnconfigure(2,weight=1)
        self.operatorframe.columnconfigure(3,weight=1)
        # add buttons to the operator frame
        # operators buttons
        self.add =  tk.Button(self.operatorframe,bg="black",fg="white",text = "+",command=lambda: self.show("+"))
        self.add.grid(row=0,column=0,sticky=tk.W+tk.E)

        self.sub =tk.Button(self.operatorframe,bg="black",fg="white",text = "-",command=lambda: self.show("-"))
        self.sub.grid(row=0,column=1,sticky=tk.W+tk.E)

        self.mul =tk.Button(self.operatorframe,bg="black",fg="white",text = "*",command=lambda: self.show("*"))
        self.mul.grid(row=0,column=2,sticky=tk.W+tk.E)

        self.div=tk.Button(self.operatorframe,bg="black",fg="white",text = "/",command=lambda: self.show("/"))
        self.div.grid(row=0,column=3,sticky=tk.W+tk.E)
        # Pack the operatorframe 
        self.operatorframe.pack(padx=5,fill=tk.X)
        
        # buttonfram
        self.buttonframe = tk.Frame(self.root,bg="black")
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        # number Buttons 
        self.btn7 = tk.Button(self.buttonframe,text="7",bg="black",fg="white",command=lambda: self.show(7))
        self.btn7.grid(row=0,column=0,sticky=tk.W+tk.E)

        self.btn8 = tk.Button(self.buttonframe,text="8",bg="black",fg="white",command=lambda: self.show(8))
        self.btn8.grid(row=0,column=1,sticky=tk.W+tk.E)

        self.btn9 = tk.Button(self.buttonframe,text="9",bg="black",fg="white",command=lambda: self.show(9))
        self.btn9.grid(row=0,column=2,sticky=tk.W+tk.E)

        self.btn4 = tk.Button(self.buttonframe,text="4",bg="black",fg="white",command=lambda: self.show(4))
        self.btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

        self.btn5 = tk.Button(self.buttonframe,text="5",bg="black",fg="white",command=lambda: self.show(5))
        self.btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

        self.btn6 = tk.Button(self.buttonframe,text="6",bg="black",fg="white",command=lambda: self.show(6))
        self.btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

        self.btn1 = tk.Button(self.buttonframe,text="1",bg="black",fg="white",command=lambda: self.show(1))
        self.btn1.grid(row=2,column=0,sticky=tk.W+tk.E)
        
        self.btn2 = tk.Button(self.buttonframe,text="2",bg="black",fg="white",command=lambda: self.show(2))
        self.btn2.grid(row=2,column=1,sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.buttonframe,text="3",bg="black",fg="white",command=lambda: self.show(3))
        self.btn3.grid(row=2,column=2,sticky=tk.W+tk.E)
        self.buttonframe.pack(padx=5,fill=tk.X)# stretch to the x axis

        # ezc  frame
        self.ezc = tk.Frame(self.root,bg= "black")
        self.ezc.columnconfigure(0,weight=1)
        self.ezc.columnconfigure(1,weight=1)
        self.ezc.columnconfigure(2,weight=1)
         
        self.clear=tk.Button(self.ezc,text = "C",command = self.clear,bg="red",fg="white")
        self.clear.grid(row=0,column=0,sticky=tk.W+tk.E)

        self.zero=tk.Button(self.ezc,text = "0",command=lambda: self.show(0),bg="black",fg="white")
        self.zero.grid(row=0,column=1,sticky=tk.W+tk.E)

        self.equal=tk.Button(self.ezc,text = "=",command=self.answer,bg="green")
        self.equal.grid(row=0,column=2,sticky=tk.W+tk.E)
        
        self.ezc.pack(padx=5,fill=tk.X)# stretch to  x axis
        
    def show(self,val):
        '''
        shows button value on the  screen
        
        if the '=' button is pressed and result has been shown
        on the screen, the  screen will be cleared if new
        button click is type int
        '''
        # enable entry to input value
        self.entry.config(state=tk.NORMAL)
        if self.on_answer == True and isinstance(val, int):
            self.entry.delete(1.0,tk.END)
        self.on_answer = False
        self.entry.config(fg="lightblue")# change color to normal if red caused by (zerodivision)
        self.entry.insert(tk.END,val)
        # disable entry -> not allow direct keyboard entry
        self.entry.config(state=tk.DISABLED)
        

    def answer(self):
        '''
        gets screen expression, evaluate it, and
        insert result on the entry widget
        '''
        
        self.entry.config(state=tk.NORMAL)
        user = self.entry.get(1.0,tk.END)
        self.entry.delete(1.0,tk.END)
        try:
            ans = eval(str(user))
            # if answer is float: round it to 2dp
            if isinstance(ans,float):
                ans = round(ans,2)
            self.entry.insert(tk.END,ans)
            self.entry.config(state=tk.DISABLED)
            self.on_answer = True
        except ZeroDivisionError:
            self.entry.config(state=tk.NORMAL,fg="red")
            self.entry.insert(tk.END,"Division by zero is not allowed!")
            self.entry.config(state=tk.DISABLED)
            self.on_answer = True
        except:
            self.entry.config(state=tk.NORMAL)
            self.entry.insert(tk.END,"ERROR")
            self.entry.config(state=tk.DISABLED)
            self.on_answer = True
        
    def clear(self):
        '''clears screen expression'''
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0,tk.END)
        self.entry.config(state=tk.DISABLED)
        
def main():
    root = tk.Tk()
    cal = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
