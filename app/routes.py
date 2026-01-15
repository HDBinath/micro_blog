from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route("/index")
def index():
    user = {'name': 'Binath'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Sri Lanka!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Flask is really cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods = ["GET" , "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template('login.html', title = "Sign In", form=form)
    
