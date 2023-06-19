from flask import Blueprint,jsonify,request,render_template,redirect,url_for,flash
from application import db
from application.models.user import User
from application import login_manager
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth',__name__,static_folder='static')

@auth.route('/login',methods=['GET','POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('main.Home'))
    


    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            login_user(user,True)
            flash("Logged in successfully")
            return redirect(url_for('main.Home'))
        else:
            flash("Invalid email or password")
            return redirect(url_for('auth.Login'))
        
    return render_template('auth/login.html',page_name="Login")
    




@auth.route('/register', methods=['POST','GET'])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('main.Home'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.Please Try Another One")
            return redirect(url_for('auth.Register'))
        else:
            new_user = User(email=email,password=generate_password_hash(password),first_name=first_name,last_name=last_name,is_admin=0)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,False)
            flash("Registered and Logged in successfully")
            return redirect(url_for('main.Home'))
    return render_template('auth/register.html',page_name="Register")








