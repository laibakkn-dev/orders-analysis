import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# Customers table
cur.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

# Orders table
cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER
)
""")

customers = [
    (1, "Ali", "Lahore"),
    (2, "Sara", "Karachi"),
    (3, "Ahmed", "Lahore"),
    (4, "Ayesha", "Islamabad"),
    (5, "Hamza", "Karachi"),
    (6, "Fatima", "Islamabad")
]

orders = [
    (101, 1, 6000),
    (102, 1, 3500),
    (103, 2, 8000),
    (104, 2, 4500),
    (105, 3, 7000),
    (106, 3, 3000),
    (107, 4, 9000),
    (108, 5, 5500),
    (109, 5, 6500),
    (110, 6, 4000)
]

cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)
cur.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders)

conn.commit()
conn.close()

print("Orders database created successfully.")