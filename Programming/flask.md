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
- GET request to '/hello?name=Tony' returns 'Hello Tony'

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
```py
#forms.py

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

    # validating username for uniqueness
    def validate_username(self, username):
        # querying our database by the user model
        user = User.query.filter_by(username=username.data)
        if user:
          raise ValidationError('That username is taken. Please choose another.')
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
Uploading files in forms:
```py
from flask_wtf.file import FileField, FileAllowed

class UpdateAccountForm(FlaskForm):
    username = ...
    email = ...
    picture = FileField('Update Profile Picture', validators=[FileAllowed('jpg', 'png')])
    ...
```
## Databases
***

- using SQLAlchemy:
  - uses object-relational mapping, object-oriented paradigm
  - in cli:
    - `db.createAll()`
    - `db.session.add(some_user)`
    - `db.session.commit()`
    - `db.drop_all()`
    - can query all, first, filter by search, get by id
      - eg. `User.query.filter_by(username='Bob')` to query all user database models by username
      - eg. `Post.query.first()` to query first post database model
```py
#__init__.py

from flask_sqlalchemy import SQLAlchemy

#set up local sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// indicates relative path
db = SQLAlchemy(app)

#models.py

from flaskapp import db

class User(db.Model): # database models are classes
    # instance of class is a table with columns

    # primary key asigned automatically
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # User makes Posts (posts is an attribute in each user), backref is an attribute in posts,
    # specify lazy loading
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    ...
    # table and columns are lowercase
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```
- encrypting passwords:
  - `from flask_bcrypt import Bcrypt`
  - `bcrypt.generate_password_hash('passwd').decode('utf-8')`
  - `bcrypt.check_password_hash(hashed, 'passwd')`

Implementing authentication logic on registration page:
```py
@app.route("/register", methods='GET', 'POST') # allowing for POST requests
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
```
- implementing a login system using flask_login:
```py
#models.py

from flaskapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    ...

#routes.py

from flask_login import login_user, logout_user, current_user

@app.route("/login", methods=['GET', 'POST'])
def login():
    # if user already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') # next page in url query
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccesfful.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
```
## CRUD Example
***
```py
#routes.py

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created.', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form)

@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route("/post/<int:post_id>") # route variables
def post(post_id):
    post = Post.query.get_or_404(post_id) # 404 missing error
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403) # 403 forbidden error
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.title.content
        db.session.commit()
        flash('Your post has been updated.', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form)

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.', 'success')
    return redirect(url_for('home'))
```
## Package Structure
***

- common importing errors:
  - running script will overwrite its `__name__` as `__name__`
  - cyclic import dependencies
- turn the entire application into a package using an `__init__.py` file
```py
#run.py
from flaskapp import app

if __name__ == '__main__':
    app.run(debug=True)

#__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#set up flask app and related extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// indicates relative path
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # default login page
login_manager.login_message_category = 'info'

from flaskblog import routes # still avoiding circular import issues

#the parent folder of this file is now a package
#other modules inside package can import app from flaskapp
#other modules inside package can import from other modules from flasblog.modulename
```
## Pagination
***

- *paginate* data to load chunks of data at a time
- `posts = Post.query.paginate()`
  - `posts.per_page` defaults to 20
    - `Post.query.paginate(per_page=5)` specifies page limit
  - `posts.page` defaults at 1
    - `Post.query.paginate(page=2)` gives desired page
  - `for post in posts.items` to iterate through them
  - `posts.total` gives total number of posts
  - `posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2)`
    - divides up page numbers
    - None values can be shown with ellipses
```py
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)         # setting a query parameters
    posts = Post.query.order_by(post.date_posted.desc()) # ordering by latest posts
                .paginate(page=page, per_page=5)         # rather than querying all posts
    return render_template('home.html', posts=posts)

@app.route("/user/<string:username>") # only showing specific user's posts
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
                .order_by(post.date_posted.desc())\
                .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)
```
## Email and Password Reset
***

- creating a time sensitive token:
  - `from itsdangerous import TimedJSONWebSignatureSerializer as Serializer`
  - `s = Serializer('secret', 30)` with secret key, expires after 30 seconds
  - `token = s.dumps({'user_id': 1}).decode('utf-8')`
  - `s.loads(token)` gives back desired payload
  - after time limit, attempting to load token gives a TimeExpired error
```py
#models.py

class User(db.model, UserMixin):
    ...
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod # no need to access class or instance attributes
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    ...

#forms.py

class RequestResetForm(FlaskForm):
    email = ...
    submit = ...

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email.')

class ResetPasswordForm(FlaskForm):
    password = ...
    comfirm_password = ...
    submit = ...

#routes.py

def send_reset_email(user): # from flask_mail import Mail, Message
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = 'To reset your password, visit the following link: {}'
               .format(url_for('reset_token', token=token, _external=True))
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect (url_for('home'))
    user = User.verify_reset_token(token)
    if not user:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated.')
        return redirect(url_for('login'))
    return render_template('rest_token.html', title="Reset Password", form=form)
```
## Application Configuration
***

### Flask Blueprints
***

Use flask blueprints to split app into modular packages:
```py
#main/
#main/__init__.py
#main/routes.py

from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/home")
...

#posts/
#posts/__init__.py
#posts/routes.py

from flask import (Blueprint, render_template, url_for, flash,
                   redirect, request, abort)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new")
...

#posts/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    ...
...

#users/
#users/__init__.py
#users/routes.py

from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (...)
from flaskblog.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/register")
...
@users.route("/login")
...

#users/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flasblog.models import User

class RegistrationForm(FlaskForm):
    ...
...

#users/utils.py

import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import app, mail

def save_picture ...
def send_reset_email ...

#must also update all url_for('link') calls as url_for('blueprint.link') !
```
### Registering Blueprints
***
```py
#config.py

import os

class Config:
    SECRET_KEY = ...
    SQLALCHEMY_DATABASE_URI = ...
    MAIL_SERVER = ...
    MAIL_PORT = ...
    ...

#__init__.py

from flasblog.config import Config

#initializing extensions here
db = SQLAlchemy() # instead of SQLAlchemy(app)
...

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # passing in app to extensions
    db.init_app(app)
    ...

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app

#must also update all imports / references to app:
#from flask import current_app

#run.py
from flasblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```
