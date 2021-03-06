import sqlite3
import csv


def initiate_tables():
    # drop the tables - use this order due to foreign keys - so that we can rerun the file as needed without repeating values
    conn.execute('DROP TABLE IF EXISTS movies')
    conn.execute('DROP TABLE IF EXISTS release_years')
    conn.execute('DROP TABLE IF EXISTS release_dates')
    conn.execute('DROP TABLE IF EXISTS languages')
    conn.execute('DROP TABLE IF EXISTS age_ratings')
    conn.execute('DROP TABLE IF EXISTS vote_counts')
    conn.execute('DROP TABLE IF EXISTS vote_averages')

    # create the tables again - create them in reverse order of deleting due to foreign keys
    conn.execute('CREATE TABLE movies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, overview TEXT, '
                 'release_year_id INTEGER, release_id INTEGER, language_id INTEGER, age_rating_id INTEGER,'
                 'vote_count_id INTEGER, vote_average_id INTEGER, '
                 'FOREIGN KEY(release_id) REFERENCES release_date(id), FOREIGN KEY(language_id) REFERENCES language(id)'
                 'FOREIGN KEY(age_rating_id) REFERENCES age_rating(id), FOREIGN KEY(vote_count_id) REFERENCES vote_count(id),'
                 'FOREIGN KEY(vote_average_id) REFERENCES vote_average(id) )')
    conn.execute('CREATE TABLE release_years ( id INTEGER PRIMARY KEY AUTOINCREMENT, release_year INTEGER UNIQUE )')
    conn.execute('CREATE TABLE release_dates ( id INTEGER PRIMARY KEY AUTOINCREMENT, release_date TEXT UNIQUE )')
    conn.execute('CREATE TABLE languages (id INTEGER PRIMARY KEY AUTOINCREMENT, language TEXT UNIQUE )')
    conn.execute('CREATE TABLE age_ratings ( id INTEGER PRIMARY KEY AUTOINCREMENT, age_rating TEXT UNIQUE )')
    conn.execute('CREATE TABLE vote_counts ( id INTEGER PRIMARY KEY AUTOINCREMENT, vote_count INTEGER UNIQUE)')
    conn.execute('CREATE TABLE vote_averages ( id INTEGER PRIMARY KEY AUTOINCREMENT, vote_average REAL UNIQUE )')
    print("Tables created successfully.")


def open_csv():
    with open('latest_popular_movies_dataset.csv', newline='') as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        assign_values(reader)
        return(file)


def close_csv(f):
    f.close()
    print("CSV-File closed successfully.")


def assign_values(content):
    i = 0
    print("Parsing data to database...")
    for row in content:
        year = row[2].split("-", 1)[0]
        try:
            year = int(year)
            if isinstance(year, int) and int(year) >= 2007:
                #                print(str(i + 2), row)
                movie_name = row[1]
                movie_overview = row[3]
                try:
                    release_date = row[2]
                except ValueError:
                    release_date = "not known"
                try:
                    if len(row[4]) <= 3 and row[4] != "":
                        original_language = row[4]
                    else:
                        original_language = "not known"
                except ValueError:
                    original_language = "not known"
                try:
                    vote_count = int(row[5])
                except ValueError:
                    vote_count = "not known"
                try:
                    if float(row[6]) <= 10:
                        vote_average = float(row[6])
                    else:
                        vote_average = "not known"
                except ValueError:
                    vote_average = "not known"
                try:
                    adult = bool(row[7])
                except ValueError:
                    adult = "not known"

                try:
                    cur.execute('INSERT INTO release_years VALUES(NULL,?)', (year,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    pass

                try:
                    cur.execute('INSERT INTO release_dates VALUES(NULL,?)', (release_date,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    pass
                try:
                    cur.execute('INSERT INTO languages VALUES(NULL,?)', (original_language,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    pass
                try:
                    cur.execute('INSERT INTO age_ratings VALUES(NULL,?)', (adult,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    pass
                try:
                    cur.execute('INSERT INTO vote_counts VALUES(NULL,?)', (vote_count,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    pass
                try:
                    cur.execute('INSERT INTO vote_averages VALUES(NULL,?)', (vote_average,))
                    conn.commit()
                except sqlite3.IntegrityError:
                    pass

                cur.execute('SELECT * FROM release_years WHERE release_year=?', (year,))
                release_year_ids = cur.fetchall()
                release_year_id = release_year_ids[0][0]

                cur.execute('SELECT * FROM release_dates WHERE release_date=?', (release_date,))
                release_ids = cur.fetchall()
                release_id = release_ids[0][0]

                cur.execute('SELECT * FROM languages WHERE language=?', (original_language,))
                language_ids = cur.fetchall()
                language_id = language_ids[0][0]

                cur.execute('SELECT * FROM age_ratings WHERE age_rating=?', (adult,))
                age_ratings = cur.fetchall()
                age_rating_id = age_ratings[0][0]

                cur.execute('SELECT * FROM vote_counts WHERE vote_count=?', (vote_count,))
                vote_count_ids = cur.fetchall()
                vote_count_id = vote_count_ids[0][0]

                cur.execute('SELECT * FROM vote_averages WHERE vote_average=?', (vote_average,))
                vote_averages = cur.fetchall()
                # print(release_ids)
                vote_average_id = vote_averages[0][0]

                cur.execute('INSERT INTO movies VALUES(NULL,?,?,?,?,?,?,?,?)',
                            (movie_name, movie_overview, release_year_id,
                             release_id, language_id, age_rating_id,
                             vote_count_id, vote_average_id))
                conn.commit()
                i += 1
        except ValueError:
            print("Error in original data, skipping: ", row[0], year)
    print("Data parsed successfully.")


conn = sqlite3.connect('movies-data.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

initiate_tables()
csv_file = open_csv()
close_csv(csv_file)