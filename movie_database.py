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
    cur.execute("SELECT * FROM release_dates WHERE id=?", (release_id,))
    dates = cur.fetchall()
    cur.execute("SELECT * FROM languages WHERE id=?", (language_id,))
    lang = cur.fetchall()
    cur.execute("SELECT * FROM age_ratings WHERE id=?", (age_rating_id,))
    age_ratings = cur.fetchall()
    if age_ratings[0][0] == 1:
        age_rating = "non-adult movie"
    else:
        age_rating = "adult movie"
    cur.execute("SELECT * FROM vote_counts WHERE id=?", (vote_count_id,))
    votes = cur.fetchall()
    cur.execute("SELECT * FROM vote_averages WHERE id=?", (vote_average_id,))
    vote_average = cur.fetchall()
    conn.close()
    return render_template('movie_details.html', movie=movie, youtube=youtube, dates=dates, lang=lang,
                           age_rating=age_rating, votes=votes, vote_average=vote_average)


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
#    for movie in movies:    # to delete, not needed
#        release_ids.append(movies[0]['release_id'])     # to delete, not needed
    cur.execute("SELECT * FROM release_dates")
    dates = cur.fetchall()
    conn.close()
    return render_template('year.html', movies=movies, year=year, release_ids=release_ids, dates=dates)
# clean-up release_ids from code and return statement

@app.route('/years')
def years():
    pass


@app.route('/age_rating')
def age_rating(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)