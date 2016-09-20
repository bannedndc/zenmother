#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import requests
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    posts = []
    upcoming_shows =\
      requests.get("http://api.songkick.com/api/3.0/artists/8823199/calendar.json?apikey=zdpZeMNcromcrzB4&order=desc")
    past_shows =\
      requests.get("http://api.songkick.com/api/3.0/artists/8823199/gigography.json?apikey=zdpZeMNcromcrzB4&order=desc")
    return render_template('home.html',
               posts=posts,
			   upcoming_shows=upcoming_shows.json(),
			   past_shows=past_shows.json())

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
