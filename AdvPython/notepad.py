import tkinter as tk
from tkinter import filedialog, font, messagebox
import os

# Create the main window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")

# ------------------- Text Area -------------------
text_area = tk.Text(root, undo=True, wrap="word", font=("Consolas", 12))
text_area.pack(expand=True, fill="both")

# Scrollbar
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# ------------------- Menu Bar -------------------
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

current_file = None

def new_file():
    global current_file
    if confirm_save():
        text_area.delete(1.0, tk.END)
        current_file = None
        update_title()

def open_file():
    global current_file
    if confirm_save():
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text_area.delete(1.0, tk.END)
                    text_area.insert(tk.END, f.read())
                current_file = file_path
                update_title()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")

def save_file():
    global current_file
    if current_file:
        try:
            with open(current_file, "w", encoding="utf-8") as f:
                f.write(text_area.get(1.0, tk.END))
            update_title()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text_area.get(1.0, tk.END))
            current_file = file_path
            update_title()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

def confirm_save():
    if text_area.edit_modified():
        response = messagebox.askyesnocancel("Save?", "Do you want to save changes?")
        if response is True:
            save_file()
            return True
        elif response is False:
            return True
        else:
            return False
    return True

def exit_app():
    if confirm_save():
        root.destroy()

def update_title():
    title = os.path.basename(current_file) if current_file else "Untitled"
    root.title(f"{title} - Notepad")

file_menu.add_command(label="New", accelerator="Ctrl+N", command=new_file)
file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=open_file)
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=text_area.edit_undo)
edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=text_area.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: text_area.tag_add("sel", "1.0", "end"))

# Format Menu
format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)

word_wrap = tk.BooleanVar(value=True)
format_menu.add_checkbutton(label="Word Wrap", variable=word_wrap, command=lambda: text_area.config(wrap="word" if word_wrap.get() else "none"))

def change_font():
    font_window = tk.Toplevel(root)
    font_window.title("Font")
    font_window.geometry("300x150")
    font_window.transient(root)
    font_window.grab_set()

    fonts = list(font.families())
    fonts.sort()

    current_font = text_area.cget("font").split()[0]
    current_size = int(text_area.cget("font").split()[1])

    tk.Label(font_window, text="Font:").pack(pady=5)
    font_list = tk.Listbox(font_window, height=6, exportselection=0)
    font_list.pack(fill="x", padx=10)
    for f in fonts[:50]:  # Show first 50 fonts
        font_list.insert(tk.END, f)
    font_list.selection_set(fonts.index(current_font) if current_font in fonts else 0)

    tk.Label(font_window, text="Size:").pack(pady=5)
    size_var = tk.StringVar(value=str(current_size))
    size_entry = tk.Entry(font_window, textvariable=size_var, width=5)
    size_entry.pack()

    def apply_font():
        selected = font_list.get(font_list.curselection())
        size = size_var.get()
        if size.isdigit():
            new_font = (selected, int(size))
            text_area.config(font=new_font)
        font_window.destroy()

    tk.Button(font_window, text="OK", command=apply_font).pack(pady=10)

format_menu.add_command(label="Font...", command=change_font)

# ------------------- Status Bar -------------------
status_bar = tk.Label(root, text="Line 1, Column 1 | Characters: 0", anchor="w", bd=1, relief="sunken")
status_bar.pack(side="bottom", fill="x")

def update_status(event=None):
    cursor_pos = text_area.index(tk.INSERT)
    line, col = cursor_pos.split(".")
    chars = len(text_area.get(1.0, tk.END)) - 1  # Exclude final newline
    status_bar.config(text=f"Line {line}, Column {col} | Characters: {chars}")

text_area.bind("<KeyRelease>", update_status)
text_area.bind("<ButtonRelease-1>", update_status)
update_status()

# ------------------- Start the App -------------------
root.mainloop()
