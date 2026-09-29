import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# Part A: INNER JOIN
print("Customer orders:")

cur.execute("""
SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
""")

for row in cur.fetchall():
    print(row)


# Part B: Total spending per customer
print("\nTotal spending per customer:")

cur.execute("""
SELECT customers.name, SUM(orders.amount) AS total_spend
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id
ORDER BY total_spend DESC;
""")

for row in cur.fetchall():
    print(row)


# Part C: Cities with average order amount > 5000
print("\nCities with average order amount above 5000:")

cur.execute("""
SELECT customers.city, AVG(orders.amount) AS average_amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.city
HAVING AVG(orders.amount) > 5000;
""")

for row in cur.fetchall():
    print(row)

conn.close()