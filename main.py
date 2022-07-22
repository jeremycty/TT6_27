from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
###User details table
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required when creating DB.

###Exchange rate table
class ExchangeRate(db.Model):
    __tablename__ = "exchange_rate"
    id = db.Column(db.Integer, primary_key=True)
    base_currency = db.Column(db.String(100))
    exchange_currency = db.Column(db.String(100), unique=True)
    rate = db.Column(db.Integer)

    def to_dict(self):
        dictionary={}
        for column in self.__table__.columns:
            dictionary[column.name]=getattr(self, column.name)
        return dictionary

# db.create_all()

### INITIALIZE LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
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

@app.route('/exchange-rates', methods=["GET"])
def exchange_rates():
    rates=ExchangeRate.query.all()
    allratesdict=[rate.to_dict() for rate in rates]
    return jsonify(rates=allratesdict)


if __name__=="__main__":
    app.run(debug=True)
