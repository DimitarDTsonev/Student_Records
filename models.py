from extesnsions import db

class Student(db.Model):
    __tablename__ = 'students'
    id             = db.Column(db.Integer,  primary_key=True)
    faculty_number = db.Column(db.String(20), unique=True, nullable=False)
    first_name     = db.Column(db.String(100), nullable=False)
    last_name      = db.Column(db.String(100), nullable=False)
    specialty      = db.Column(db.String(100), nullable=False)
    course         = db.Column(db.Integer, nullable=False)
    group          = db.Column(db.String(20), nullable=False)
    email          = db.Column(db.String(120), unique=True, nullable=False)
    address        = db.Column(db.String(255), nullable=False)
    city           = db.Column(db.String(100), nullable=False)
    state          = db.Column(db.String(100), nullable=False)
    phone          = db.Column(db.String(20), nullable=False)
