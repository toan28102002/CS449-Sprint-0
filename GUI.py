import tkinter as tk
from tkinter import ttk

def on_checkbox_toggle():
    """Handles checkbox state change."""
    if checkbox_var.get():
        label.config(text="Checkbox is Checked")
    else:
        label.config(text="Checkbox is Unchecked")

def on_radio_select():
    """Handles radio button selection."""
    selected_option = radio_var.get()
    label.config(text=f"Selected: {selected_option}")

# Create main window
root = tk.Tk()
root.title("SOS GUI Example")
root.geometry("300x250")

# Label
label = ttk.Label(root, text="Welcome to the GUI", font=("Arial", 12))
label.pack(pady=10)

# Canvas (Draws a line)
canvas = tk.Canvas(root, width=200, height=50)
canvas.pack()
canvas.create_line(10, 25, 190, 25, fill="black", width=3)

# Checkbox
checkbox_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(root, text="Check me", variable=checkbox_var, command=on_checkbox_toggle)
checkbox.pack(pady=5)

# Radio buttons
radio_var = tk.StringVar(value="None")
radio1 = ttk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=on_radio_select)
radio2 = ttk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=on_radio_select)
radio1.pack()
radio2.pack()

# Run the GUI
root.mainloop()
