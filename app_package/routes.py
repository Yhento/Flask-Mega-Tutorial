from flask import render_template
from app_package import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Tyler Payne'}
    return render_template('index.html', user=user)
    