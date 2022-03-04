import os
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db

app = Flask(__name__)

def create_app(test_config=None): #code mainly from Flask Documentation/Tutorial
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'movies-data.db'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        cursor = connect_to_db()
        cursor.execute("select * from release_years")
        years = cursor.fetchall()
        return render_template('index.html', years=years)

    from . import database
    database.init_app(app)

    from . import movies
    app.register_blueprint(movies.bp)

    from . import movie_details
    app.register_blueprint(movie_details.bp)

    from . import year
    app.register_blueprint(year.bp)

    from . import statistics
    app.register_blueprint(statistics.bp)

    return app