from tkinter import *

class convert():
    def __init__(self):
        self.win = Tk()
        self.win.config(background='white smoke')
        self.win.resizable(width=False, height=False)
        self.win.geometry("474x317")
        self.win.title('Money Converter')

        self.storedvalue = ""
        self.currencyname = ["Euro", "Dollar", "Dollar Canadien", "Dollar Australien" "Franc Suisse", "Rouble Russe"]
        self.sigle = ["EUR", "USD", "CAD", "AUD", "CHF", "RUB"]
        self.rates = []
        self.dictcurrency = {}
        self.dictcurrency["Currency"] = self.currencyname

    # def getValue(self):

    # def newRate(self):


app = convert()
app.win.mainloop()
