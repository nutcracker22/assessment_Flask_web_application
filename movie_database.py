import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# database details - to remove some duplication
db_name = 'movies-data.db'

@app.route('/')
def index():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from years
    cur.execute("select * from release_years")
    years = cur.fetchall()
    return render_template('index.html', years=years)


@app.route('/movies')
def movies():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from movies
    cur.execute("select * from movies")
    rows = cur.fetchall()
    conn.close()
    return render_template('movies.html', rows=rows)


@app.route('/movies_details')
def movie_details():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from movies
    cur.execute("select * from movies")
    rows = cur.fetchall()
    conn.close()
    return render_template('movies.html', rows=rows)


@app.route('/years')
def years():
    pass


@app.route('/age_rating')
def age_rating():
    pass




# @app.route('/customers')
# def customers():
#     conn = sqlite3.connect(db_name)
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     # get results from customers
#     cur.execute("select * from customers")
#     rows = cur.fetchall()
#     conn.close()
#     return render_template('customers.html', rows=rows)
#
# @app.route('/customer_details/<id>')
# def customer_details(id):
#     conn = sqlite3.connect(db_name)
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     # get results from customers
#     cur.execute("select * from customers WHERE id=?", (id,))
#     customer = cur.fetchall()
#     conn.close()
#     return render_template('customer_details.html', customer=customer)
#
# @app.route('/orders')
# def orders():
#     conn = sqlite3.connect(db_name)
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     # get results from orders
#     cur.execute("select * from orders")
#     rows = cur.fetchall()
#     conn.close()
#     return render_template('orders.html', rows=rows)
#
# @app.route('/order_details/<id>')
# def order_details(id):
#     conn = sqlite3.connect(db_name)
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     # get results from orders
#     cur.execute("select * from orders WHERE id=?", (id,))
#     order = cur.fetchall()
#     customer_id = order[0]['customer_id']
#     print(customer_id)
#     # get results from line_items
#     cur.execute("select * from line_items WHERE order_id=?", (id,))
#     items = cur.fetchall()
#     product_id = items[0]['product_id']
#     # get results from customers
#     cur.execute("select * from customers WHERE id=?", (customer_id,))
#     customer = cur.fetchall()
#     #get results from products
#     cur.execute("select * from products")
#     product_table = cur.fetchall()
#     conn.close()
#     return render_template('order_details.html', order=order, items=items, customer=customer, product_table=product_table)

if __name__ == '__main__':
    app.run(debug=True)