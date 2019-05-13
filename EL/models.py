from EL import db, login_manager, admin, bcrypt
from datetime import datetime
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from wtforms.widgets import TextArea
from wtforms import TextAreaField
import os
import secrets






@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))




class Student(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(50),nullable=False)
    Last_Name = db.Column(db.String(50), nullable=False)
    Student_Class = db.Column(db.String(20),unique=False, nullable=False)
    Status = db.Column(db.String(20), nullable=False)
    Gender = db.Column(db.String(3))
    Date_of_birth = db.Column(db.DATE)
    Image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
    # student = db.relationship('StudentClass', backref='student')


    def __repr__(self):
        return f"Student('{self.First_Name}','{self.Image_file}', '{self.Date_of_birth}')"

class SetView(ModelView):
    from_colums = ['id', 'First_Name', 'Last_Name', 'StudentClass', 'Gender', 'Date_of_birth', 'Image_file', 'Department']
       



class Books(db.Model):
    BookID = db.Column(db.Integer, primary_key=True)
    Book_Topic = db.Column(db.String(150), nullable=False)
    Class= db.Column(db.String(10), nullable=False)
    Subject = db.Column(db.String(30), nullable=True)
    Book_Author = db.Column(db.String(100), nullable=True)
    Book = db.Column(db.String(60), nullable=False, default='default.pdf')

    def __repr__(self):
        return f"Books('{self.Book_Topic}'), '{self.Book}, '{self.Book_Author}')"

    def __unicode__(self):
        return self.name


class Videos(db.Model):
    VideosID = db.Column(db.Integer, primary_key=True)
    Videos_Topic = db.Column(db.String(150), nullable=False)
    Class= db.Column(db.String(10), nullable=False)
    Subject= db.Column(db.String(100), nullable=False)
    Videos = db.Column(db.String(60), nullable=False, default='default.mp4')

    def __repr__(self):
        return f"Books('{self.Videos}'), '{self.Videos_Topic}')"



class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Subject = db.Column(db.String(100), nullable=False)
    Class = db.Column(db.String(10), nullable=False)
    def __repr__(self):
        return f"Subject('{self.Subject}')"


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    content = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"Content('{self.content}')"



admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(Books, db.session))
admin.add_view(ModelView(Videos, db.session))
admin.add_view(ModelView(Subject, db.session))






