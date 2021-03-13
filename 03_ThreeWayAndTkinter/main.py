import tkinter as tk
from functools import partial
import random
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__()
        for i in range(5):
            self.rowconfigure(i, weight=1)
            if i != 4:
                self.columnconfigure(i, weight=1)

        self.digits = [(i//4, i%4) for i in range(16)]
        self.digits = random.sample(self.digits, len(self.digits))
        self.win_digits = [(i//4, i%4) for i in range(16)]

        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit, width=2, height=2)
        self.quitButton.grid(row=0, column=2, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.newButton = tk.Button(self, text='New', command=self.set_random, width=2, height=2)
        self.newButton.grid(row=0, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

        
        self.digitButtons = []
        for i, (y, x) in enumerate(self.digits[:-1]):
            self.digitButtons.append(tk.Button(self, text=str(i+1), command=partial(self.check_and_update_digits, i), width=2, height=2))
            self.digitButtons[-1].grid(row=y+1, column=x, sticky=tk.N+tk.S+tk.E+tk.W)
    
        print(self.digits[0])
        if  self.digits == self.win_digits:
            messagebox.showinfo("Victory!", "You've won! Congratulations!")  
            self.set_random()#create_widgets=False)


    def set_random(self, create_widgets=True):
        self.digits = random.sample(self.digits, len(self.digits))
        while self.digits == self.win_digits:
            self.digits = random.sample(self.digits, len(self.digits))
        for wid_idx in range(len(self.digitButtons)):
            self.digitButtons[wid_idx].destroy()
        if create_widgets:    
            self.createWidgets()        

    def check_and_update_digits(self, digit_idx):
        for neighbour_y, neighbour_x in [(self.digits[digit_idx][0] + i, self.digits[digit_idx][1] + j) for i, j in [[0, 1], [0, -1], [-1, 0], [1, 0]]]:
            if neighbour_y == self.digits[-1][0] and neighbour_x == self.digits[-1][1]:
                self.digits[digit_idx], self.digits[-1] = self.digits[-1], self.digits[digit_idx]
                for wid_idx in range(len(self.digitButtons)):
                    self.digitButtons[wid_idx].destroy()
                self.createWidgets()
                break


app = Application()
#app.master.title('Sample application')
app.mainloop()
