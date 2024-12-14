"""
Author: DannyPy
Date: 7th Jan., 2024
Email: olatundedaniel943@gmail.com
"""

__status__ = "Progressing"
__author__ = "DannyPy"
__status__ = "Planning"

import tkinter as tk

WIDTH = 400
HEIGHT = 700
SMALL_DISPLAY_FONT = ("Arial 20")
LARGE_DISPLAY_FONT = ("Arial 30 bold")
DISPLAY_FRAME_COLOR = "#e1e1e1"
EXPRESSION_COLOR = "#333"
BUTTON_FRAME_COLOR = "#ececec"
BUTTONS_COLOR = "#333"
BUTTONS_FONT = ("Arial 24 bold")
EQUALS_BUTTON_COLOR = "#B2ECF1"
NONE_DIGIT_BUTTONS_COLOR = "#ECECEC"

class Calculator:
    '''Class Calculator'''
    
    def __init__(self):

        self.root = tk.Tk()
        
        self.sw = int((self.root.winfo_screenwidth() - WIDTH) / 2)
        self.sh =  int((self.root.winfo_screenheight() - HEIGHT) /2)
        
        self.root.title("Calculator")
        self.root.geometry("{}x{}+{}+{}".format(WIDTH,HEIGHT,self.sw,self.sh))
        self.root.resizable(False,False)

        
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label,self.label = self.create_display_labels()

        self.buttons = {
            7:(1,0),8:(1,1),9:(1,2),
            4:(2,0),5:(2,1),6:(2,2),
            1:(3,0),2:(3,1),3:(3,2),
            ".":(4,0),0:(4,1)
            }
        self.operators = {"/":"\u00F7" ,"*":"\u00D7","-":"-","+":"+"}
            
        self.buttons_frame = self.create_buttons_frame()
        
        for x in range(4):
            self.buttons_frame.columnconfigure(x,weight=1)
            self.buttons_frame.rowconfigure(x,weight=0)
            
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def square(self):
        if self.current_expression == '':
            return 
        try:
            self.current_expression = str(eval(self.current_expression)**2)
            self.update_label()
        except SyntaxError:
            self.current_expression = "Error"
            self.total_expression = ""
            self.update_label()
            self.update_total_label()
        except:pass
        
    def create_square_button(self):
        button = tk.Button(self.buttons_frame,command=self.square,text="x\u00b2",bg=NONE_DIGIT_BUTTONS_COLOR, fg=BUTTONS_COLOR,font=BUTTONS_FONT,bd=0)
        button.grid(row=0,column=1,sticky=tk.NSEW)

    def sqrt(self):
        if self.current_expression == '':
            return 
        try:
            self.current_expression = str(eval(self.current_expression)**0.5)
            self.update_label()
        except SyntaxError:
            self.current_expression = "Error"
            self.total_expression = ""
            self.update_label()
            self.update_total_label()
        except: pass
        
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame,command=self.sqrt,text="\u221ax",bg=NONE_DIGIT_BUTTONS_COLOR, fg=BUTTONS_COLOR,font=BUTTONS_FONT,bd=0)
        button.grid(row=0,column=2,sticky=tk.NSEW)

        
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,font=SMALL_DISPLAY_FONT,fg=EXPRESSION_COLOR,bg=DISPLAY_FRAME_COLOR,padx=25)
        total_label.pack(pady=35,expand=True,fill="both")
        
        label = tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,font=LARGE_DISPLAY_FONT,fg=EXPRESSION_COLOR,bg=DISPLAY_FRAME_COLOR,padx=25)
        label.pack(pady=70,expand=True,fill="both")
        return total_label,label
    
    def create_display_frame(self):
        '''create the display frame'''
        
        frame = tk.Frame(self.root,width=WIDTH,height=250,bg=DISPLAY_FRAME_COLOR)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        '''create the buttons frame'''
        
        frame = tk.Frame(self.root,width=WIDTH,height=500,bg="green")
        frame.pack(expand=True,fill=tk.BOTH)
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
        
    def create_digit_buttons(self):
        for digit,digit_grid in self.buttons.items():
            button = tk.Button(self.buttons_frame,command=lambda x = digit:self.add_to_expression(x),text=str(digit),bg="white", fg=BUTTONS_COLOR,font=BUTTONS_FONT,bd=0)
            button.grid(row=digit_grid[0],column=digit_grid[1],sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame,command=self.clear_expression,text="C",bg=NONE_DIGIT_BUTTONS_COLOR, fg=BUTTONS_COLOR,font=BUTTONS_FONT,bd=0)
        button.grid(row=0,column=0,sticky=tk.NSEW)

    def evaluate(self):
        '''Evaluates the total expresssion.'''
        try:
            self.total_expression += self.current_expression
            self.update_total_label()
            self.current_expression = str(eval(str(self.total_expression)))
            self.total_expression = ''
            self.update_total_label()
            self.update_label()
        except ZeroDivisionError:
            self.current_expression = "Error"
            self.total_expression = ""
            self.update_label()
            self.update_total_label()
        except:pass
        
    def clear_expression(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_total_label()
        self.update_label()
        
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, command=self.evaluate,text="=",bg=EQUALS_BUTTON_COLOR, fg=BUTTONS_COLOR,font=BUTTONS_FONT,bd=0)
        button.grid(row=4,column=2,columnspan=2,sticky=tk.NSEW)
        
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_label()
        self.update_total_label()   
        
    def create_operator_buttons(self):
        count = 0
        for operator, value in self.operators.items():
            operators_button = tk.Button(self.buttons_frame,command=lambda x = operator: self.append_operator(x), text=value,bg=NONE_DIGIT_BUTTONS_COLOR, fg=BUTTONS_COLOR,font=BUTTONS_FONT,bd=0)
            operators_button.grid(column=3,row=count,sticky=tk.NSEW)
            count += 1

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        # reduce the max len of the current expression to  11
        self.current_expression = self.current_expression
        if len(self.current_expression) >= 11:
            self.current_expression = self.current_expression[:11]
            
        self.label.config(text=self.current_expression[:11])
        
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
