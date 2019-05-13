import os
import secrets
from io import BytesIO
from PIL import Image
from flask import *
from EL import app, db, bcrypt
from flask_login import login_user, logout_user, current_user
from EL.forms import RegistrationForm, LoginForm
from EL.forms2 import StudentLoginForm, ContentForm, BookForm, VideoForm, SubjectForm
from EL.models import Student, Content, Books, Videos, Subject



# def save_images(photo):
#     hash_photo = secrets.token_urlsafe(10)
#     _, f_ext = os.path.splitext(photo.filename)
#     photo_name = hash_photo + file_extention
#     file_path = os.join(app.root_path, 'static/images', photo_name)
#     photo.save(file_path)
#     return photo_name




@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/super')
def super():
    info = Content.query.all()
    return render_template('Admindash.html', title='admin', info=info)




@app.route('/student_dashboard')
def student_dashboard():
    name = Student.query.all()
    book = Books.query.filter_by(Class=[current_user.Student_Class])
    video = Videos.query.filter_by(Class=[current_user.Student_Class])
    sub = Subject.query.filter_by(Class=[current_user.Student_Class])
            # book = Books.query.all()
    image = url_for('static', filename='profile_pics/'+current_user.Image_file)
    return render_template('student_dashboard.html', title='My Dashboard', name=name, book=book, image=image, video=video, sub=sub )


def save_picture(Image_file):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(Image_file.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125,125)
    i = Image.open(Image_file)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def save_book(Book):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(Book.filename)
    Book_fn = random_hex + f_ext
    Book_path = os.path.join(app.root_path, 'static/Book', Book_fn)
    Book.save(Book_path)

    return Book_fn


def save_video(Videos):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(Videos.filename)
    Videos_fn = random_hex + f_ext
    Videos_path = os.path.join(app.root_path, 'static/videos', Videos_fn)
    Videos.save(Videos_path)

    return Videos_fn

@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.Image_file.data)
       # m
       #  hashesd_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Student(id=form.Reg_NO.data,First_Name=form.First_Name.data, Last_Name=form.Last_Name.data, Student_Class=form.Student_Class.data,\
                    Gender=form.Gender.data, Date_of_birth=form.Date_of_birth.data,\
                    Image_file=picture_file, Status=form.Status.data)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created!', 'success')
        return redirect(url_for('index'))
    else:
        return render_template('signup.html', title='signup', form=form)

@app.route('/adminlogin', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin=form.username.data
        password=form.password.data

        password==password and admin==admin
        return redirect(url_for('super'))
    return render_template('adminlogin.html', title='login', form=form)



@app.route('/studentlogin', methods=['GET','POST'])
def studentlogin():
    if current_user.is_authenticated:
        return redirect(url_for('student_dashboard'))
    form = StudentLoginForm(request.form)
    if form.validate_on_submit(): 
        user = Student.query.filter_by(id=form.Reg_NO.data, Student_Class=form.Class.data, Status='active').first()
        if user:
            login_user(user)
            return redirect(url_for('student_dashboard'))
        else:
            flash('Wrong Reg_No or Class  if issues still continue contact your admin', 'danger',)
    return render_template('studentlogin.html', title='Student login', form=form)


@app.route('/suggestion', methods=['GET','POST'])
def suggestion():
    form = ContentForm()
    if form.validate_on_submit():
        content=Content(content=form.content.data)
        db.session.add(content)
        db.session.commit()
        flash('suggestion has been sent', 'success')
        return redirect(url_for('index'))
    return render_template('suggestion.html', title='suggestion', form=form)


@app.route('/subject', methods=['GET','POST'])
def subject():
    form = SubjectForm()
    if form.validate_on_submit():
        subject = Subject(Subject=form.Subject.data, Class=form.Class.data)
        db.session.add(subject)
        db.session.commit()
        flash('Subject has been post', 'success')
        return redirect(url_for('super'))
    return render_template('subject.html', title='post subject', form=form)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = BookForm()
    if form.validate_on_submit():
        Book_file = save_book(form.Book.data)
        book = Books(BookID=form.BookID.data, Book_Topic=form.Book_Topic.data, Class=form.Class.data, Book=Book_file, Subject=form.Subject.data)
        db.session.add(book)
        db.session.commit()
        flash('Book has been uploaded' , 'success')
        return redirect(url_for('super'))
    return render_template('upload.html', title='upload', form=form)




@app.route('/VideosUpload', methods=['GET', 'POST'])
def Videosupload():
    form = VideoForm()
    if form.validate_on_submit():
        Videos_file = save_video(form.Videos.data)
        video = Videos(VideosID=form.VideosID.data, Videos_Topic=form.Videos_Topic.data,Class=form.Class.data,Videos=Videos_file,  Subject=form.Subject.data)
        db.session.add(video)
        db.session.commit()
        flash('Video has been uploaded' , 'success')
        return redirect(url_for('super'))
    return render_template('VideosUpload.html', title='upload', form=form )



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.errorhandler(401)
def e401(e):
    return "It seems like you are not allowed to access this link."

@app.errorhandler(404)
def e404(e):
    return "The URL you were looking for does not seem to exist.<br><br>If you have typed the link manually, make sure you've spelled the link right."

@app.errorhandler(500)
def e500(e):
    return "Internal error. Contact the manager about this."

@app.errorhandler(403)
def e403(e):
    return "Forbidden access."

@app.errorhandler(410)
def e410(e):
    return "The content you were looking for has been deleted."

