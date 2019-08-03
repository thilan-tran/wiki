# Flask
***

## Basics and Routing
***
```py
from flask import Flask
app = Flask(__name__) # name of the module

@app.route("/") # multiple routes
@app.route("/home")
def home():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about():
    return "<h1>About page.</h1>"

@app.route("/posts/<postid>")     # variables routes
@app.route("/posts/<int:postid>") # converters: int, float, string, path
def posts(postid):
    return "Post " + postid

if __name__ == '__main__': # run in python directly
    app.run(debug=True)
```
- export the env variable `FLASK_APP=webpage.py`
  - hotsave flask app with env variable `FLASK_DEBUG=1`
  - run with `flask run`

## Requests and Responses
***

Using query strings:
```py
from flask import request

@app.route('/hello')
def hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'
```
- GET request to '/hello?name=Tony' returs 'Hello Tony'

Request data and headers:
```py
from flask import json

@app.route('/messages', methods=['POST'])
def message():
    if request.headers['Content-Type'] == 'text/plain':
        return 'Text Message: ' + request.data
    elif request.headers['Content-Type'] == 'application/json':
        # alternatively, request.is_json and request.get_json()
        return 'JSON Message: '+ json.dumps(request.json)
    else:
        return '415 Unsupported Media Type'
```
Handling responses:
```py
from flask import Responses

@app.route('/hello', methods=['GET'])
def hello():
    data = {
        'content' : '...',
        'id' : 5
    }
    js = json.dumps(data)

    # mimetype is content-type
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = '...'

    return resp

from flask import jsonify, make_response # alternative json parsing and response
...
if request.is_json:
    req = request.get_json()
    res_body = {
        'message': 'JSON received',
        'sender': req.get('name')
    }
    res = make_response(jsonify(res_body), 200)
...
```

## Templating
***
```py
from flask import Flask, render_template, url_for

posts = [
    {
        'author': ...,
        'title': ...,
        'content': ...,
        'date': ...,
    }
]

@app.route("/")
def home():
    return render_template('home.html', title='Home', posts=posts) # templates/home.html
```
Using Jinja2 templating engine in html:
```py
{% if title %} # if statement
  <title>{{ title }}</title>
{% else %}
  ...
{% endif %}

{% for post in posts %} # for loop
  <h1>{{ post.title }}</h1>
  <p>By {{ post.author }} on {{ post.date }}</p>
{% endfor %}

{% extends "layout.html" %} # inheritance
{% block content %}
  ...
{% endblock content %}

{% with messages = get_flashed_messages(with_categories=true) %} # grabbing flashed messages
{% for category, message in messages %}
  ...
{% endfor %}

...href="{{ url_for('static', filename='main.css') }}" # static files, static/main.css
```
## Forms
***

forms.py:
```py
from flask_wtf import FlaskForm # wt forms flask plugin
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign Up')
```
Using forms in app:
```py
from forms import RegistrationForm

app.config['SECRET_KEY'] = '...'

@app.route("/register", methods='GET', 'POST') # allowing for POST requests
    form = RegistrationForm()
    if form.validate_on_submit():
        # flask flash alert, second arg is custom category
        flash(f'Account created for {form.username.data}', 'success')
        # redirect to url of a route function
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
```
## Databases
***

- using SQLAlchemy
  - uses object-relational mapping, object-oriented paradigm
  - in cli:
    - `db.createAll()`
    - `db.session.add(some_user)`
    - `db.session.commit()`
    - `db.drop_all()`
    - can query all, first, filter by search, get by id
```py
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # relative path
db = SQLAlchemy(app)

class User(db.Model): # database models are classes
    # instance of class is a table with columns

    # primary key asigned automatically
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # User makes Posts, backref is another column in the posts, specify lazy loading
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    ...
    # table and columns are lowercase
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```
