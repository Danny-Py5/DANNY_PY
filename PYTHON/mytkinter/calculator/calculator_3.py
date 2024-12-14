"""Calculator module

Author: DannyPy
Date: 8th Jan., 2024

NOTES:
------
*  During the building of the project, i realized the when 0
starts the current expression, it raises a 'SynthaxError'
HOW did I fix it:
---------------
*  def delete_to_left(self):
        a,b = self.current_expression,self.total_expression
        if len(a) == 0 and len(b) > 0:
            b = b[:-1]
            self.update_total_label()
        self.current_expression = self.current_expression[:-1]
        self.update_label()

  that logic don't work because it is not the 'b' am configuring
  in update_total_label(). see the working one on line 137

"""


__version__ = "1.0.0"


__author__ = "DannyPy"
__copyright__ = "copyright 2024 DannyPy"
__date__ = "8th Jan., 2024"
__status__ = "Development"


import tkinter as tk 


C_WIDTH = 400
C_HEIGHT = 800
DISPLAY_BACKGROUND_COLOR = "#444"
BUTTONS_BACKGROUND_COLOR = "#555"
DIGITS_COLOR,LIGHT_GRAY = "#E1E1E1","#E1E1E1"
TOTAL_EXPRESSION_FONT_STYLE = ("Arial 15")
CURRENT_EXPRESSION_FONT_STYLE = ("Arial 30 bold")
DIGIT_BUTTONS_FONT_STYLE= ("Aria 25 bold")
OPERATORS_COLOR = "red"
GREEN_COLOR = "#0F0"
EQUAL_BUTTON_COLOR = "#FFF"
EQUAL_BUTTON_BG_COLOR = "GREEN"



