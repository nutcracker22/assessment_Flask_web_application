from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db

bp = Blueprint('statistics', __name__, url_prefix='/statistics')

@bp.route('/statistics')
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


