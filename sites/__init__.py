import os
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db
#from sites.test import create_app

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

    from . import index
    app.register_blueprint(index.bp)

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
