import tkinter as tk
from tkinter import ttk, messagebox

# Main Application Class
class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Application - Student Records")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")

        # Sample data (in real app, load from database)
        self.students = [
            {"id": 1, "name": "Alice Johnson", "age": 20, "email": "alice@example.com"},
            {"id": 2, "name": "Bob Smith", "age": 22, "email": "bob@example.com"},
            {"id": 3, "name": "Charlie Brown", "age": 19, "email": "charlie@example.com"},
        ]

        self.next_id = 4

        # Title
        title_label = tk.Label(root, text="Student Management System", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)

        # Form Frame
        form_frame = tk.LabelFrame(root, text="Student Details", font=("Helvetica", 12), padx=20, pady=20)
        form_frame.pack(pady=10, padx=20, fill="x")

        # Form Fields
        tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Age:").grid(row=1, column=0, sticky="w", pady=5)
        self.age_entry = tk.Entry(form_frame, width=30)
        self.age_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=2, column=1, pady=5, padx=10)

        # Buttons Frame
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        self.add_btn = tk.Button(btn_frame, text="Add Student", width=12, bg="#4CAF50", fg="white", command=self.add_student)
        self.add_btn.pack(side="left", padx=5)

        self.update_btn = tk.Button(btn_frame, text="Update Student", width=14, bg="#2196F3", fg="white", command=self.update_student, state="disabled")
        self.update_btn.pack(side="left", padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Delete Student", width=14, bg="#f44336", fg="white", command=self.delete_student, state="disabled")
        self.delete_btn.pack(side="left", padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear Fields", width=12, bg="#9E9E9E", fg="white", command=self.clear_fields)
        self.clear_btn.pack(side="left", padx=5)

        # Table Frame
        table_frame = tk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Treeview Table
        columns = ("id", "name", "age", "email")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

        # Column headings
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("age", text="Age")
        self.tree.heading("email", text="Email")

        # Column widths
        self.tree.column("id", width=60, anchor="center")
        self.tree.column("name", width=200, anchor="w")
        self.tree.column("age", width=80, anchor="center")
        self.tree.column("email", width=250, anchor="w")

        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Pack table and scrollbars
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)

        # Load initial data
        self.refresh_table()

    def refresh_table(self):
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert data
        for student in self.students:
            self.tree.insert("", "end", values=(student["id"], student["name"], student["age"], student["email"]))

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.update_btn.config(state="disabled")
        self.delete_btn.config(state="disabled")

    def add_student(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not age or not email:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        if not age.isdigit():
            messagebox.showwarning("Input Error", "Age must be a number!")
            return

        # Add to list
        new_student = {
            "id": self.next_id,
            "name": name,
            "age": int(age),
            "email": email
        }
        self.students.append(new_student)
        self.next_id += 1

        self.refresh_table()
        self.clear_fields()
        messagebox.showinfo("Success", "Student added successfully!")

    def on_item_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return

        values = self.tree.item(selected, "values")
        self.clear_fields()

        # Fill form
        self.name_entry.insert(0, values[1])
        self.age_entry.insert(0, values[2])
        self.email_entry.insert(0, values[3])

        # Enable update and delete buttons
        self.update_btn.config(state="normal")
        self.delete_btn.config(state="normal")

        # Store current selected ID
        self.selected_id = int(values[0])

    def update_student(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not age or not email:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        if not age.isdigit():
            messagebox.showwarning("Input Error", "Age must be a number!")
            return

        # Update in list
        for student in self.students:
            if student["id"] == self.selected_id:
                student["name"] = name
                student["age"] = int(age)
                student["email"] = email
                break

        self.refresh_table()
        self.clear_fields()
        messagebox.showinfo("Success", "Student updated successfully!")

    def delete_student(self):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?"):
            self.students = [s for s in self.students if s["id"] != self.selected_id]
            self.refresh_table()
            self.clear_fields()
            messagebox.showinfo("Success", "Student deleted successfully!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
