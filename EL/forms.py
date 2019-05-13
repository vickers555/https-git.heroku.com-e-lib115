from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import*
from wtforms.fields.html5 import *
from EL.models import Student


class RegistrationForm(FlaskForm):
    First_Name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20), ])
    Last_Name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20), ])
    Student_Class = SelectField('Student_Class', choices=[('','select class'),('js1','Jss1'),('js2','Jss2'), ('js3', 'Jss3'), ('ss1', 'SSS1'), ('ss2', 'SSS2'), ('ss3', 'SSS3') ])
    Date_of_birth = DateField('Date of Birth', format='%Y-%m-%d')
    Reg_NO = StringField('Reg_NO', validators=[DataRequired()])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Status = StringField('Status', validators=[DataRequired()])
    Image_file= FileField('Upload profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Sign up')

    # def validate_Reg_No(self, Reg_No):
    #     user = Student.query.filter_by(Reg_No=Reg_No.data).first()
    #     if True:
    #         raise validationError('Reg_No has been created in the database')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='invalid username')])
    password = PasswordField('password', validators=[DataRequired(message='wrong password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField ('Login')

