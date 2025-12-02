from tkinter import *


window = Tk()
window.title("Mile to km Converter")

entry = Entry(width=20)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
entry.focus()


label = Label(text="Miles")
label.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text="Km")
label3.grid(column=2, row=1)

def action():
    miles = float(entry.get())
    km = round(miles * 1.60934)

    label_result.config(text=f"{km:.2f}")

button = Button(text='calculate', command=action)
button.grid(column=1, row=2)
label_result = Label(text="0")
label_result.grid(column=1, row=1)

window.minsize(width=300, height=300)
window.config(padx=20, pady=20)
window.mainloop()