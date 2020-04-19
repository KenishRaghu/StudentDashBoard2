from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/college.db'
db = SQLAlchemy(app)


class StudentMarks(db.Model):
    usn = db.Column(db.String(10), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), primary_key=True, nullable=False)
    cie1 = db.Column(db.Integer, nullable=False, default=0)
    cie2 = db.Column(db.Integer, nullable=False, default=0)
    cie3 = db.Column(db.Integer, nullable=False, default=0)
    lab1 = db.Column(db.Integer, nullable=False, default=0)
    lab2 = db.Column(db.Integer, nullable=False, default=0)
    aat = db.Column(db.Integer, nullable=False, default=0)
    quiz1 = db.Column(db.Integer, nullable=False, default=0)
    quiz2 = db.Column(db.Integer, nullable=False, default=0)
    see = db.Column(db.Integer, nullable=False, default=0)

    # def __repr__(self):
    #     return 'Student ' + str(self.usn)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/teacher')
def teacher():
    return render_template("teacher.html")


@app.route('/student')
def student():
    return render_template("student.html")


@app.route('/enter_marks', methods=['GET', 'POST'])
def enter_marks():
    if request.method == 'POST':
        post_usn = request.form['usn'].upper()
        post_name = request.form['name'].title()
        post_subject = request.form['subject'].upper()
        post_cie1 = request.form['cie1'] if request.form['cie1'] else 0
        post_cie2 = request.form['cie2'] if request.form['cie2'] else 0
        post_cie3 = request.form['cie3'] if request.form['cie3'] else 0
        post_lab1 = request.form['lab1'] if request.form['lab1'] else 0
        post_lab2 = request.form['lab2'] if request.form['lab2'] else 0
        post_aat = request.form['aat'] if request.form['aat'] else 0
        post_quiz1 = request.form['quiz1'] if request.form['quiz1'] else 0
        post_quiz2 = request.form['quiz2'] if request.form['quiz2'] else 0
        post_see = request.form['see'] if request.form['see'] else 0
        new_marks = StudentMarks(usn=post_usn, name=post_name, subject=post_subject, cie1=post_cie1,  cie2=post_cie2, cie3=post_cie3,
                                 lab1=post_lab1, lab2=post_lab2, aat=post_aat, quiz1=post_quiz1, quiz2=post_quiz2, see=post_see)
        db.session.add(new_marks)
        db.session.commit()
        # flash("Successfully added marks to the db.")
        return redirect('/enter_marks')
    else:
        all_posts = StudentMarks.query.order_by(StudentMarks.usn).all()
        return render_template('enter_marks.html', posts=all_posts)


@app.route('/enter_marks/edit_marks/<string:usn>/<string:subject>', methods=['GET', 'POST'])
def edit_marks(usn, subject):
    student_marks = StudentMarks.query.get_or_404((usn, subject))
    if request.method == 'POST':
        student_marks.usn = request.form['usn']
        student_marks.name = request.form['name']
        student_marks.subject = request.form['subject']
        student_marks.cie1 = request.form['cie1']
        student_marks.cie2 = request.form['cie2']
        student_marks.cie3 = request.form['cie3']
        student_marks.lab1 = request.form['lab1']
        student_marks.lab2 = request.form['lab2']
        student_marks.aat = request.form['aat']
        student_marks.quiz1 = request.form['quiz1']
        student_marks.quiz2 = request.form['quiz2']
        student_marks.see = request.form['see']
        db.session.commit()
        return redirect('/enter_marks')
    else:
        return render_template('edit_marks.html', student=student_marks)


@app.route('/enter_marks/delete_marks/<string:usn>/<string:subject>')
def delete_marks(usn, subject):
    student_marks = StudentMarks.query.get_or_404((usn, subject))
    db.session.delete(student_marks)
    db.session.commit()
    return redirect('/enter_marks')


@app.route('/check_marks', methods=['GET', 'POST'])
def check_marks():
    if request.method == 'POST':
        post_usn = request.form['usn'].upper()
        post_subject = request.form['subject'].upper()
        post_student_marks = StudentMarks.query.get_or_404((post_usn, post_subject))
        return render_template('check_marks.html', student_marks=post_student_marks)
    else:
        return render_template('check_marks.html')


if __name__ == "__main__":
    app.run(debug=True)
