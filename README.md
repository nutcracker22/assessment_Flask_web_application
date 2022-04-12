# assessment_Flask_web_application

## Initial remarks

As the final assessment for the course Advanced Programming, I needed to create a database driven web application within 5 days, using Flask. This repository contains my solution. Furthermore, I had to submit a development report, which is shown below.

## Development report

My aim had been to develop and app about environmental data, preferably in the Aberdeen area. But I could not find any suitable datasource. The data I found had either too few items or came in a non-suitable data format. Thus, I had to switch to a more standard data set – a movie database. The original dataset can be found at: https://www.kaggle.com/hamzansariii/latest-popular-movies-dataset.

Since this data set contains more than 7000 rows, I thought of only including the movies between 2007 and 2022, in order to meet the outlined requirements of the assessment. I designed the database using a hand-drawn database diagram, which was the basis for the first draft of movie_db.py (the database creator file)

Initially I started developing the app with basically two python files, one for creating and filling the database. And the other one, that did all the data handling and contained all the routes for the html templates, which I had placed in a template folder.

For the creation of the database I implemented automatic error handling, since I did not want to manipulate the original dataset manually. However, this meant that some rows of the original dataset are not transferred into the database of the app. But the user will be notified about the skipped data.

After the main structure of the website was working, I added tests. However, PyCharm Community Edition, my chosen IDE, does only support behavior driven development, when the feature files are supplied from another IDE, which supports the Gherkin language. Henceforth, I obtained a student license for the Professional edition, which does support BDD and especially the creation of feature files. Then I created both the feature files and the steps files to run tests. As environment.py I used the file obtained from Bruce Scharlau’s https://github.com/scharlau/shopping_testing_p repository. However, since I am using Firefox as my browser of choice, I needed to adopt the environment.py accordingly, to run with geckodriver instead of the chromedriver. This needs to be considered when trying to reproduce my tests. But I guess that it will be enough to simply replace my environment.py with the one from the public repository.

After running the tests, both as fails and as passes, I started to include data comparison functionalities on my website.

The next step was to refactor the whole set of files according to the Tutorial in the official Flask documentation (see https://flask.palletsprojects.com/en/2.0.x/tutorial/). I used a similar structure for files and folders, but used different names. This made it possible to separate each route for each single webpage in separate files. This will make the maintenance of the app significantly easier, even if another programmer would join the team or replace me, since now there is one file movie.py paired with one file movie.html, who will handle all that is needed to show the page /movie.html. The same applies to the other pages. Only the index.html is still parsed from the __init__.py

Afterwards I was confident enough to push the first version of my application to Heroku, after following all the steps outlined in the Flask documentation and the Heroku documentation (https://devcenter.heroku.com/articles/python-gunicorn). However, the app did not run online. After inspecting the Heroku logs, I could narrow the arrow down to the Procfile or the __init__.py. Still, all attempts of me failed to get the app running. The error messages showed that gunicorn was unable to start the app. I tried renameing the create_app() function, I declared the app variable before the function, all without success. Also searching for the error messages online to get help, did not give the solution.
By accident I found the following GitHub page, were a user had encountered a similar problem. So basically my whole problem had been caused by a bug in gunicorn 20.0.0 and 20.1.0 (the version I was using):
https://github.com/benoitc/gunicorn/issues/2159
The work around provided (calling the create_app() function, assigning it to a variable and using this variable in the Procfile, instead of ‘app’), solved the issue. This whole process of debugging this issue took me about 5 hours.
Because of this delay, I could not implement some functionalities, as I had intended.

As shown in the git-log.txt file, I used git from the beginning on, almost exclusively working on the development branch of the repository, with usually two merges per day, usually after significant steps had been done or errors had been fixed. In order to remember functionalities I wanted to implement after finished the tasks I was working on, I started creating issues on GitHub and via git. In this way I found out that this is very easy to use and very helpful, since the issues can be closed by a message attached to a commit or merge command, even via the terminal of the IDE.
