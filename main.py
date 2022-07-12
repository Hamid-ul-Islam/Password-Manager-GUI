from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# generate password
def pass_gen():
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

  password = ""
  for char in password_list:
    password += char
  password_entry.delete(0, END)
  password_entry.insert(0, password)
  pyperclip.copy(password)


# saving password to a file
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    json_data = {
    website : {
        "Email" : email,
        "Password" : password
    }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Don't Leave any fields empty")
    else:
        try:
            with open('password.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('password.json', 'w') as file:
                json.dump(json_data, file, indent=4)
                messagebox.showinfo(title="Saved", message="The Password was Saved")
        else:
            data.update(json_data)
            with open('password.json', 'w') as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo(title="Saved", message="The Password was Saved")
        finally:
            pass
# searching password
def find_pass():
  website = website_entry.get()
  try:
    with open('password.json', 'r') as file:
      data = json.load(file)
      if website in data:
        email = data[website]["Email"]
        password = data[website]["Password"]

        messagebox.showinfo(title=f"{website} Found", message=f"Email: {email}\nPassword: {password}")
      else:
        messagebox.showinfo(title="Not Found", message=f"No Records found for: {website}")
  except:
    messagebox.showinfo(title="Not Found", message="Nothing is Saved Yet.\nFirst add some records")

window = Tk()
window.title("Secure Password Manager")
window.config(padx=50, pady=30)
logo = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(110, 100, image=logo)
canvas.grid(row=0, column=1)

# levels
website_level = Label(text="Website:")
website_level.grid(row=1, column=0)
email_level = Label(text="Email/Username:")
email_level.grid(row=2, column=0)
password_level = Label(text="Password:")
password_level.grid(row=3, column=0)

# Entries
website_entry = Entry(width=27)
website_entry.grid(row=1, column=1)
website_entry.insert(0, "https://")
website_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, pady=2, columnspan=2)
email_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=find_pass)
search_button.grid(row=1, column=2 )
generate_button = Button(text="Generate Password", command=pass_gen)
generate_button.grid(row=3, column=2)
add_button = Button(text="Save", width=39, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()