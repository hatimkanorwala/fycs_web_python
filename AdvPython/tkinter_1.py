import tkinter as tk
from tkinter import messagebox

def login():
    # Safely get values
    username = entry_username.get().strip() if entry_username else ""
    password = entry_password.get() if entry_password else ""
    # Check if fields are empty
    if not username and not password:
        messagebox.showerror("Error", "Please enter username and password")
        return
    elif not username:
        messagebox.showerror("Error", "Please enter username")
        entry_username.focus()
        return
    elif not password:
        messagebox.showerror("Error", "Please enter password")
        entry_password.focus()
        return
    # Dummy authentication - replace with real logic later
    if username == "admin" and password == "secret":
        messagebox.showinfo("Success", f"Welcome, {username}!\nLogin successful!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Invalid username or password")
        entry_password.delete(0, tk.END)  # Clear password on wrong attempt
        entry_password.focus()
# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("350x280")
root.resizable(False, False)
# Title
tk.Label(root, text="User Login").grid(row=1, column=1)
# Username
tk.Label(root, text="Username:").grid(row=2, column=1)
entry_username = tk.Entry(root, width=30)
entry_username.grid(row=2, column=2)
# Password
tk.Label(root, text="Password:").grid(row=3, column=1)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.grid(row=3, column=2)
# Login Button
tk.Button(root, text="Login", width=15, height=2,command=login).grid(row=4, column=1)
# Focus and Enter key support
entry_username.focus()
root.bind("<Return>", lambda event: login())
# Start the app
root.mainloop()
