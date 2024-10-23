from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    The function created for the 'Generate Password' button on the GUI
    generates a random password with:
    8-10 letters, 2-4 symbols and 2-4 numbers
    in a shuffle order each time -> delete the oold entry and create a new one
    Copy the generated password to the clipboard with 'pyperclip'
    :return: A very strong password
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Copied!", message="Generated password copied to clipboard")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    """
    This function created for the 'Add' button on the GUI.
    it checks the entries of the: website, email and password -> if fails, an error box appears,
    then, if needed, it creates or adds to the file 'data.json' the entries as formated
    the website and password entries gets clean for a new add
    :returns: {"www.example.com": {"email": "user@gmail.com","password": "example123"}}
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # json data
    json_data = {website: {
        "email": email,
        "password": password,
    }

    }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showerror(title="ERROR", message="Please fill all the fields.")
    else:
        try:
            with open("data.json", "r") as data_file: # Writes data to a json file
                # Read old data
                loaded_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(json_data, data_file, indent=4)
        else:
            # Update data
            loaded_data.update(json_data)

            with open("data.json", "w") as data_file:
                # Saving update
                json.dump(loaded_data, data_file, indent=4)
        finally:
                # Delete the last entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search_json():
    """
    This function created for the 'Search' button on the GUI.
    gets the website entry, and check if it exists in the 'data.json' file
    if exists -> a message box with the info appears
    if not exists -> an info message appears
    if FileNotFoundError -> an error message appears
    :return: Username/Email: "user@gmail.com" , Password: "example123"
    """
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No data is saved")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email/Username: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="No Information saved", message=f"No details for the website: {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
# Window Settings
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Insert the image
logo_img = PhotoImage(file="logo.png")
logo_canvas = Canvas(width=200,height=200, highlightthickness=0)
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=27)
website_entry.grid(row=1 , column=1)

email_entry = Entry(width=46)
email_entry.grid(row=2 , column=1, columnspan=2)
email_entry.insert(END, "user@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(row=3 , column=1)

# Buttons
search_button = Button(text="Search", width=15, command=search_json)
search_button.grid(row=1, column=2)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3 , column=2, columnspan=2)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4 , column=1, columnspan=2)

window.mainloop()