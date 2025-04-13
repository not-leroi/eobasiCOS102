import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def welcomeMessage(username):
    # Create a new window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}!\n", font=('Arial', 14))
    label_1.pack(pady=10)

    label_2 = tk.Label(window, text="This is Python GUI with Tkinter", font=('Arial', 12))
    label_2.pack()

def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x250")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Login", command=submit)
submit_button.pack(pady=20)

root.mainloop()
