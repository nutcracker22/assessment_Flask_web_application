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


@app.route('/movie_details/<id>')
def movie_details(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from movies
    cur.execute("SELECT * FROM movies WHERE id=?", (id,))
    movie = cur.fetchall()
    print(movie)
    movie_name = movie[0][1]
    movie_name_split = movie_name.split(" ")
    youtube = "https://www.youtube.com/results?search_query="
    for i in range(0, len(movie_name_split) - 1):
        youtube += movie_name_split[i] + "+"
    youtube += "Trailer"
    print(youtube)
#    youtube = "https://www.youtube.com/results?search_query=" + movie_name_split[0] + "+" + movie_name_split[1] + "+" + "Trailer"
    conn.close()
    return render_template('movie_details.html', movie=movie, youtube=youtube)


@app.route('/year/<id>')
def year(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from years
    cur.execute("SELECT * FROM release_years WHERE id=?", (id,))
    year = cur.fetchall()
    cur.execute("SELECT * FROM movies WHERE release_year_id=?", (id,))
    movies = cur.fetchall()
    release_ids = []
    for movie in movies:
        release_ids.append(movies[0]['release_id'])
    cur.execute("SELECT * FROM release_dates")
    dates = cur.fetchall()
    conn.close()
    return render_template('year.html', movies=movies, year=year, release_ids=release_ids, dates=dates)


@app.route('/years')
def years():
    pass


@app.route('/age_rating')
def age_rating(id):
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