import tkinter as tk
from tkinter import ttk
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = combo.get()
        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/':
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            res = num1 / num2
        else:
            result_label.config(text="Error: Invalid operation")
            return
        result_label.config(text=f"Result: {res}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("250x200")
# Input for first number
tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)
# Input for second number
tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)
# Operation dropdown
tk.Label(root, text="Operation:").grid(row=2, column=0)
combo = ttk.Combobox(root, values=['+', '-', '*', '/'], state="readonly", width=17)
combo.grid(row=2, column=1, padx=10, pady=5)
# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
