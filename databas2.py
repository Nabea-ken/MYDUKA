import psycopg2

conn = psycopg2.connect(host='localhost', port='5433', user='postgres', password='postgres', dbname='myduka_db')
cur = conn.cursor()

# -------------------------
# GET PRODUCTS
# -------------------------
def get_products():
    cur.execute("SELECT * FROM products")
    return cur.fetchall()

products = get_products()
print("PRODUCTS:", products)


# -------------------------
# INSERT PRODUCTS (FIXED)
# -------------------------
def insert_products(name, buying_price, selling_price):
    sql = "INSERT INTO products(name, buying_price, selling_price) VALUES (%s, %s, %s)"
    cur.execute(sql, (name, buying_price, selling_price))
    conn.commit()

# insert sample products
insert_products("iphone", 100000, 120000)
insert_products("hp", 50000, 60000)


# -------------------------
# INSERT SALES (CORRECT)
# -------------------------
def insert_sales(pid, quantity):
    sql = "INSERT INTO sales (pid, quantity) VALUES (%s, %s)"
    cur.execute(sql, (pid, quantity))
    conn.commit()
    print("Sale inserted successfully!")


# Insert sample sales
insert_sales(1, 2)   # product id 1 → iphone
insert_sales(2, 1)   # product id 2 → hp


# -------------------------
# GET SALES (FIXED)
# -------------------------
def get_sales(pid=None):
    if pid:
        sql = "SELECT * FROM sales WHERE pid = %s"
        cur.execute(sql, (pid,))
    else:
        cur.execute("SELECT * FROM sales")

    rows = cur.fetchall()

    print("\nSALES DATA:")
    for row in rows:
        print(row)


# Display sales
get_sales()
