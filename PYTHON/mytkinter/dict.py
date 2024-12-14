#print(__import__("os").getcwd())

import tkinter as tk


class Dict:
    def __init__(self,window):
        self.window = window
        window.title("Dictionary")
        
        self.words = {"popular":"person or something which is famous"}

        self.lable = tk.Label(window,text="Input Word!")
        self.lable.place(x=5,y=0)

        self.entry = tk.Entry(window)
        self.entry.place(x=150,y=1)

        self.button = tk.Button(window,text="Search",command=self.search)
        self.button.place(x=5,y=30)

        self.text = tk.Text(window,width=42, height=10)
        self.text.place(x=5,y=66)

        self.exit = tk.Button(window,text="Exit",command=window.destroy)
        self.exit.place(x=200,y=275)
        #set geometry
        window.geometry("430x310")
        
        
    def search(self):
        w = self.entry.get()
        word = self.words.get(w,"'"+w+"' Word not found in the dictionary!")
        self.text.delete(1.0,tk.END)
        self.text.insert(tk.END,word)

    def add_word(self,word,meaning):
        for w in self.words:
            if w == word:
                return word+" exists"
        self.words[word] = meaning
        return str(word)+" added"

    def del_word(self,word):
        
        if word not in self.words:
            return "can only delete existing word!"
        self.words.pop(word)
        return"word deleted"

    def get_all(self):
        return self.words
    
    def update_word(self,word,new_meaning):
        pass

def main():
    window = tk.Tk()
    window.config(bg="lightblue")
    d = Dict(window)
    window.mainloop()
if __name__ == "__main__":
    d = main()














##class Dict:
##    def __init__(self):
##        self.words = {"popular":"person or something which is famous"}
##
##    def search(self, word):
##        if word not in self.words:
##            return str(word)+" not found"
##        return self.words[word]
##
##    def add_word(self,word,meaning):
##        for w in self.words:
##            if w == word:
##                return word+" exists"
##        self.words[word] = meaning
##        return str(word)+" added"
##
##    def del_word(self,word):
##        
##        if word not in self.words:
##            return "can only delete existing word!"
##        self.words.pop(word)
##        return"word deleted"
##
##    def get_all(self):
##        return self.words
##    
##    def update_word(self,word,new_meaning):
##        pass
##
##
##
##
