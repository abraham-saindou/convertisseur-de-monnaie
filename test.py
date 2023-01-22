from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.config(background='white smoke')
win.resizable(width=False, height=False)
win.geometry("474x317")
win.title('Money Converter')

currencyname = ["Euro", "Dollar", "Dollar Canadien", "Dollar Australien", "Franc Suisse", "Rouble Russe"]
sigle = ["EUR", "USD", "CAD", "AUD", "CHF", "RUB"]

EURrates = {"Dollar": 1.1, "Dollar Canadien": 1.2, "Dollar Australien": 1.3, "Franc Suisse": 1.4, "Rouble Russe": 1.5}
USDrates = {"Euro": 1.1, "Dollar Canadien": 1.2, "Dollar Australien": 1.3, "Franc Suisse": 1.4, "Rouble Russe": 1.5}
CADrates = {"Euro": 1.1, "Dollar": 1.2, "Dollar Australien": 1.3, "Franc Suisse": 1.4, "Rouble Russe": 1.5}
AUDrates = {"Euro": 1.1, "Dollar": 1.2, "Dollar Canadien": 1.3, "Franc Suisse": 1.4, "Rouble Russe": 1.5}
CHFrates = {"Euro": 1.1, "Dollar": 1.2, "Dollar Canadien": 1.3, "Dollar Australien": 1.4, "Rouble Russe": 1.5}
RUBrates = {"Euro": 1.1, "Dollar": 1.2, "Dollar Canadien": 1.3, "Dollar Australien": 1.4, "Franc Suisse": 1.5}

dictcurrency = {"Currency": currencyname, "Sigle": sigle}

# currency choices
var1 = StringVar()
var1.set(dictcurrency["Currency"][0])
box1 = OptionMenu(win, var1, *currencyname)
box1.pack()
selected1 = var1.get()

var2 = StringVar()
var2.set(dictcurrency["Currency"][1])
box2 = OptionMenu(win, var2, *currencyname)
box2.pack()
selected2 = var2.get()

Label(win, text="Enter Amount to convert", font=('Calibri 10')).pack()
val = Entry(win, width=35)
val.pack()

historique = []
# for selected2 in EURrates:
#     somme = amount * EURrates[selected2]

def convert():
    global selected1, selected2, currencyname, historique
    amount = float(val.get())
    match selected1:
        case "Euro":
            for x in range(len(EURrates)):
                somme = amount * EURrates[selected2]
                historique.append(somme)
                label.config(text=somme)
                break
        case "Dollar":
            for x in range(len(EURrates)):
                somme = amount * EURrates[selected2]
                historique.append(somme)
                label.config(text=somme)
                break
        case "Dollar Canadien":
            for x in range(len(EURrates)):
                somme = amount * EURrates[selected2]
                print(somme)
                label.config(text=somme)
                break
        case "Dollar Australien":
            for x in range(len(EURrates)):
                somme = amount * EURrates[selected2]
                historique.append(somme)
                label.config(text=somme)
                break
        case "Franc Suisse":
            for x in range(len(EURrates)):
                somme = amount * EURrates[selected2]
                historique.append(somme)
                label.config(text=somme)
                break
        case "Rouble Russe":
            for x in range(len(EURrates)):
                somme = amount * EURrates[selected2]
                historique.append(somme)
                label.config(text=somme)
                break


# Create an Entry widget
label = Label(win, text="Total Sum : ", font=('Calibri 15'))
label.pack(pady=20)

Button(win, text="Calculate Sum", command=convert).pack()

win.mainloop()
