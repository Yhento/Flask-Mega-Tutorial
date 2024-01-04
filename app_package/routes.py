from flask import render_template
from app_package import app
from app_package.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Tyler Payne'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            },
            {
                'author': {'username': 'Tyler'},
                'body': 'Learning a lot today!'
            },
            {
                'author': {'username': 'John Honnold'},
                'body': 'I am such a good boss!'
            }

    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
