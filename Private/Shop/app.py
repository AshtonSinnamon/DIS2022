from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, widgets, SelectField, \
    HiddenField, RadioField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, URL, Optional, ValidationError, Length, Email, EqualTo
import random
import sqlite3
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "myverysecretkey"

con = sqlite3.connect("", check_same_thread=False)
con.row_factory = sqlite3.Row

cur = con.cursor()


class SignUpForm(FlaskForm):
    pass


class LoginForm(FlaskForm):
    pass


@app.route("/")
def index():
    pass


@app.route("/login")
def login():
    pass


@app.route("/user_home")
def index():
    pass


@app.route("/shop")
def shop():
    pass

    @app.route("/category_1")
    def category_1():
        pass

    @app.route("/category_2")
    def category_2():
        pass


@app.route("/wishlist")
def index():
    pass


@app.route("/cart")
def index():
    pass


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)