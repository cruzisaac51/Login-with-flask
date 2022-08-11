from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import re
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

#models 
from models.ModelUser import ModelUser


#entities
from models.entities.User import User


app=Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return render_template('auth/index.html')

@app.route('/index')
def landing_page():
    return render_template('auth/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0,request.form['username'],request.form['password'])
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("index"))
            else:
                flash('Invalid password')
                return render_template('auth/login.html')
        else:
            flash("user not found...")
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# @app.route('/signup', methods =['GET', 'POST']) 
# def register(): 
#     if request.method == 'POST': 
#         user = User(0,request.form['username'],request.form['password'], request.form['fullname'])
        
    #     registered_user = ModelUser.sign_up(db, user)
    #     if registered_user != " ":
    #         if registered_user.username:
    #             register(registered_user)
    #             return redirect(url_for("sign_up"))
    #     else:
    #         flash("user ocupated")
    #     return redirect(url_for("signup"))
    # else:
    #     return render_template("signup.html")

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1> esta es una vista protegida </h1>", 404

def status_401(error):
    return redirect(url_for("index"))

def status_404(error):
    return "<h1> pagina no encontrada</h1>"
    


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()