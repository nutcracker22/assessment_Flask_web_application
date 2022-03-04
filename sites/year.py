from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db

bp = Blueprint('year', __name__, url_prefix='/year')

@bp.route('/year/<id>')
def year(id):
    cursor = connect_to_db()
    # get results from years
    cursor.execute("SELECT * FROM release_years WHERE id=?", (id,))
    year = cursor.fetchall()
    cursor.execute("SELECT * FROM movies WHERE release_year_id=?", (id,))
    movies = cursor.fetchall()
    cursor.execute("SELECT * FROM release_dates")
    dates = cursor.fetchall()
    return render_template('year.html', movies=movies, year=year, dates=dates)
