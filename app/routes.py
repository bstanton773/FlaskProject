from app import app2
from app.forms import LoginForm
from flask import render_template, redirect, flash

from app.models import Post

@app2.route('/')
@app2.route('/index')
def index():
    user = {'username': 'Brian'}
    posts = Post.query.all()
    return render_template('index.html', user=user, posts = posts, title='A title')

@app2.route('/store')
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
    return render_template('store.html', items=items, title='A title 2')

@app2.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)