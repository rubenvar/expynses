import tkinter as tk

from db import create_database
from inputs import show_inputs_window
from totals import show_totals_window
from categories import show_categories_window


def show_inputs():
    show_inputs_window(window)


def show_categories():
    show_categories_window(window)


def show_totals():
    show_totals_window(window)


# execute function to create db
create_database()

# Create the main window
window = tk.Tk()
window.title("Expense Tracker App")
window.geometry("500x300")

# nav buttons
button_inputs = tk.Button(
    window,
    text="Inputs",
    command=show_inputs,
    relief=tk.FLAT,
    cursor="hand2",
    fg="blue",
)
button_inputs.pack(pady=10)

button_categories = tk.Button(
    window,
    text="Categories",
    command=show_categories,
    relief=tk.FLAT,
    cursor="hand2",
    fg="blue",
)
button_categories.pack(pady=10)

button_totals = tk.Button(
    window,
    text="Totals",
    command=show_totals,
    relief=tk.FLAT,
    cursor="hand2",
    fg="blue",
)
button_totals.pack(pady=10)


window.mainloop()
