import tkinter as tk
import pyperclip
import json

from tkinter import messagebox
from random import choice, randint, shuffle


#Password Generator Project
# ----------------- PASSWORD GENERATOR --------------- #
def generate_password():

    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    symbols = [
        '!', '#', '$', '%', '&', '(', ')', '*', '+', '^', 'π', '÷', '≠', '≈',
        '∞', '√', '∑', '∫', '¬', '∆', '˚', 'µ', '≤', '≥', '~', '∏', '∂', '¢',
        '£', '€', '¥', '₹', '§', '©', '®', '™', '℅', '№', 'Ø', 'Æ', 'Å', 'Þ',
        'ß', 'Ð', '×', '¶'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------- SAVE PASSWORD ---------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------- SEARCH FOR STORED PASSWORD ---------- #
def website_search():

    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error",
                message=f"No details for {website} exist.")


# ---------- UI SETUP ---------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")
email_label = tk.Label(text="Email / Username:")
email_label.grid(row=2, column=0, sticky="E")
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

#Entries
website_entry = tk.Entry()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()
email_entry = tk.Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = tk.Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
search_button = tk.Button(text="Search", command=website_search)
search_button.grid(row=1, column=2, sticky="EW")
generate_password_button = tk.Button(
    text="Generate Password", command=generate_password
)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
