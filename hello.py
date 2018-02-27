from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    posts = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'body': 'Python can do every thing. However, it is very easy'
        },
        {
            'title': {'main': 'I love C#', 'sub': 'this is a happy story'},
            'body': 'C# can do some things. However, it is very easy'
        },
        {
            'title': {'main': 'I hate C#', 'sub': 'this is a sad story'},
            'body': 'C# can do no things. However, it is very stupid!'
        }
    ]
    return render_template('index.html', user=user, posts = posts, title='A title')

@app.route('/store')
def store():
    items = [
        {
            'title': 'Python Book',
            'price': 200
        },
        {
            'title': 'Cook Book',
            'price': 25
        },
        {
            'title': 'iPhone X',
            'price': 1000
        }
    ]
    return render_template('store.html', items=items)

app.run()

