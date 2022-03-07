from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Yourmum'

#########################################################################
# HTTP Routes
#########################################################################
students = [
    "23456, John Smith, 8, Mitre",
    "23465, Sally Jones, 11, Scudo",
    "32453, Aidan McKenzie, 9, Taja",
    "43263, Mary Philp, 10, Gladius",
    "31234, Xan Xi, 12, Boek"
]


@app.route('/')
def home():
    onlyNames = []
    for line in students:
        values = line.split(", ")
        onlyNames.append([values[1], values[0]])

    pageTitle = 'List of Students'
    return render_template('students.html', title=pageTitle, names=onlyNames)


@app.route('/student_details')
def student_details():
    if not request.args.get('studentid'):
        flash("Select a student from the list")
        return redirect(url_for('home'))
    else:
        studentid = request.args.get('studentid')
        found_student = []
        for line in students:
            values = line.split(", ")
            if values[0] == studentid:
                found_student = values
        return render_template('student_details.html', student=found_student)


#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)