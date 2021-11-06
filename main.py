from tkinter import *
from tkinter import messagebox
import random
import string
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    password_entry.delete(0, END)
    letters = list(string.ascii_letters )
    numbers = list(string.digits)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


    rand_lett = random.sample(letters, random.randint(8, 10))
    rand_numb = random.sample(numbers, random.randint(2, 4))
    rand_symb = random.sample(symbols, random.randint(2, 4))

    combined = rand_lett + rand_numb + rand_symb
    random.shuffle(combined)

    password = ''.join(combined)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }



    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops!", message="Please make sure not to leave any fields empty.")
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
                json.dump(data, data_file, indent=4)
        #finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="Existing file with passwords not found. Try creating one!")
    else:
        try:
            website = website_entry.get().title()
            website_data = data[website]
            messagebox.showinfo(title=website, message=f"Email: {website_data['email']}\nPassword: "
                                                         f"{website_data['password']}")
        except KeyError:
            messagebox.showerror(title="Oops!", message="Entry not found!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


### Labels:

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", justify="right")
password_label.grid(column=0, row=3)

### Entry fields:

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, )
website_entry.focus()


email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "your@mail.com")


password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)


### Buttons:

gen_pass_button = Button(text="Generate Password", command=generate)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()


