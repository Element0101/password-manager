#Project description: Password Manager that Generates strong passwords and save them with log data into a txt file
    #using GUI from TKinter Module
#Project from: FreedomOutlines
#Prject start: 31.03.2025, 08:00 Uhr
#Project end: 31.03.2025, 21:00 Uhr

import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

BLACK = "#09122C"
RED = "#E17564"
FONT = "courier"
SHARP_RED = "#872341"
WHITE = "#E5D0AC"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_list = [[random.choice(letters), random.choice(symbols), random.choice(numbers)] for _ in range(8)]
    random.shuffle(password_list)
    password = ""
    for lists in password_list:
        for char in lists:
            password += char
    #Delete the previous password and insert a new one whenever the Generate button is clicked again
    password_input.delete(0, END)
    password_input.insert(0, password)
    #Copy the password automatically whenever a password is generated
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_log_data():
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()

    #Display a popup when the user tries to save data with empty fields
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Empty field", "Dont leave the fields empty!")
    #Ask the user to confirm his data before save
    else:
        is_ok = messagebox.askokcancel(title="conform save", message=f"This is the data you want to save:\nwebsite: {website}"
                                                                     f"\nUsername: {username},\nPassword: {password}"
                                                                     f"\nPress ok to save")
        if is_ok:
            with open("login_data.txt", mode="a") as data:
                data.write(f"{website}, {username}, {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=75, pady=75, bg=BLACK)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BLACK)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(80, 80, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_lbl = Label(text="Website:", fg=RED, bg=BLACK)
website_lbl.grid(column=0, row=1)
email_lbl = Label(text="Email/Username:", fg=RED, bg=BLACK)
email_lbl.grid(column=0, row=2)
password_lbl = Label(text="Password:", fg=RED,bg=BLACK)
password_lbl.grid(column=0, row=3)

#Entries
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "mohammad.raghis@")
password_input = Entry(width=21)
password_input.place(x= 96, y=243)

#Buttons
generate_pass = Button(text="Generate Password", background=WHITE, command=password_generator)
generate_pass.place(x= 231, y=243)
add = Button(text="Add", width=34, bg=WHITE, command=save_log_data)
add.place(y=270, x=96)



window.mainloop()