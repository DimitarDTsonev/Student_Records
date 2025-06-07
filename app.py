import os
from sqlite3 import IntegrityError
from flask import Flask, render_template, redirect, url_for, flash, request # type: ignore
from dotenv import load_dotenv # type: ignore
from sqlalchemy import asc, desc # type: ignore
from forms import StudentForm, SPECIALTY_CHOICES, GROUP_MAP

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-default-secret')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from extensions import db

from models import Student
from forms import StudentForm

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentForm()
    selected_spec = form.specialty.data or SPECIALTY_CHOICES[0][0]
    form.group.choices = GROUP_MAP.get(selected_spec, [])

    if form.validate_on_submit():
        if Student.query.filter_by(faculty_number=form.faculty_number.data).first():
            flash('Този факултетен номер вече е зает от друг студент.', 'warning')
        elif Student.query.filter_by(email=form.email.data).first():
            flash('Този имейл вече е зает от друг студент.', 'warning')
        else:
            new_student = Student(
                faculty_number=form.faculty_number.data,
                first_name    = form.first_name.data,
                last_name     = form.last_name.data,
                specialty     = form.specialty.data,
                course        = int(form.course.data),
                group         = form.group.data,
                email         = form.email.data,
                address       = form.address.data,
                city          = form.city.data,
                state         = form.state.data,
                phone         = form.phone.data
            )
            db.session.add(new_student)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash('Възникна грешка при запис. Моля, провери данните.', 'danger')
            else:
                flash('Студентът беше успешно добавен.', 'success')
                return redirect(url_for('index'))

        # --- филтри + сортиране ---
    flt_spec   = request.args.get('specialty')
    flt_course = request.args.get('course')
    flt_group  = request.args.get('group')

    sort  = request.args.get('sort',  'faculty_number')
    order = request.args.get('order', 'asc')

    q = Student.query
    if flt_spec:
        q = q.filter_by(specialty=flt_spec)
    if flt_course:
        q = q.filter_by(course=int(flt_course))
    if flt_group:
        q = q.filter_by(group=flt_group)

    sort_attr = getattr(Student, sort, Student.faculty_number)
    q = q.order_by(desc(sort_attr) if order == 'desc' else asc(sort_attr))

    students = q.all()   # без limit

    specialties = [s[0] for s in db.session.query(Student.specialty).distinct()]
    courses     = sorted({s.course for s in Student.query.with_entities(Student.course)})
    groups      = sorted({s.group  for s in Student.query.with_entities(Student.group)})

    return render_template(
        'index.html',
        form=form,
        students=students,
        GROUP_MAP=GROUP_MAP,
        specialties=specialties,
        courses=courses,
        groups=groups,
        request_args=request.args
    )


@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit(student_id):
    student = Student.query.get_or_404(student_id)
    form    = StudentForm(obj=student)

    selected_spec = form.specialty.data or student.specialty
    form.group.choices = GROUP_MAP.get(selected_spec, [])

    if form.validate_on_submit():
        if form.faculty_number.data != student.faculty_number and \
           Student.query.filter_by(faculty_number=form.faculty_number.data).first():
            flash('Този факултетен номер вече е зает от друг студент.', 'warning')
        elif form.email.data != student.email and \
             Student.query.filter_by(email=form.email.data).first():
            flash('Този имейл вече е зает от друг студент.', 'warning')
        else:
            student.faculty_number = form.faculty_number.data
            student.first_name     = form.first_name.data
            student.last_name      = form.last_name.data
            student.specialty      = form.specialty.data
            student.course         = int(form.course.data)
            student.group          = form.group.data
            student.email          = form.email.data
            student.address        = form.address.data
            student.city           = form.city.data
            student.state          = form.state.data
            student.phone          = form.phone.data
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash('Възникна грешка при обновяване. Моля, провери данните.', 'danger')
            else:
                flash('Данните на студента бяха обновени.', 'success')
                return redirect(url_for('index'))

    return render_template(
        'edit.html',
        form=form,
        student=student,
        GROUP_MAP=GROUP_MAP
    )

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash('Студентът беше изтрит.', 'info')
    return redirect(url_for('index'))

@app.route('/students', methods=['GET'])
def students():
    all_students = Student.query.order_by(Student.id).all()
    return render_template('students.html',
                           students=all_students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
