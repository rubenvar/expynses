import tkinter as tk
import tkinter.simpledialog as simpledialog
import sqlite3


def show_categories_window(main_window):
    def save_category():
        # get data
        name = name_entry.get()

        # db connect
        conn = sqlite3.connect("expynses.db")
        cursor = conn.cursor()

        # save to db
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))

        # close
        conn.commit()
        conn.close()

        # empty input
        name_entry.delete(0, tk.END)

        # update list
        refresh_category_list()
        # cats_window.destroy()

    def refresh_category_list():
        # empty current listbox
        category_listbox.delete(0, tk.END)

        # db connect
        conn = sqlite3.connect("expynses.db")
        cursor = conn.cursor()

        # get categories
        cursor.execute("SELECT id, name FROM categories")
        categories = cursor.fetchall()

        # add data from db into widget
        for category in categories:
            # get data
            category_id = category[0]
            category_name = category[1]

            # create frame
            frame = tk.Frame(category_listbox)
            frame.pack(fill=tk.X)

            # show name
            label = tk.Label(frame, text=category_name, width=30)
            label.pack(side=tk.LEFT)

            def change_category_name(category_id):
                new_name = simpledialog.askstring(
                    "Change Category Name", "Enter the new name"
                )
                if new_name:
                    cursor.execute(
                        "UPDATE categories SET name = ? WHERE id = ?",
                        (new_name, category_id),
                    )
                    conn.commit()
                    refresh_category_list()

            button = tk.Button(
                frame,
                text="Change name",
                command=lambda id=category_id: change_category_name(id),
            )
            button.pack(side=tk.RIGHT)

    # new window
    categories_window = tk.Toplevel(main_window)
    categories_window.title("Input Category")

    # name label + input
    name_label = tk.Label(categories_window, text="Name")
    name_label.pack()
    name_entry = tk.Entry(categories_window)
    name_entry.pack()

    # save button
    button_save = tk.Button(categories_window, text="Save", command=save_category)
    button_save.pack()

    # create categories list widget
    category_listbox = tk.Listbox(categories_window, width=50)
    category_listbox.pack()

    # update list
    refresh_category_list()

    # start
    categories_window.mainloop()
