import tkinter as tk

digits = [(i//4, i%4) for i in range(16)]

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=0, column=1)
        self.newButton = tk.Button(self, text='New', command=self.set_random)
        self.newButton.grid(row=0, column=0)

        self.digitButtons = []
        for i, (y, x) in enumerate(digits[:-1]):
            self.digitButtons.append(tk.Button(self, text=str(i), command=self.check_and_update_digits))
            self.digitButtons[-1].grid(row=y+1, column=x)


    def set_random(self):
        pass

    def check_and_update_digits(self):
        pass

app = Application()
app.master.title('Sample application')
app.mainloop()
