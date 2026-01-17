import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

def fetch_data_from_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',        
            database='burhani_fy',  
            user='root',           
            password='admin'    
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT id, username, password, email, contact, gender FROM user")
            rows = cursor.fetchall()
            return rows

    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL: {e}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def display_users():
    root = tk.Tk()
    root.title("Users Database - Grid View")
    root.geometry("900x600")
    root.configure(bg="#f4f4f4")

    # Title
    title = tk.Label(root, text="Registered Users ", font=("Helvetica", 20, "bold"), bg="#f4f4f4")
    title.pack(pady=20)

    # Frame for Treeview and Scrollbars
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10, fill="both", expand=True)

    # Scrollbars
    v_scroll = ttk.Scrollbar(frame, orient="vertical")
    h_scroll = ttk.Scrollbar(frame, orient="horizontal")

    # Treeview Table
    columns = ("User ID", "Name", "Password", "Email", "Contact", "Gender")
    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings",
        yscrollcommand=v_scroll.set,
        xscrollcommand=h_scroll.set
    )

    v_scroll.config(command=tree.yview)
    v_scroll.pack(side="right", fill="y")
    h_scroll.config(command=tree.xview)
    h_scroll.pack(side="bottom", fill="x")

    # Column Configuration
    tree.heading("User ID", text="User ID")
    tree.heading("Name", text="Name")
    tree.heading("Password", text="Password")
    tree.heading("Email", text="Email")
    tree.heading("Contact", text="Contact")
    tree.heading("Gender", text="Gender")

    tree.column("User ID", width=80, anchor="center")
    tree.column("Name", width=150, anchor="w")
    tree.column("Password", width=120, anchor="center")  # Will show masked
    tree.column("Email", width=250, anchor="w")
    tree.column("Contact", width=130, anchor="center")
    tree.column("Gender", width=100, anchor="center")

    # Striped row colors
    tree.tag_configure("oddrow", background="#ffffff")
    tree.tag_configure("evenrow", background="#f9f9f9")

    # Fetch data
    rows = fetch_data_from_mysql()

    if not rows:
        no_data = tk.Label(root, text="No users found or connection failed.", font=("Arial", 14), fg="red")
        no_data.pack(pady=50)
    else:
        for i, row in enumerate(rows):
            # Mask password for display
            display_row = list(row)
            # Hide actual password
            #display_row[2] = "••••••••"  
            
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            tree.insert("", "end", values=display_row, tags=(tag,))

    tree.pack(fill="both", expand=True)

    # Double-click to show full details (including real password if needed)
    def on_double_click(event):
        item = tree.selection()
        if item:
            values = tree.item(item, "values")
            actual_row = rows[tree.index(item)]
            messagebox.showinfo("User Details",
                                f"User ID: {actual_row[0]}\n"
                                f"Name: {actual_row[1]}\n"
                                f"Password: {actual_row[2]}\n"  # Shows real password here
                                f"Email: {actual_row[3]}\n"
                                f"Contact: {actual_row[4]}\n"
                                f"Gender: {actual_row[5]}")

    tree.bind("<Double-1>", on_double_click)

    # Refresh button (optional)
    refresh_btn = tk.Button(root, text="Refresh Data", font=("Arial", 12), bg="#4CAF50", fg="white",
                            command=lambda: refresh_table(tree))
    refresh_btn.pack(pady=10)

    def refresh_table(tree_widget):
        for item in tree_widget.get_children():
            tree_widget.delete(item)
        new_rows = fetch_data_from_mysql()
        global rows
        rows = new_rows
        for i, row in enumerate(new_rows):
            display_row = list(row)
            #display_row[2] = "••••••••"
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            tree_widget.insert("", "end", values=display_row, tags=(tag,))

    root.mainloop()

# Run the app
if __name__ == "__main__":
    display_users()
