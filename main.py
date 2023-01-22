from tkinter import *

class convert():
    def __init__(self):
        self.win = Tk()
        self.win.config(background='white smoke')
        self.win.resizable(width=False, height=False)
        self.win.geometry("474x317")
        self.win.title('Money Converter')

        # self.num = StringVar()
        self.amountField = Entry()
        self.amountField.grid(row=0, columnspan=5, rowspan=2)
        self.numberval = self.amountField.get()


        self.currencyname = ["Euro", "Dollar", "Dollar Canadien", "Dollar Australien" "Franc Suisse", "Rouble Russe"]
        self.sigle = ["EUR", "USD", "CAD", "AUD", "CHF", "RUB"]
        self.rates = []
        self.dictcurrency = {"Currency": self.currencyname, "Sigle": self.sigle}
        # self.dictcurrency["Currency"] = self.currencyname
        self.get_value()
        self.buttons()

    def get_value(self, amount=1):

        # if self.numberval is True:
        amount = float(self.amountField.get())
        print(amount)
        # else:
        #     int(self.numberval)
        #     total = self.numberval * 1.2
        #     self.num.set(total)
        #     print(self.num)
    def buttons(self):

        self.button_convert = Button(self.win, text="Convert", width=5, height=2, bg="light slate blue", activebackground="slate blue", command=self.get_value(0))
        self.button_convert.grid(row=2, column=1)

    # def newRate(self):


app = convert()
app.win.mainloop()
