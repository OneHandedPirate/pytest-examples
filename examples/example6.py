import sqlite3


def save_user(name: str, age: int) -> None:
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if type(age) is not int:
        raise TypeError("Age must be an integer")

    conn = sqlite3.connect("example6.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (name text, age integer)")

    cursor.execute("INSERT INTO users VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
