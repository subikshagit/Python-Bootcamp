# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

import json
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+','[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`', '~']

    letter_count = 4
    numbers_count = 4
    symbols_count = 4

    password =[]

    for j in range(letter_count):
        password.append(random.choice(letters))

    for k in range(numbers_count):
        password.append(random.choice(numbers))

    for l in range(symbols_count):
        password.append(random.choice(symbol))

    random.shuffle(password)
    password_str = ''.join(password)
    password_entry.delete(0,END)
    password_entry.insert(0, password_str)
    return password_str
# ---------------------------- SEARCH PASSWORD ------------------------------- #
from tkinter import messagebox
def search():
    website= website_entry.get()
    print(website)
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
        return

    with open("data.txt", "r") as data_file:
        line = data_file.readlines()
        for i in line:
            if website in i:
                try:
                    splt = i.split(" | ")
                    messagebox.showinfo(title=website, message=f"Email: {splt[1]} \nPassword: {splt[2]}")
                    return
                except IndexError:
                    messagebox.showinfo(title="Error", message="Data format error.")
                    return
        messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
        return
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_Entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) != 0 or len(password) != 0:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                email_Entry.insert(0, "example@example.com")

            
    else:
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        email_Entry.delete(0,END)
        email_Entry.insert(0, "example@example.com")

        return
    
        
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=300, height=200)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label = Label(text='Website:',highlightthickness=0)
label.grid(row=1, column=0,columnspan=1,sticky=E)

#ENTRY
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2,)
website_entry.focus()


label = Label(text='Email/Username:',highlightthickness=0)
label.grid(row=2, column=0,columnspan=1)



email_Entry = Entry(width=35)
email_Entry.grid(row=2, column=1, columnspan=2)
email_Entry.insert(0, "example@example.com")


label = Label(text='Password:')
label.grid(row=3, column=0,sticky=E,columnspan=1)


password_entry = Entry(width=25)
password_entry.grid(row=3, column=1,sticky=E)



generate_password_button = Button(text="GeneratePassword",width=14)
generate_password_button.grid(row=3, column=2)
generate_password_button.config(command=generate_password)

add_button = Button(text="Add",width=30, command=save)
add_button.grid(row=4, column=1,columnspan=2)
add_button.config(command=save)


search_button = Button(text="Search",width=13,command=search)
search_button.grid(row=1, column=2,sticky=E)
search_button.config(command=search)

window.mainloop()