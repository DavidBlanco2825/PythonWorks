from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 100)
    password_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("password_database.json", mode="r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"There's not data for the website: '{website}'")
    else:
        messagebox.showinfo(title=f"{website}", message=f"Email/Username: {email}\nPassword: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooopsie.",
                            message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_database.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password_database.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            # Updating the old data with new data
            data.update(new_data)

            with open("password_database.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 14))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 14))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 14))
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", font=(FONT_NAME, 12), command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, font=(FONT_NAME, 12), command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=17, font=(FONT_NAME, 12), command=search_password)
search_button.grid(column=2, row=1, columnspan=2)

website_entry = Entry(width=18, font=(FONT_NAME, 14))
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35, font=(FONT_NAME, 14))
email_entry.insert(END, string="nobody@nowhere.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=18, font=(FONT_NAME, 14))
password_entry.grid(column=1, row=3)
window.mainloop()
