from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

##create Currency TABLE
class currency(db.model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, primary_key=True)

##create Transaction TABLE
class transaction(db.model):
    id = db.Column(db.Integer, primary_key=True)
    debit_currency = db.Column(db.String(100), nullable=False)
    debit_amount = db.Column(db.Integer, primary_key=True)
    credit_currency = db.Column(db.String(100), nullable=False)
    credit_amount = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True))
    create_by = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True))
    updated_by = db.Column(db.String(100), nullable=False)

#Line below only required once, when creating DB.
db.create_all()

### INITIALIZE LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="POST":
        inputpw=request.form.get("password")
        inputemail=request.form.get("email")
        account=User.query.filter_by(email=inputemail).first()
        if account is None:
            flash('User does not exist')
        else:
            if account.password== inputpw:
                flash('Incorrect Password')
            else:
                login_user(account)
                flash('Logged in successfully.')
                return redirect(url_for('home', current_user=current_user))
    return render_template("login.html")

@app.route('/currency', methods=["GET", "POST"])
def currency():
    user_currency=
    return jsonify

if __name__=="__main__":
    app.run(debug=True)
