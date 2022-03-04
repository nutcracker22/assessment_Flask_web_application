from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db

bp = Blueprint('movies', __name__)

@bp.route('/movies')
def movies():
    cursor = connect_to_db()
    # get results from movies
    cursor.execute("select * from movies")
    rows = cursor.fetchall()
    return render_template('movies.html', rows=rows)
