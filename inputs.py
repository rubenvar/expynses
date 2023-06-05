import tkinter as tk
import sqlite3


def show_inputs_window(main_window):
    def save_expense():
        # get data
        title = title_entry.get()
        cents = int(cents_entry.get())
        desc = desc_entry.get()
        category_id = category_entry.get()

        # db connect
        conn = sqlite3.connect("expynses.db")
        cursor = conn.cursor()

        # save to db
        cursor.execute(
            """
            INSERT INTO expenses (title, cents, desc, category_id)
            VALUES (?, ?, ?, ?)""",
            (title, cents, desc, category_id),
        )
        conn.commit()
        conn.close()

        # close
        inputs_window.destroy()

    inputs_window = tk.Toplevel(main_window)
    inputs_window.title("Input expenses")

    # title label + input
    title_label = tk.Label(inputs_window, text="Title")
    title_label.pack()
    title_entry = tk.Entry(inputs_window)
    title_entry.pack()

    # cents label + input
    cents_label = tk.Label(inputs_window, text="Cents")
    cents_label.pack()
    cents_entry = tk.Entry(inputs_window)
    cents_entry.pack()

    # desc label + input
    desc_label = tk.Label(inputs_window, text="Description")
    desc_label.pack()
    desc_entry = tk.Entry(inputs_window)
    desc_entry.pack()

    # category label + input
    category_label = tk.Label(inputs_window, text="Category ID")
    category_label.pack()
    category_entry = tk.Entry(inputs_window)
    category_entry.pack()

    # save button
    button_save = tk.Button(inputs_window, text="Save", command=save_expense)
    button_save.pack()

    inputs_window.mainloop()
