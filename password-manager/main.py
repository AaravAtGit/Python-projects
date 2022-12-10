from tkinter import *
from tkinter import messagebox
font = ("Arial", 10)
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
        'username': username,
        'password': password
    }
}

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(
            title="opps", message="dont leave any feilds empty")
    else:
        bool = messagebox.askokcancel(
            title=website, message=f"here are the details entered \n email:{username}\n pass{password}\n is it ok to save")

        if bool:
            try:
                with open("data.json", "r") as f:
                    try:
                        data = json.load(f)
                    except:
                        data = dict()
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data,f,indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as f:
                    json.dump(data,f,indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=font)

website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:", font=font)
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=font)
password_label.grid(row=3, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'aaravshishodia5029@gmail.com')


password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)


gen_password = Button(text="Generate Password", command=password_gen)
gen_password.grid(row=3, column=2)

add_button = Button(text="add", width=36, font=font, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
