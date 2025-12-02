import psycopg2

conn = psycopg2.connect(host='localhost',port='5433',user='postgres',password='postgres',dbname='myduka_db')

cur = conn.cursor()

""" cur.execute("select * from products")
products = cur.fetchall()
# print(products) """

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)


""" cur.execute("insert into products(name,buying_price,selling_price)values('samsung',15000,20000)")
conn.commit()
print(products) """

def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

product1 = ('iphone',100000,120000)
product2 = ('hp',50000,60000)
insert_products(product1)
insert_products(product2)

#2  with tasks

def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()

sales1=(0,20)
sales2=(1,25)
insert_sales(sales1)
insert_sales(sales2)

def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales = get_sales()
print(sales)

#secure from sql injection
def insert_sales_2(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",(values))
    conn.commit

sale1 = (9,20)
insert_sales(sale1)






