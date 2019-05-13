# from sqlalchemy import create_engine
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin







app = Flask(__name__)

app.config['SECRET_KEY'] = 'anyonemustnothere'
app.config['SECRET_KEY'] = '0d49f8f8066cd7e3a1274998b8a01e5f'

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:''@localhost:3306/flask'
app.config['FLASK_ADMIN_SWATCH'] = 'Darkly'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= 'False'

db = SQLAlchemy(app)
bcrypt =  Bcrypt(app)
login_manager = LoginManager(app)
admin = Admin(app,template_mode='bootstrap3')



# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_USER'] = ''
# app.config['MYSQL_DB'] = 'user'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#
# db = MySQLConnection(app)
#

# db.create_all()
# db.session.commit()


# Flask views


# # Create admin
# admin = flask_admin.Admin(
#     app,
#     'My Dashboard',
#     base_template='my_master.html',
#     template_mode='bootstrap3',
# )



from EL import routes

