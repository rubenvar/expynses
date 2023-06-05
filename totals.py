import tkinter as tk
import sqlite3


def show_totals_window(main_window):
    # db connect
    conn = sqlite3.connect("expynses.db")
    cursor = conn.cursor()

    # get data from db
    cursor.execute(
        """SELECT expenses.id, expenses.title, expenses.cents, expenses.created_at, expenses.desc, categories.name
        FROM expenses LEFT JOIN categories ON expenses.category_id = categories.id"""
    )
    expenses = cursor.fetchall()

    # close
    cursor.close()
    conn.close()

    # create window
    totals_window = tk.Toplevel(main_window)
    totals_window.title("Totals")

    # create widget
    listbox = tk.Listbox(totals_window, width=100)

    # add data from db into widget
    for expense in expenses:
        expense_text = f"ID: {expense[0]}\nTitle: {expense[1]}\nCents: {expense[2]}\nCreated At: {expense[3]}\nDesc: {expense[4]}\nCategory: {expense[5]}"
        lines = expense_text.split("\n")
        for line in lines:
            listbox.insert(tk.END, line)
        listbox.insert(tk.END, "-" * 50)

    listbox.pack()

    totals_window.mainloop()
