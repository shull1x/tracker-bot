import sqlite3
from config import DB_NAME

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, category TEXT)")

def add_expense(user_id, amount, category):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO expenses (user_id, amount, category) VALUES (?, ?, ?)", (user_id, amount, category))

def get_expenses(user_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT SUM(amount) FROM expenses WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()[0]
        return result if result else 0
