from flask import render_template, request
from flask_bcrypt import check_password_hash
from flask_login import login_required, login_user
from werkzeug.utils import redirect

from OurApp import app#, csrf
from OurApp.forms import LoginForm
from OurApp.models import Users, Categories, Subscriptions

user = Users.query.all()


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", title="Home", info="Ma page d'accueil dynamique")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/webstart", methods=['POST', 'GET'])
# @csrf.exempt
def Webstart():
    form = LoginForm()
    user = Users.query.filter_by(email=form.login_name.data).first()

    if user is not None:
        if user.is_admin == 1 and check_password_hash(user.password, form.password.data):
            login_user(user)
            return render_template("login.html")
    return render_template("webstart.html",  title="Webstart", info="Page de presentation de Webstart", form=form)


@app.route("/usersList")
@login_required
def usersList():
    users = Users.query.all()
    return render_template("usersList.html", title="usersList", info="Page de la liste des utilisateurs", users=users)


@app.route("/categories")
@login_required
def categories():
    categories = Categories.query.all()
    return render_template("categories.html", title="categories", info="Page de la liste des categories", categories=categories)

@app.route("/login")
@login_required
def login():
    return render_template("login.html")


@app.route("/submit", methods=['POST'])
def submit():
    categories = Categories.query.all()
    users = Users.query.all()
    users_mail = {}

    for category in categories:
        if request.form.get(category.name) is not None:
            subscriptions = Subscriptions.query.filter_by(category_id=category.id).all()
            for subscription in subscriptions:
                print(subscription)
                user = Users.query.filter_by(id=user.id)
                users_mail[subscription.user_id] = user.email
                print(user)

        print(category.name, request.form.get(category.name))
    return render_template("login.html")

def send_mail(email, content):
    pass
