"""
Create and run a python server.
Present some simple pages and a form.
Display the content of the form on a page
Also has the Flask Browser Debugger."""

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, sample

app = Flask(__name__)  # creating an instance of the Flask Class

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

# 1 - Home page
@app.route('/')
def home():
    return render_template('home.html')

# 2 - Greet form
@app.route('/greetform')
def greetform():
    return render_template('greet_form.html')

# 3 - greet page
@app.route('/greet')
def greet():
    displayname = request.args['displayname']
    if displayname == "":
        displayname = "User"
    compliments = request.args.get('compliments', False)
    list_o_compliments = ['awesome', 'a hard worker', 'supersmart', 'Tenacious', 'very popular', 'a winner', 'super fun']
    ran_compliments = sample(list_o_compliments, 3)
    return render_template('greet.html', displayname=displayname, compliments=compliments, ran_compliments=ran_compliments)

# 4 - lucky number page
@app.route('/lucky')
def lucky_number():
    num = randint(1,20)
    return render_template('lucky.html', lucky_num=num)

# 5 - Comment form
@app.route('/form')
def show_form():
    return render_template('form.html')

# 6 - Comment page
@app.route('/comment')
def show_comment():
    username = request.args.get('username', 'User')
    comment = request.args.get('comment', 'No comment')
    return render_template('comment.html', username=username, comment=comment)
