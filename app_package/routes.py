from app_package import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Tyler Payne'}
    return '''
    <html>
        <head>
        <title> Home Page - Microblog </title>
        </head>
        <body>
            <h1> Hello, ''' + user['username'] + '''!</h1>
        </body>
    
    
    </html>'''