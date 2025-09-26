from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp

SPECIALTY_CHOICES = [
    ('КН','КН'),('СИ','СИ'),('И','И'),('ИС','ИС'),
    ('М','М'),('ПМ','ПМ'),('МИ','МИ'),('С','С'),
    ('АД','АД')
]
COURSE_CHOICES = [(str(i), str(i)) for i in range(1,5)]
GROUP_MAP = {
  'КН': [(str(i),str(i)) for i in range(1,9)],
  'СИ': [(str(i),str(i)) for i in range(1,7)],
  'И':  [(str(i),str(i)) for i in range(1,7)],
  'ИС': [(str(i),str(i)) for i in range(1,5)],
  'М':  [('1','1')],
  'ПМ': [('1','1'),('2','2')],
  'МИ': [('1','1')],
  'С':  [('1','1')],
  'АД': [('1','1'),('2','2')],
}

class StudentForm(FlaskForm):
    faculty_number = StringField(
        'Факултетен номер',
        validators=[
            DataRequired(message='Полето “Факултетен номер” е задължително.'),
            Regexp(r'^\d{5}$',
                   message='Факултетният номер може да съдържа само цифри.'),
            Length(min=5,
                   max=5, 
                   message='Факултетният номер трябва да е точно %(max)d символа.')
        ]
    )
    first_name = StringField(
        'Име',
        validators=[
            DataRequired(message='Полето “Име” е задължително.'),
            Length(min=2, max=100, message='Името трябва да е между %(min)d и %(max)d символа.'),
            Regexp(
                r'^[A-Za-zА-Яа-я\- ]+$',
                message='Името може да съдържа само букви, интервали и тирета.'
            )
        ]
    )
    last_name = StringField(
        'Фамилия',
        validators=[
            DataRequired(message='Полето “Фамилия” е задължително.'),
            Length(min=2, max=100, message='Фамилията трябва да е между %(min)d и %(max)d символа.'),
            Regexp(
                r'^[A-Za-zА-Яа-я\- ]+$',
                message='Името може да съдържа само букви, интервали и тирета.'
            )
        ]
    )
    specialty = SelectField(
        'Специалност',
        choices=SPECIALTY_CHOICES,
        validators=[DataRequired(message='Избери специалност')]
    )
    course = SelectField(
        'Курс',
        choices=COURSE_CHOICES,
        validators=[DataRequired(message='Избери курс')]
    )
    group = SelectField(
        'Група',
        choices=[],
        validators=[DataRequired(message='Избери група')]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Полето “Email” е задължително.'),
            Email(message='Моля, въведете валиден имейл адрес.'),
            Regexp(
                r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
            ),
            Length(max=120, message='Имейлът трябва да е не повече от %(max)d символа.')
        ]
    )
    address = StringField(
        'Адрес',
        validators=[
            DataRequired(message='Полето “Адрес” е задължително.'),
            Regexp(
                r'^[A-Za-z0-9А-Яа-я\-.," ]+$',
                message='Адресът може да съдържа само букви, цифри, интервали, тирета и запетаи.'
            ),
            Length(max=255, message='Адресът трябва да е не повече от %(max)d символа.')
        ]
    )
    city = StringField(
        'Град',
        validators=[
            DataRequired(message='Полето “Град” е задължително.'),
            Regexp(
                r'^[A-Za-zА-Яа-я\- ]+$',
                message='Градът може да съдържа само букви, интервали и тирета.'
            ),
            Length(max=100, message='Градът трябва да е не повече от %(max)d символа.')
        ]
    )
    state = StringField(
        'Област',
        validators=[
            DataRequired(message='Полето “Област” е задължително.'),
            Regexp(
                r'^[A-Za-zА-Яа-я\- ]+$',
                message='Областа може да съдържа само букви, интервали и тирета.'
            ),
            Length(max=100, message='Областта трябва да е не повече от %(max)d символа.')
        ]
    )
    phone = StringField(
        'Телефон',
        validators=[
            DataRequired(message='Полето “Телефон” е задължително.'),
            Regexp(
                r'^[0-9\+ ]+$',
                message='Телефонът може да съдържа само цифри.'
            ),
            Length(min=5, max=20, message='Телефонът трябва да е между %(min)d и %(max)d символа.')
        ]
    )
    submit = SubmitField('Запази')
