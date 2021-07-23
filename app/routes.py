from flask.templating import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Seb'}
    return render_template('index.html', user=user)

@app.route('/test')
def test():
    user = {'username': 'Seb'}
    return render_template('test.html', user=user)

@app.route('/test2')
def test2():
    user = {'username': 'Seb'}
    sample_data = [
        {
            'author': {'username': 'Seb'},
            'body': 'Hello!'
        },
        {
            'author': {'username': 'Seb'},
            'body': 'Welcome to Flask!'
        }
    ]
    return render_template('test2.html', user=user, sample_data=sample_data)