"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, 
                    session, redirect)

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ View homepage. """

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def all_users():
    """View all users"""

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show profile page of a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user=user)
    #make new html file for single user profile page, render that page

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Account with this email already exists. Please try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')

@app.route('/log-in')
def log_in(email, password):
    """User log in."""

    user = crud.get_user_by_email(email)

    if user.password == password:
        session['user_id'] = user_id
        flash('Logged in!')

    return redirect('/')
    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)



#error: users not defined in line 8 of all_users.html