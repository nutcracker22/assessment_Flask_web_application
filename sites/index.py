from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db

bp = Blueprint('index', __name__,)

@bp.route('/')
def index():
    cursor = connect_to_db()
    cursor.execute("select * from release_years")
    years = cursor.fetchall()
    return render_template('index.html', years=years)
