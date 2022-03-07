from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)


#########################################################################
# HTTP Routes
#########################################################################
@app.route('/')
def home():
    if request.args:
        # return request.args
        if request.args.get('lang') != 'en':
            return 'sorry english only'
        else:
            return 'This is in english'
    else:
        return 'This is the home page route'


@app.route('/about')
def index():
    return 'You have found the about page route'


@app.route('/contact')
def contacts():
    if request.args.get("source") == "facebook":
        return 'Message me'
    else:
        return 'Email Me'
    # return 'This is the contact page'


@app.route('/menu')
@app.route('/menus')
def menu():
    return 'Here are our menus'


#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)