class Calculator:

    def __init__(self):
        """calculator constructor."""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.resizable(False,False)
        x = (self.root.winfo_screenwidth() - C_WIDTH) // 2
        y = (self.root.winfo_screenheight() - C_HEIGHT) // 2
        self.root.geometry("{}x{}+{}+{}".format(C_WIDTH,C_HEIGHT,x,y))

        
        self.display_frame = self.create_display_frame()
        self.total_expression = ''
        self.current_expression = '' 
        self.total_label,self.label = self.create_display_label()
        
        self.digit_buttons = {
            7:(1,0),8:(1,1),9:(1,2),
            4:(2,0),5:(2,1),6:(2,2),
            1:(3,0),2:(3,1),3:(3,2),
            ".":(4,0),0:(4,1)}
        self.operators = {"/":"\u00f7","*":"\u00d7","-":"-","+":"+"}
        self.buttons_frame = self.create_buttons_frame()

        # let the whole buttons contain the button frame
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=2)
            self.buttons_frame.rowconfigure(i, weight=1)
        
        self.create_buttons()
        self.create_operators()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equal_button()
        self.create_delete_to_left_button()
        self.create_sqare_button()

    def create_display_frame(self):
        frame = tk.Frame(self.root,bg=DISPLAY_BACKGROUND_COLOR)
        frame.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
        return frame

    def create_display_label(self):
        total_label = tk.Label(self.display_frame,anchor=tk.E,text=self.total_expression,font=TOTAL_EXPRESSION_FONT_STYLE,bg=DISPLAY_BACKGROUND_COLOR,fg=LIGHT_GRAY)
        total_label.pack(pady=30,fill=tk.BOTH)
        label = tk.Label(self.display_frame,anchor=tk.E,text=self.current_expression,font=CURRENT_EXPRESSION_FONT_STYLE ,bg=DISPLAY_BACKGROUND_COLOR,fg=LIGHT_GRAY)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)
        return total_label, label
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.root,bg=BUTTONS_BACKGROUND_COLOR)
        frame.pack(side=tk.TOP,expand=True,fill=tk.BOTH)
        return frame

    def append_digit(self, value):
        self.current_expression += str(value)
        self.update_label()
        
    def create_buttons(self):
        for digit,digit_grid in self.digit_buttons.items():
            button = tk.Button(self.buttons_frame,command=lambda x=digit: self.append_digit(x),text=str(digit),activeforeground=DIGITS_COLOR,activebackground="#333",font=DIGIT_BUTTONS_FONT_STYLE,fg=DIGITS_COLOR,bg=BUTTONS_BACKGROUND_COLOR,bd=0)
            button.grid(row=digit_grid[0],column=digit_grid[1],sticky=tk.E+tk.W)

    def append_operator(self, operator):
        '''this function updates the total expression with the current expression
           and also clears the current expression.'''
        
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_both_tl()
        
    def create_operators(self):
        i = 0
        for key,value in self.operators.items():
            button = tk.Button(self.buttons_frame,command=lambda x=key: self.append_operator(x),text=value,activeforeground="lightblue",activebackground="#333",font=DIGIT_BUTTONS_FONT_STYLE,fg=GREEN_COLOR,bg=BUTTONS_BACKGROUND_COLOR,bd=0)
            button.grid(row=i,column=3,sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.total_expression = ''
        self.current_expression = ''
        self.update_both_tl()
        
    def create_clear_button(self):
        clear = tk.Button(self.buttons_frame,command=self.clear,text="C",activeforeground="RED",activebackground="#333",font=DIGIT_BUTTONS_FONT_STYLE,fg=GREEN_COLOR,bg=BUTTONS_BACKGROUND_COLOR,bd=0)
        clear.grid(row=0,column=0,sticky=tk.E+tk.W)

    def delete_to_left(self):
        a,b = self.current_expression,self.total_expression
        if len(a) == 0 and len(b) > 0:
            self.total_expression = self.total_expression[:-1]
            self.update_total_label()
        self.current_expression = self.current_expression[:-1]
        self.update_label()
        
    def create_delete_to_left_button(self):
        button = tk.Button(self.buttons_frame,command=self.delete_to_left,text='\u232b',activeforeground="lightblue",activebackground="#333",font=DIGIT_BUTTONS_FONT_STYLE,fg=GREEN_COLOR,bg=BUTTONS_BACKGROUND_COLOR,bd=0)
        button.grid(row=0,column=1,sticky=tk.E+tk.W)

    def square(self):
        try:
            self.current_expression = str(eval(self.current_expression)**2)
            self.update_label()
        except:return 
        
    def create_sqare_button(self):
        button = tk.Button(self.buttons_frame,command=self.square,text='x\u00b2',activeforeground="lightblue",activebackground="#333",font=DIGIT_BUTTONS_FONT_STYLE,fg=GREEN_COLOR,bg=BUTTONS_BACKGROUND_COLOR,bd=0)
        button.grid(row=0, column=2, sticky=tk.NSEW)
        
    def error(self):
        '''shows error'''
        self.current_expression = 'Error'
        self.total_expression = ''
        self.update_both_tl()
        
    def evaluate(self):
        try:
            self.total_expression += self.current_expression
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ''
            self.update_both_tl()
        except ZeroDivisionError:
            self.error()
        except:
            self.error()
            
    def create_equal_button(self):
        button = tk.Button(self.buttons_frame,text="=",command=self.evaluate,activeforeground="lightblue",activebackground=EQUAL_BUTTON_BG_COLOR,font=DIGIT_BUTTONS_FONT_STYLE,fg=EQUAL_BUTTON_COLOR,bg=EQUAL_BUTTON_BG_COLOR,bd=0)
        button.grid(row=4,column=2,columnspan=2,sticky=tk.E+tk.W)

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def update_both_tl(self):
        """to avoid save two lines to code, this func updates
           both the total and current expression at once when called."""
        self.update_total_label()
        self.update_label()
    
    def run(self):
        self.root.mainloop() 


def main():

    calc = Calculator()
    calc.run()


if __name__ == "__main__":
    main()



