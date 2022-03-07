from flask import Flask, render_template, request, redirect, flash, session, url_for

from datetime import datetime, date
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField, RadioField, PasswordField, SelectMultipleField, \
    SelectField, widgets
from wtforms.fields.html5 import \
    DateField  # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, InputRequired
import sqlite3
import random
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ddksididkdkdl'

# connect to the database
con = sqlite3.connect("VideoProgram.db", check_same_thread=False)
con.row_factory = sqlite3.Row

# create a cursor/pointer to navigate the database
cur = con.cursor()


### Form models ####

class LoginForm(FlaskForm):
    ID = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class VideoForm(FlaskForm):
    Title = StringField('Title', validators=[DataRequired()])
    Description = TextAreaField('Description')
    URL = StringField('URL', validators=[DataRequired(), URL(message="Not a valid URL")])
    topics = MultiCheckboxField('Topics for this Video', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit URL')


########## routes ##########


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    if session['username']:
        if session['is_teacher']:
            sql = """
                select *
                from Videos
                where Available = '0';"""

            cur.execute(sql, )
            results = cur.fetchall()
            newApprovals = []
            for row in results:
                newApprovals.append((row['Title'], row['Description'], row['URL'], row['Submitter']))
            session['newApprovals'] = newApprovals
            # print('newApprovals', newApprovals)

            sql = """
                    select *
                    from Reports;"""

            cur.execute(sql,)
            result = cur.fetchall()
            my_Reports = []
            for row in result:
                my_Reports.append((row['UserID'], row['VideoID']))
            session['my_Reports'] = my_Reports
            # print('my_Reports', my_Reports)
            return render_template('index.html')
        else:
            un = session['username']
            sql = """
                    select Title, URL, TopicID, SubjectID
                    from Videos
                    where SubjectID in (
                        select SubjectID
                        from Class
                        where ClassID in (
                            select ClassID
                            from TimetabledClass
                            where StudentID = ?))
                    limit 5;"""

            cur.execute(sql, (un,))
            results = cur.fetchall()
            featuredVideos = []
            for row in results:
                featuredVideos.append((row['Title'], row['URL']))
            session['featuredVideos'] = featuredVideos
            # print('featuredVideos', session['featuredVideos'])

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            un = form.ID.data
            pw = form.password.data
            # print(un, pw)
            sql = """
                    select *
                    from Users
                    where ID = ?
                    and password = ?;"""

            cur.execute(sql, (un, pw))
            result = cur.fetchall()
            # print(result)
            if len(result) <= 1:
                flash("You are logged in")
                session['username'] = result[0][0]
                session['firstname'] = result[0][1]
                session['lastname'] = result[0][2]
                session['is_teacher'] = result[0][6]
                # print("User", session['username'])
                if session['is_teacher']:
                    session['teacher_code'] = True
                    print('session teacher', session['teacher_code'])
                return redirect(url_for('index'))
            else:
                flash("There is an error")
        else:
            flash("There is something missing!")

    return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    if session['username']:
        # clear out the session
        session['username'] = None
        session['firstname'] = None
        session['lastname'] = None
        session['is_teacher'] = None
        session['Teacher_Code'] = None
        session['subject'] = None

        flash("You have successfully logged out")
    else:
        flash("You must be logged in first")
    return redirect(url_for("index"))


@app.route('/subjects')
def subjects():
    if session['username']:
        un = session['username']
        print(un)
        sql = """
                select distinct SubjectID
                from Class
                where ClassID in (
                    select ClassID
                    from TimetabledClass
                    where StudentID = ?);"""

        cur.execute(sql, (un,))
        results = cur.fetchall()

        my_classes = []
        for row in results:
            # print(row['SubjectID'])
            my_classes.append(row['SubjectID'])
        session['subject'] = my_classes
        # print(my_classes)

        return render_template('subjects.html', title="Subject", results=results)
    else:
        flash('You must be logged in first')

    return render_template('index.html', title="Home")


@app.route('/topics', methods=['GET'])
def topics():
    # Find the topics of the user
    if request.args.get('subject'):
        # print(request.args.get('subject'))
        subject = request.args.get('subject')
        # print(subject, 'subject')
        sql = """
                select TopicID, TopicName
                from Topics
                where SubjectID = ?;"""

        cur.execute(sql, (subject,))
        results = cur.fetchall()
        # print('results', results)
        # print(results)
        my_topics = []
        my_topicID = []
        for row in results:
            my_topics.append(row['TopicName'])
        # print('my_topics', my_topics)
        session['Topics'] = my_topics
        for row in results:
            my_topicID.append(row['TopicID'])
        session['TopicID'] = my_topicID


        return render_template('topics.html', subject=subject, TopicID_Len=len(session['TopicID']))


@app.route('/Videos')
def Videos():
    if request.args.get('topic'):
        tn = request.args.get('topic')
        sql = """
                select TopicID
                from Topics
                where TopicName = ?"""

        cur.execute(sql, (tn,))
        result = cur.fetchone()
        # print(result)
        session['TopicID'] = str(result['TopicID'])
        # print('TopicID', session['TopicID'])
        sql = """
                select *
                from Videos
                where TopicID = ?;"""

        cur.execute(sql, (session['TopicID'],))
        results = cur.fetchall()

        # print('results', results)
        # print('length', len(results))
        session['amount_of_subjects'] = len(results)
        my_url = []
        my_VideoID = []
        my_VideoTitle = []
        for row in results:
            my_url.append((row['url'], row['Title'], row['VideoID']))
            my_VideoID.append(row['VideoID'])
        session['my_url'] = my_url
        print(my_VideoID)

        return render_template('Videos.html', my_VideoID=my_VideoID)


@app.route('/submitVideo', methods=['GET', 'POST'])
def submit_newVideo():
    if session['username']:
        form = VideoForm()
        my_topics = []
        sql = """
            select TopicID, TopicName, s.SubjectID
            from Topics t, Subjects s, TimetabledClass a, Users u, Class c 
            where t.SubjectID = s.SubjectID
            and s.SubjectID = c.SubjectID
            and c.ClassID = a.ClassID
            and a.StudentID = u.ID
            and u.ID = ?
            order by s.SubjectID asc, TopicID asc;"""

        cur.execute(sql, (session['username'],))
        results = cur.fetchall()
        for row in results:
            my_topics.append((row['TopicID'], row['SubjectID'] + '-' + row['TopicName']))
        form.topics.choices = my_topics
        if request.method == 'POST':
            if form .validate_on_submit():
                title = form.Title.data
                description = form.Description.data
                url = form.URL.data
                video_topics = []
                for v in form.topics.data:
                    video_topics.append(int(v))

                sql = """
                        insert
                        into Videos(TopicID, Description, Title, URL, submitter)
                        values(?, ?, ?, ?, ?);"""

                cur.execute(sql, (video_topics[0], description, title, url, session['username']), )
                con.commit()
                if con.commit():
                    flash("Your video submission will be reviewed")
        # return render_template('submitVideo.html', form=form)
        return render_template("submitVideo.html", form=form)
    else:
        flash('You must be logged in first')

    return render_template('index.html', title="Home")


@app.route('/report')
def report():
    print("Reports")
    if request.args.get('report'):
        Broken_VideoID = request.args.get('report')
        print(report)
        sql = """
                insert
                into Reports(UserID, VideoID)
                values(?, ?)
                """

        cur.execute(sql, (session['username'], Broken_VideoID,))
        con.commit()

        # make video unavailable

    return redirect(url_for("index"))

@app.route("/approval")
def approval():
    if session['is_teacher']:
        if request.args.get('approve'):
            approval = request.args.get('url')
            print('approval', approval)

            # Update availability to true
            sql = """
                    UPDATE Videos
                    SET Available = '1'
                    where url = ?"""

            cur.execute(sql, (approval,))
            con.commit()

            return redirect(url_for("index"))

        if request.args.get('denial'):
            denial = request.args.get('url')
            print('denial', denial)

            # Delete the video
            sql = """                  
                    DELETE 
                    FROM Videos
                    where url = ?"""

            cur.execute(sql, (denial,))
            con.commit()

            return redirect(url_for("index"))
    return redirect(url_for("index"))

@app.route("/brokenLinks")
def brokenLinks():
    if session['is_teacher']:
        if request.args.get('remove'):
            # print(request.args.get('remove'))
            faulty = request.args.get('remove')
            print(faulty)

            sql = """
                    DELETE
                    FROM Videos
                    where VideoID = ?"""

            cur.execute(sql, (faulty,))
            con.commit()

            sql = """
                    delete
                    from Reports
                    where VideoID = ?"""

            cur.execute(sql, (faulty,))
            con.commit()

        return redirect(url_for("index"))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host, port, debug=True)
