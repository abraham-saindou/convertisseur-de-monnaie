from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.config(background='white smoke')
win.resizable(width=False, height=False)
win.geometry("674x717")
win.title('Money Converter')

# Names and Rates of each currency
EURrates = {"Dollar": [1.087, "USD"], "Dollar Canadien": [1.453, "CAD"], "Dollar Australien": [1.549, "AUD"],
            "Franc Suisse": [1.004, "CHF"], "Rouble Russe": [74.775, "RUB"]}
USDrates = {"Euro": [0.919, "EUR"], "Dollar Canadien": [1.336, "CAD"], "Dollar Australien": [1.425, "AUD"],
            "Franc Suisse": [0.923, "CHF"], "Rouble Russe": [68.765, "RUB"]}
CADrates = {"Euro": [0.689, "EUR"], "Dollar": [0.748, "USD"], "Dollar Australien": [1.067, "AUD"],
            "Franc Suisse": [0.691, "CHF"], "Rouble Russe": [51.472, "RUB"]}
AUDrates = {"Euro": [0.645, "EUR"], "Dollar": [0.702, "USD"], "Dollar Canadien": [0.938, "CAD"],
            "Franc Suisse": [0.648, "CHF"], "Rouble Russe": [48.26, "RUB"]}
CHFrates = {"Euro": [0.995, "EUR"], "Dollar": [1.082, "USD"], "Dollar Canadien": [1.446, "CAD"],
            "Dollar Australien": [1.543, "AUD"], "Rouble Russe": [109.937, "RUB"]}
RUBrates = {"Euro": [0.013, "EUR"], "Dollar": [0.014, "USD"], "Dollar Canadien": [0.019, "CAD"],
            "Dollar Australien": [0.021, "AUD"], "Franc Suisse": [0.009, "CHF"]}
new_rates = {}

currencyname = ["Euro", "Dollar", "Dollar Canadien", "Dollar Australien", "Franc Suisse", "Rouble Russe"]
dict_ofdict = {currencyname[0]: EURrates, currencyname[1]: USDrates, currencyname[2]: CADrates,
               currencyname[3]: AUDrates, currencyname[4]: CHFrates, currencyname[5]: RUBrates}

# currency choices
Label(win, text="From", font=('Calibri 10')).place(x=10, y=3)
var1 = StringVar()
var1.set(currencyname[0])
box1 = OptionMenu(win, var1, *currencyname)
box1.place(x=100, y=3)

Label(win, text="To", font=('Calibri 10')).place(x=10, y=40)
var2 = StringVar()
var2.set(currencyname[1])
box2 = OptionMenu(win, var2, *currencyname)
box2.place(x=100, y=40)

Label(win, text="Enter Amount to convert", font=('Calibri 10')).pack()
val = Entry(win, width=35)
val.pack()

values = ["", 1.2, ""]
historique = []


def convert():
    global currencyname, historique, values
    amount = float(val.get())
    selected1 = var1.get()
    selected2 = var2.get()

    for items in currencyname:
        if selected1 in currencyname and selected1 != selected2:
            for keys in range(len(dict_ofdict[selected1])):
                # used to convert
                result = amount * dict_ofdict[selected1][selected2][0]

                print(dict_ofdict[selected1][selected2][0])
                str_sum = str(result) + " " + dict_ofdict[selected1][selected2][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(dict_ofdict[selected1][selected2][0]) + " = " + str(result)
                str_rate = "1 " + selected1 + " = " + str(dict_ofdict[selected1][selected2][0]) + " " + dict_ofdict[selected1][selected2][1]
                str_histo = str_rate + ":  " + str_calcul
                histon.insert(0, str_histo)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot convert a currency into the same")

Label(win, text="Add new rate", font=('Calibri 10')).pack()
val2 = Entry(win, width=35)
val2.pack()


def add_currency():
    global box1, box2, new_rates, values
    new = val2.get()
    values = new.split()
    currencyname.append(values[0])

    rate_value = float(values[1])
    new_rates = RUBrates.copy()
    new_rates["Rouble Russe"] = [0.1, " RUB"]
    # print(dict_ofdict)


# enter new currency, the output currency name (Euro, Dollar) and its rate
    # Yen 1.24 Dollar
    if len(values) == 3:
        dict_ofdict[]
        new_rates[values[2]][0] = rate_value
        print(new_rates)
# enter new currency, its rate, the new sigle, and the existing currecency (Euro, Dollar)
    #Yen 0.25 JPY Euro
    elif len(values) > 3:
        addto = {values[0]: [rate_value, values[2]]}
        print(addto)
        dict_ofdict[values[3]].update(addto)
        print(dict_ofdict)

    box1.destroy()
    box2.destroy()

    box1 = OptionMenu(win, var1, *currencyname)
    box2 = OptionMenu(win, var2, *currencyname)
    box1.place(x=100, y=3)
    box2.place(x=100, y=40)


# Create an Entry widget
label = Label(win, text="Total Sum : ", font=('Calibri 15'))
label.pack(pady=20)

button_conv = Button(win, text="Calculate Sum", command=convert).pack()
button_add = Button(win, text="Add new rate", command=add_currency).pack()

histon = Listbox(win, width=30, height=10, listvariable=historique)
histon.pack()

win.mainloop()
