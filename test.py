from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.config(background='white smoke')
win.resizable(width=False, height=False)
win.geometry("674x717")
win.title('Money Converter')

#Rates of each currency
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

#dict of currencynames
currencyname = ["Euro", "Dollar", "Dollar Canadien", "Dollar Australien", "Franc Suisse", "Rouble Russe"]
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
selected3 = ""
selected4 = ""

def convert():
    global currencyname, historique, values, selected3, selected4
    amount = float(val.get())
    selected1 = var1.get()
    selected2 = var2.get()
    vale = currencyname[-1]

    if selected1 == "Euro":
        if selected1 != selected2:
            for keys in range(len(EURrates)):
                # used to convert
                result = amount * EURrates[selected2][0]
                print(EURrates[selected2][0])
                str_sum = str(result) + EURrates[selected2][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(EURrates[selected2][0]) + " = " + str(result)
                str_rate = "1 " + selected1 + " = " + str(EURrates[selected2][0]) + " " + EURrates[selected2][1]
                str_histo = str_rate + ":  " + str_calcul
                histon.insert(0, str_histo)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot Eur in Eur")

    elif selected1 == "Dollar":
        if selected1 != selected2:
            for x in range(len(USDrates)):
                # used to convert
                result = amount * USDrates[selected2][0]
                str_sum = str(result) + USDrates[selected2][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(USDrates[selected2][0]) + " = " + str(result)
                str_rate = "1 " + selected1 + " = " + str(USDrates[selected2][0]) + " " + USDrates[selected2][1]
                str_histo = str_rate + ": " + str_calcul
                historique.append(str_histo)
                print(historique)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot convert USD in USD")

    elif selected1 == "Dollar Canadien":
        if selected1 != selected2:
            for x in range(len(CADrates)):
                # used to convert
                result = amount * CADrates[selected2][0]
                str_sum = str(result) + CADrates[selected2][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(CADrates[selected2][0]) + " = " + str(result)
                str_rate = "1 " + selected1 + " = " + str(CADrates[selected2][0]) + " " + CADrates[selected2][1]
                str_histo = str_rate + ": " + str_calcul
                historique.append(str_histo)
                print(historique)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot convert CAD in CAD")

    elif selected1 ==  "Dollar Australien":
        if selected1 != selected2:
            for x in range(len(AUDrates)):
                # used to convert
                result = amount * AUDrates[selected2][0]
                str_sum = str(result) + AUDrates[selected2][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(AUDrates[selected2][0]) + " = " + str(result)
                str_rate = "1 " + selected1 + " = " + str(AUDrates[selected2][0]) + " " + AUDrates[selected2][1]
                str_histo = str_rate + ": " + str_calcul
                historique.append(str_histo)
                print(historique)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot convert AUD in AUD")

    elif selected1 ==  "Franc Suisse":
        if selected1 != selected2:
            for x in range(len(CHFrates)):
                # used to convert
                result = amount * CHFrates[selected2][0]
                str_sum = str(result) + CHFrates[selected2][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(CHFrates[selected2][0]) + " = " + str(result)
                str_rate = "1 " + selected1 + " = " + str(CHFrates[selected2][0]) + " " + CHFrates[selected2][1]
                str_histo = str_rate + ": " + str_calcul
                historique.append(str_histo)
                print(historique)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot convert CHF in CHF")

    elif selected1 == "Rouble Russe":
        if selected1 != selected2:
            for x in range(len(RUBrates)):
                # used to convert
                result = amount * RUBrates[selected2][0]
                str_sum = str(result) + RUBrates[selected2][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(RUBrates[selected2][0]) + " = " + str(result)
                str_rate = "1 " + selected1 + " = " + str(RUBrates[selected2][0]) + " " + RUBrates[selected2][1]
                str_histo = str_rate + ": " + str_calcul
                historique.append(str_histo)
                print(historique)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot convert RUB in RUB")

    elif selected3 == vale:
        if selected3 != selected4:
            for x in range(len(new_rates)):
                # used to convert
                result = amount * new_rates[selected4][0]
                str_sum = str(result) + new_rates[selected4][1]
                label.config(text=str_sum)
                # used to create historique
                str_calcul = str(amount) + " * " + str(new_rates[selected4][0]) + " = " + str(result)
                str_rate = "1 " + selected3 + " = " + str(new_rates[selected4][0]) + " " + new_rates[selected4][1]
                str_histo = str_rate + ": " + str_calcul
                historique.append(str_histo)
                print(historique)
                break
        else:
            val.delete(0, END)
            val.insert(END, "Error, you cannot Euros in Euros")


Label(win, text="Add new rate", font=('Calibri 10')).pack()
val2 = Entry(win, width=35)
val2.pack()


def add_currency():
    global box1, box2, new_rates, values, selected3, selected4
    selected3 = var1.get()
    selected4 = var2.get()

    new_rate = val2.get()
    values = new_rate.split()
    currencyname.append(values[0])

    rate_value = float(values[1])
    new_rates = RUBrates.copy()
    new_rates["Rouble Russe"] = [1.1, " RUB"]

    if values[0] == selected3:
        currencyname.append(values[0])
        new_rates[values[2]][0] = rate_value
        print(new_rates)
    elif values[0] == selected4:
        match selected3:
            case "Euro":
                currencyname.append(values[0])
                EURrates[values[0]] = [rate_value, values[2]]
                print(EURrates)
            case "Dollar":
                currencyname.append(values[0])
                USDrates[values[0]] = [rate_value, values[2]]
            case "Dollar Canadien":
                currencyname.append(values[0])
                CADrates[values[0]] = [rate_value, values[2]]
            case "Dollar Australien":
                currencyname.append(values[0])
                AUDrates[values[0]] = [rate_value, values[2]]
            case "Franc Suisse":
                currencyname.append(values[0])
                CHFrates[values[0]] = [rate_value, values[2]]
            case "Rouble Russe":
                currencyname.append(values[0])
                RUBrates[values[0]] = [rate_value, values[2]]

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
