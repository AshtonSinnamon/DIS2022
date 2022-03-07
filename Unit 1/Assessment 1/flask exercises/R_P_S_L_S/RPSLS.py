from flask import Flask, render_template, request, redirect, url_for, session, flash
import random  # needed for random number generation

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myverysecretkey'  # used so session cookies can be encrypted


def checkWinner(player_choice, computer_choice):
    x = (5 + int(player_choice) - int(computer_choice)) % 5
    print("x", x)
    if x == 1 or x == 3:
        print("User won")
        result = True
        return result
    elif x == 2 or x == 4:
        print("Computer won")
        result = False
        return result
    else:
        print("draw")


def number_to_name(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Paper"
    elif number == 2:
        return "Scissors"
    elif number == 3:
        return "Spock"
    elif number == 4:
        return "Lizard"


@app.route("/")
def home():
    return render_template('Home.html')


@app.route("/game")
def index():
    if request.args.get('pc'):
        session['gameon'] = True
        pc = request.args.get('pc')
        cc = random.randint(0, 5)
        session['pc'] = number_to_name(int(pc))
        session['cc'] = number_to_name(int(cc))
        print(session['pc'])
        print(session['cc'])
        print('playerscore', session['player_score'], 'computer score', session['computer_score'])

        result = (checkWinner(pc, cc))
        print('result', result)
        if result is True:
            # player_score += 1
            session['player_score'] += 1
            flash("You won this round")
        elif result is False:
            # computer_score += 1
            session['computer_score'] += 1
            flash("You lost this round")
        else:
            flash("Draw")
        print(session['player_score'], session['computer_score'])

        if session['player_score'] == 3:
            session['gameon'] = False
            flash('You won!')
        if session['computer_score'] == 3:
            session['gameon'] = False
            flash('You lost :(')
    else:
        session['computer_score'] = 0
        session['player_score'] = 0
        session['pc'] = ''
        session['cc'] = ''
        session['gameon'] = True

    return render_template('RPSLS.html')


# ps - player score, pc - player choice
# cs - computer score, cc - computer choice

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)
