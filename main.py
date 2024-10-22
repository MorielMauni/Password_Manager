from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''
    The function created for the 'Generate Password' button on the GUI
    it generate a random password with:
    8-10 lettes, 2-4 symbols and 2-4 numbers
    in a shuffle order each time -> delete the oold entry and create a new one
    Copy the generated password to the clipboard with 'pyperclip'
    :return: A very strong password
    '''
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
    '''
    This function created for the 'Add' button on the GUI.
    it checls the entries of the: website, email and password -> if fails, an error box appears,
    take them to a final checl with a messagebox 'ok' or 'cancel -> 'ok' to continue'
    then, creats (if needed) or adds to the file 'data.txt' the entries as formeted
    WEBSITE | USERNAME/EMAIL | PASSWORD
    the website and password entries gets clean for a new add
    '''
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showerror(title="ERROR", message="Please fill all the fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Username/Email: {email}\nPassword: {password}\nPress 'ok' to save or 'cancel' to return")
        if is_ok:
            with open("data.txt", "a") as data_file: # Make a file to save the details
                data_file.write(f"{website} | {email} | {password}\n")
                # Delete the last entrys
                website_entry.delete(0, END)
                password_entry.delete(0, END)
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
website_labal = Label(text="Website:")
website_labal.grid(row=1 , column=0)

email_labal = Label(text="Email/Username:")
email_labal.grid(row=2 , column=0)

password_labal = Label(text="Password:")
password_labal.grid(row=3 , column=0)

# Entrys
website_entry = Entry(width=45)
website_entry.grid(row=1 , column=1, columnspan=2)

email_entry = Entry(width=45)
email_entry.grid(row=2 , column=1, columnspan=2)
email_entry.insert(END, "user@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(row=3 , column=1)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3 , column=2)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4 , column=1, columnspan=2)

window.mainloop()