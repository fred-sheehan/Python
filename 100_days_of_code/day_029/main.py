import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


# ----- PASSWORD CHARS ----- #
password_chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  '!', '#', '$',
    '%', '&', '(', ')', '*', '+', '_', '^', '§', '°', 'ç', '¨', '£', '¢', '¬',
    'µ', '¶', '•', 'ª', 'º', '°', '¹', '²', '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9','³', '¼', '½', '¾', '€', '¥', '¢', '£', '¤', '¡', '¿', '©',
    '®', '™', '№', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]


# ----- PASSWORD GENERATOR ----- #
def generate_password():
    password_entry.delete(0, tk.END)
    password = "".join(random.choices(password_chars, k=16))
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ----- SAVE PASSWORD ----- #
def add_data():

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title="Confirmation", message=f"Do you want to save the entered data? \n\nWebsite: {website_entry.get()} \nEmail: {email_entry.get()} \nPassword: {password_entry.get()}")

    if not is_ok:
        return
    else:
        with open("data.txt", "a") as file:
            file.write(
                f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
            )
            messagebox.showinfo(title="Success", message="Data saved successfully!")

# ----- UI SETUP ----- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = tk.Entry()
email_entry.insert(0, string="your@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = tk.Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
password_button = tk.Button(
    text="Generate Password", command=generate_password
)
password_button.grid(row=3, column=2)
add_button = tk.Button(
    text="Add", command=add_data
)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
