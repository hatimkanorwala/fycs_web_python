import tkinter as tk
from tkinter import messagebox
def clear_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_confirm.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    gender_var.set(None)  # Clear radio button selection
    entry_username.focus()
def register():
    username = entry_username.get().strip()
    password = entry_password.get()
    confirm = entry_confirm.get()
    email = entry_email.get().strip()
    contact = entry_contact.get().strip()
    gender = gender_var.get()
    # Validation checks
    if not all([username, password, confirm, email, contact, gender]):
        messagebox.showerror("Error", "All fields are required!")
        return
    if password != confirm:
        messagebox.showerror("Error", "Password and Confirm Password do not match!")
        entry_confirm.focus()
        return
    # Contact: exactly 10 digits
    if not (contact.isdigit() and len(contact) == 10):
        messagebox.showerror("Error", "Contact number must be exactly 10 digits!")
        entry_contact.focus()
        return
    # If all validations pass
    messagebox.showinfo("Success", f"Registration Successful!\n\n"
                                f"Username: {username}\n"
                                f"Email: {email}\n"
                                f"Contact: {contact}\n"
                                f"Gender: {gender}")
    # Optional: Clear fields after successful registration
    clear_fields()
# Create main window
root = tk.Tk()
root.title("User Registration")
root.geometry("450x550")
root.resizable(False, False)
# Title
tk.Label(root, text="Registration Form").grid(row=1, column=1)
# Username
tk.Label(root, text="Username:").grid(row=2, column=1)
entry_username = tk.Entry(root, width=35)
entry_username.grid(row=2, column=2)
# Password
tk.Label(root, text="Password:").grid(row=3, column=1)
entry_password = tk.Entry(root, width=35, show="*")
entry_password.grid(row=3, column=2)
# Confirm Password
tk.Label(root, text="Confirm Password:").grid(row=4, column=1)
entry_confirm = tk.Entry(root, width=35, show="*")
entry_confirm.grid(row=4, column=2)
# Email
tk.Label(root, text="Email:").grid(row=5, column=1)
entry_email = tk.Entry(root, width=35)
entry_email.grid(row=5, column=2)
# Contact
tk.Label(root, text="Contact (10 digits):").grid(row=6, column=1)
entry_contact = tk.Entry(root, width=35)
entry_contact.grid(row=6, column=2)
# Gender
tk.Label(root, text="Gender:").grid(row=7, column=1)
gender_var = tk.StringVar(value=None)
frame_gender = tk.Frame(root)
frame_gender.grid(row=7, column=2)
tk.Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female").pack(side="left")
# Buttons
tk.Button(root, text="Submit", width=15,command=register).grid(row=8, column=1)
tk.Button(root, text="Clear", width=15,command=clear_fields).grid(row=8, column=2)
# Focus on username when window opens
entry_username.focus()
# Allow Enter key to submit
root.bind("<Return>", lambda event: register())
# Start the GUI
root.mainloop()
