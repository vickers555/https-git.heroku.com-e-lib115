from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import*
from datetime import datetime
from wtforms.fields.html5 import *




class StudentLoginForm(FlaskForm):
    Reg_NO = StringField('Reg.No/Admission No', validators=[DataRequired()])
    Class = SelectField('Student_Class',choices=[('','select class'),('js1','Jss1'),('js2','Jss2'), ('js3', 'Jss3'), ('ss1', 'SSS1'), ('ss2', 'SSS2'), ('ss3', 'SSS3') ])
    submit = SubmitField('Login')


class ContentForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired(),])
    submit = SubmitField('send')

class SubjectForm(FlaskForm):
    Subject = StringField('Subject', validators=[DataRequired()])
    Class = SelectField('Student_Class', choices=[('','select class'),('js1','Jss1'),('js2','Jss2'), ('js3', 'Jss3'), ('ss1', 'SSS1'), ('ss2', 'SSS2'), ('ss3', 'SSS3') ])
    submit = SubmitField('post')


class BookForm(FlaskForm):
    BookID = StringField('BookID', validators=[DataRequired()])
    Book_Topic = StringField('Book_Topic', validators=[DataRequired()])
    Book_Author = StringField('Book_Author', validators=[DataRequired()])
    Subject = StringField('Subject', validators=[DataRequired()])
    Class = SelectField('Student_Class', choices=[('','select class'),('js1','Jss1'),('js2','Jss2'), ('js3', 'Jss3'), ('ss1', 'SSS1'), ('ss2', 'SSS2'), ('ss3', 'SSS3') ])
    Book = FileField('Upload Book', validators=[FileAllowed(['pdf'])])
    submit = SubmitField('upload')

class VideoForm(FlaskForm):
    VideosID = StringField('BookID', validators=[DataRequired()])
    Videos_Topic = StringField('Book_Topic', validators=[DataRequired()])
    Class = SelectField('Student_Class', choices=[('','select class'),('js1','Jss1'),('js2','Jss2'), ('js3', 'Jss3'), ('ss1', 'SSS1'), ('ss2', 'SSS2'), ('ss3', 'SSS3') ])
    Videos = FileField('Upload Video', validators=[DataRequired()])
    Subject = StringField('Subject', validators=[DataRequired()])
    submit = SubmitField('upload')
