import sqlite3
from flask import Flask, render_template, g, request

app = Flask(__name__)

DB_NAME = 'movies-data.db'

app.config.from_object(__name__)


def connect_to_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return cur


# this function was obtained from https://github.com/mjhea0/flaskr-tdd
def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_to_db()
    return g.sqlite_db


# this function was obtained from https://github.com/mjhea0/flaskr-tdd
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


@app.route('/', methods=["GET", "POST"])
def index():
    cursor = connect_to_db()
    ### add later - search function
    # get user input
    # if request.method == "POST":
    #     search = request.form['search_for']
    #     if search == "movie":
    #         name = request.form["movie_name"]
    #         cursor.execute("SELECT * FROM movies WHERE name=?", (name,))
    #         movies1 = cursor.fetchall()
    #         movies(movies1)
    #     else:
    #         name = int(request.form["movie_name"])
    #         if name < 2007:
    #             pass
    #             # print (not in database) on html
    #         elif name > 2022:
    #             pass
    #             #print (sorry, that is in the future) on html
    #         else:
    #             cursor.execute("SELECT * FROM release_years WHERE release_year=?", (name,))
    #             years1 = cursor.fetchall()
    #             years1_id = years1[0][0]
    #             year(years1_id)
    # get results from years
    cursor.execute("select * from release_years")
    years = cursor.fetchall()
    return render_template('index.html', years=years)


@app.route('/movies')
def movies():
    cursor = connect_to_db()
    # get results from movies
    cursor.execute("select * from movies")
    rows = cursor.fetchall()
    return render_template('movies.html', rows=rows)


@app.route('/movie_details/<id>')
def movie_details(id):
    cursor = connect_to_db()
    # get results from movies
    cursor.execute("SELECT * FROM movies WHERE id=?", (id,))
    movie = cursor.fetchall()
    movie_name = movie[0][1]
    movie_name_split = movie_name.split(" ")
    youtube = "https://www.youtube.com/results?search_query="
    for i in range(0, len(movie_name_split)):
        youtube += movie_name_split[i] + "+"
    youtube += "Trailer"
    release_id = movie[0][4]
    language_id = movie[0][5]
    age_rating_id = movie[0][6]
    vote_count_id = movie[0][7]
    vote_average_id = movie[0][8]
    cursor.execute("SELECT * FROM release_dates WHERE id=?", (release_id,))
    dates = cursor.fetchall()
    cursor.execute("SELECT * FROM languages WHERE id=?", (language_id,))
    lang = cursor.fetchall()
    cursor.execute("SELECT * FROM age_ratings WHERE id=?", (age_rating_id,))
    age_ratings = cursor.fetchall()
    if age_ratings[0][0] == 1:
        age_rating = "non-adult movie"
    else:
        age_rating = "adult movie"
    cursor.execute("SELECT * FROM vote_counts WHERE id=?", (vote_count_id,))
    votes = cursor.fetchall()
    cursor.execute("SELECT * FROM vote_averages WHERE id=?", (vote_average_id,))
    vote_average = cursor.fetchall()
#    conn.close()
    return render_template('movie_details.html', movie=movie, youtube=youtube, dates=dates, lang=lang,
                           age_rating=age_rating, votes=votes, vote_average=vote_average)


@app.route('/statistics')
def statistics():
    cursor = connect_to_db()
    # get results from movies ### movies per year
    cursor.execute("select * from release_years")
    years = cursor.fetchall()
    years_id = []
    list_amount = []
    sum = 0
    for year in years:
        years_id.append(year[0])
        cursor.execute("SELECT * FROM movies WHERE release_year_id=?", (year[0],))
        movies_per_year = cursor.fetchall()
        amount = len(movies_per_year)
        list_amount.append(amount)
        sum += amount
    average_movies = sum / len(years_id)
    return render_template('statistics.html', average=average_movies, column1=years_id, column2=list_amount, rows=len(years_id), years=years)


@app.route('/year/<id>')
def year(id):
    cursor = connect_to_db()
    # get results from years
    cursor.execute("SELECT * FROM release_years WHERE id=?", (id,))
    year = cursor.fetchall()
    cursor.execute("SELECT * FROM movies WHERE release_year_id=?", (id,))
    movies = cursor.fetchall()
#    release_ids = []
#    for movie in movies:    # to delete, not needed
#        release_ids.append(movies[0]['release_id'])     # to delete, not needed
    cursor.execute("SELECT * FROM release_dates")
    dates = cursor.fetchall()
#    conn.close()
    return render_template('year.html', movies=movies, year=year, dates=dates)
# clean-up release_ids from code and return statement


#@app.route('/years')
#def years():
#    pass


#@app.route('/age_rating')
#def age_rating(id):
#    pass


if __name__ == '__main__':
    app.run(debug=True)