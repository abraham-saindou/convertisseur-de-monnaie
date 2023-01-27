from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()
# Set the size of the tkinter window
win.config(bg='grey40')
win.resizable(width=False, height=False)
win.geometry("674x477")
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
currencyname = ["Euro", "Dollar", "Dollar Canadien", "Dollar Australien", "Franc Suisse", "Rouble Russe"]
dict_ofdict = {currencyname[0]: EURrates, currencyname[1]: USDrates, currencyname[2]: CADrates,
               currencyname[3]: AUDrates, currencyname[4]: CHFrates, currencyname[5]: RUBrates}
# currency choices and dispositions
Label(win, text="From", font=('Calibri 12'),bg='grey40').place(x=0, y=50)
var1 = StringVar()
var1.set(currencyname[2])
box1 = OptionMenu(win, var1, *currencyname)
box1.config(font=("Arial"), bg="light slate blue", activebackground="slate blue")
box1.place(x=45, y=47)

Label(win, text="To", font=('Calibri 12'),bg='grey40').place(x=0, y=125)
var2 = StringVar()
var2.set(currencyname[3])
box2 = OptionMenu(win, var2, *currencyname)
box2.config(font=("Arial"), bg="light slate blue", activebackground="slate blue")
box2.place(x=45, y=121)

Label(win, text="Amount to convert", font=('Calibri 15'),bg='grey40').place(x=270, y=12)
val = Entry(win, width=35, font="Arial, 13", bg="lightcyan2")
val.place(x=200, y=50)
historique = []


def make_dict(new):
    # Function which creates a new dict appended dict_ofdict, every time user input new name
    for items in new:
        items = RUBrates.copy()
        items["Rouble Russe"] = [0.5, "RUB"]
        dict_ofdict[currencyname[-1]] = items
    return dict_ofdict


def convert():
    # Getting amount and currencies
    try:
        amount = float(val.get())
    except:
        val.delete(0, END)
        label.config(text="Error, conversion not allowed !")
    from_curren = var1.get()
    to_curren = var2.get()

    # Method finding user's selected currencies
    if from_curren in currencyname and from_curren != to_curren:
        for keys in range(len(dict_ofdict[from_curren])):
            # Evaluates the conversion and format it to display 3 decimals places
            result = "{0:.3f}".format(amount * dict_ofdict[from_curren][to_curren][0])
            str_sum = str(result) + " " + dict_ofdict[from_curren][to_curren][1]
            label.config(text=str_sum)
            # used to create historique
            str_calcul = str(amount) + " * " + str(dict_ofdict[from_curren][to_curren][0]) + " = " + str(result)
            str_rate = "1 " + from_curren + " = " + str(dict_ofdict[from_curren][to_curren][0]) + " " + \
                       dict_ofdict[from_curren][to_curren][1]
            str_histo = str_rate + " | " + str_calcul
            histon.insert(0, str_histo)
            break
    else:   # Throw an error user try to convert
        val.delete(0, END)
        label.config(text="Error, conversion not allowed !")

txt1 = "Type like this to add new input currency : Yen 0.25 JPY Euro"
txt2 = "Type like this to add new output currency : Yen 1.24 Dollar"

Label(win, text=txt1, font=('Calibri 10'),bg='grey40').place(x=300, y=175)
Label(win, text=txt2, font=('Calibri 10'),bg='grey40').place(x=300, y=205)
val2 = Entry(win, width=35, font="Arial, 13", bg="lightcyan2")
val2.place(x=200, y=121)

histon = Listbox(win, width=70, height=10, listvariable=historique, justify=CENTER, bg="lightcyan2")
histon.place(x=20, y=250)

def add_currency():
    global box1, box2
    new = val2.get()
    values = new.split()
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # List used to look for numbers in values
    for x in num:
        x = int(x)
        if num[x] in values[0]:
            val.delete(0, END)
            label.config(text="Error, conversion not allowed !")
    for inter in num:
        if inter == str(values[1])[0]:
            values[1] = float(values[1])
            if len(values) <= 4 and len(values[2]) > 3:
                if len(values) == 3:
                    if values[0] not in currencyname:
                        currencyname.append(values[0])
                    mydict = make_dict(values[0])
                    dict_ofdict[values[0]][values[2]][0] = values[1]
                    str_info = values[2] + " => " + values[0]
                    label.config(text=str_info)
                else:
                    if values[0] not in currencyname:
                        currencyname.append(values[0])
                    name1 = values[2] + " " + values[3]
                    mydict = make_dict(values[0])
                    dict_ofdict[values[0]][name1][0] = values[1]
                    str_info = values[2] + " => " + name1
                    label.config(text=str_info)
        elif inter == str(values[2])[0]:
            part = values.pop(1)
            values[0] = values[0] + " " + part
            if currencyname[-1] not in currencyname:
                currencyname.append(values[0])
            values[1] = float(values[1])
            if len(values) <= 4 and len(values[2]) > 3:
                if len(values) == 4:
                    name1 = values[2] + " " + values[3]
                    if values[0] not in currencyname:
                        currencyname.append(values[0])
                    mydict = make_dict(values[0])
                    dict_ofdict[values[0]][name1][0] = values[1]
                    str_info = values[2] + " => " + values[0]
                    label.config(text=str_info)
                else:
                    if values[0] not in currencyname:
                        currencyname.append(values[0])
                    mydict = make_dict(values[0])
                    dict_ofdict[values[0]][values[2]][0] = values[1]
                    str_info = values[2] + " => " + values[0]
                    label.config(text=str_info)
    # Yen 0.25 JPY Euro
    if len(values) >= 4 and len(values[2]) == 3:
        rate_value = values[1]
        if len(values) == 5:
            values[3] = values[3] + " " + values[4]
            addto = {values[0]: [rate_value, values[2]]}
            dict_ofdict[values[3]].update(addto)
            if values[0] not in currencyname:
                currencyname.append(values[0])
            str_info = values[3] + " <= " + values[0]
            label.config(text=str_info)
        else:
            addto = {values[0]: [rate_value, values[2]]}
            print(addto)
            dict_ofdict[values[3]].update(addto)
            if values[0] not in currencyname:
                currencyname.append(values[0])
            str_info = values[3] + " <= " + values[0]
            label.config(text=str_info)

    box1.destroy()  # Destroying list menu and creating new
    box2.destroy()

    box1 = OptionMenu(win, var1, *currencyname)
    box2 = OptionMenu(win, var2, *currencyname)
    box1.config(font=("Arial"), bg="light slate blue", activebackground="slate blue")
    box1.place(x=45, y=47)
    box2.config(font=("Arial"), bg="light slate blue", activebackground="slate blue")
    box2.place(x=45, y=121)


def clearHistorique():
    histon.delete(0, END)


# Display result and errors
label = Label(win, text="Total Sum : ", font=('Calibri 15'),bg='grey40')
label.place(x=5, y=185)
# Creating buttons
button_conv = Button(win, text="Calculate Sum", command=convert, bg="light slate blue",
                     activebackground="slate blue",).place(x=550, y=50)
button_add = Button(win, text="Add new rate", command=add_currency, bg="light slate blue",
                    activebackground="slate blue",).place(x=550, y=120)
button_clear = Button(win, text="Effacer historique", command=clearHistorique, bg="light slate blue",
                      activebackground="slate blue",).place(x=530, y=250)
win.mainloop()