import sqlite3

db = sqlite3.connect("products.db")
cursor = db.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS products (name TEXT, category TEXT,"
    " size TEXT, price TEXT, article TEXT, photo TEXT)"
)
db.commit()