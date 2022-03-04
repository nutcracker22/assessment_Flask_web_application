from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db

bp = Blueprint('movie_details', __name__, url_prefix='/movie_details')

@bp.route('/movie_details/<id>')
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
