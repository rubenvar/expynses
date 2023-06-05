import sqlite3


def create_database():
    # db connect
    conn = sqlite3.connect("expynses.db")
    cursor = conn.cursor()

    # create table "expenses"
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            cents INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            desc TEXT,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )"""
    )

    # create table "categories"
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )"""
    )

    # save, close
    conn.commit()
    conn.close()
