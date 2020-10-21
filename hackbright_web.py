"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get("github")

    first, last, github = hackbright.get_student_by_github(github)

    projects = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           projects=projects)

    return html


@app.route("/student-add", methods=['GET', 'POST'])
def student_add():
    """Add a student."""

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        github = request.form.get('github')
        
        hackbright.make_new_student(fname,lname, github)

        return render_template('student_added.html', github = github)

    return render_template('student_add.html')


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
