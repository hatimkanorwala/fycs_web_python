import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Display entry
display = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=4,
                   width=16, borderwidth=4, relief="ridge", justify="right", bg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=8)

# Button layout: (text, row, column, [columnspan])
buttons = [
    ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('÷', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)
]

def button_click(item):
    current = display.get() 
    
    if item.isdigit() or item == '.':
        display.insert(tk.END, item)
    
    elif item == 'C':
        display.delete(0, tk.END)
    
    elif item == '±':
        if current:
            if current[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
    
    elif item == '%':
        try:
            value = float(current) / 100
            display.delete(0, tk.END)
            display.insert(tk.END, str(value))
        except ValueError:
            messagebox.showerror("Error", "Invalid input")
    
    elif item in '+-×÷':
        # Replace last operator if already present
        if current and current[-1] in '+-×÷':
            display.delete(len(current) - 1, tk.END)
        display.insert(tk.END, item)
    
    elif item == '=':
        try:
            # Replace × and ÷ with * and /
            expression = current.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid expression")

# Create and place buttons
for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) > 3 else 1
    
    # Special styling for operators and equals
    if text in '+-×÷=':
        bg_color = "#ff9500"
        fg_color = "white"
    elif text in 'C±%':
        bg_color = "#a0a0a0"
        fg_color = "black"
    else:
        bg_color = "#e0e0e0"
        fg_color = "black"
    
    button = tk.Button(root, text=text, font=("Arial", 18, "bold"),
                       padx=20, pady=20, bg=bg_color, fg=fg_color,
                       activebackground="#d0d0d0",
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, columnspan=colspan,
                padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)

# Make grid expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the app
root.mainloop()
