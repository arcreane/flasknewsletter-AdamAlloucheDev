from flask import Flask
# from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '436ab96a7efdc88c90f2c81e5a5bba9e'
# app.config['SQLALCHEMY_DATABASE_URI'] = '''mysql://arcreane_ws:&a1éz2"e3'r4@mysql-arcreane.alwaysdata.net/arcreane_flask'''
# app.config['SQLALCHEMY_DATABASE_URI'] = '''mysql://dv20allouche:0g01fa%N@vm589.haisoft.net:8443/dv20allouche'''
# app.config['SQLALCHEMY_DATABASE_URI'] = '''mysql://root:root@localhost:3306/blog'''
app.config['SQLALCHEMY_DATABASE_URI'] = '''mysql://arcreane_ws:&a1éz2"e3'r4@mysql-arcreane.alwaysdata.net/arcreane_dv20allouche'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'webstart'
login_manager.login_message_category = "Bienvenue au login de l'application"

# csrf = CSRFProtect(app)

from OurApp import routes