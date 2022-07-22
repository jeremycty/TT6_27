from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import requests

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

##create Wallet TABLE
class Wallet(db.Model):
    __tablename__ = "wallet"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(1000))

##create Currency TABLE
class Currency(db.Model):
    __tablename__ = "currency"
    id = db.Column(db.Integer(), primary_key=True)
    wallet_id = db.Column(db.Integer(), db.ForeignKey('wallet.id'), nullable=False)
    currency = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float(), nullable=True)

##create Transaction TABLE
class Transaction(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer(), primary_key=True)
    wallet_id = db.Column(db.Integer(), db.ForeignKey('wallet.id'), nullable=False)
    debit_id = db.Column(db.Integer(), nullable=False)
    debit_currency = db.Column(db.String(100), nullable=False)
    debit_amount = db.Column(db.Float(), nullable=False)
    credit_id = db.Column(db.Integer(), nullable=False)
    credit_currency = db.Column(db.String(100), nullable=False)
    credit_amount = db.Column(db.Float(), nullable=False)
    description = db.Column(db.Text())
    created_at = db.Column(db.DateTime(timezone=True))
    create_by = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True))
    updated_by = db.Column(db.String(100), nullable=False)


##db.create_all()


#Wallet Table
class Wallet(db.Model):
    __tablename__ = 'wallet'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(1000))


### INITIALIZE LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#home
@app.route('/')
def home():
    return render_template("index.html")

#login
@app.route('/login', methods=["POST"])
def login():
    if request.method=="POST":
#### Retrive input details from user
        inputpw=request.form.get("password")
        inputemail=request.form.get("email")
######Check if user is registered in database
        account=User.query.filter_by(email=inputemail).first()
        if account is None:
            return render_template("login.html", message='User does not exist')
######Check if password is correct
        else:
            if account.password != inputpw:
                return render_template("login.html", message='Incorrect Password')
            else:
                login_user(account)
                return redirect(url_for('home', message='Logged in successfully.'))
    return render_template("login.html")

#logout
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

#exchange rates
@app.route('/exchange-rates')
def exchange_rates():
    exchangerates=ExchangeRate.query.all()
    ##Retrieving live exchange rate
    try:
        param = {"base": "SGD"}
        ratesurl = 'https://api.exchangerate.host/latest'
        response = requests.get(ratesurl, params=param)
        ratesdata=response.json()["rates"]
        ###Update Exchange rate in database
        for exchangerate in exchangerates:
            exchangerate.rate=ratesdata[exchangerate.exchange_currency]
            db.session.commit()
    finally:
        updatedexchangerates=ExchangeRate.query.all()
        allratesdict=[rate.to_dict() for rate in updatedexchangerates]
        return jsonify(rates=allratesdict)

@app.route('/currency')
def currency():
    return redirect(url_for('currency'))

@app.route('/transaction')
def transaction():
    return redirect(url_for('transaction'))

@app.route('/wallet', methods = ["GET"])
def wallet():
    wallet_info = Wallet.query.all()
    wallet_dict = []

    for info in wallet_info:
        wallet_dict.append({'id': info.id, 'user_id': info.user_id,'name': info.name})

    return jsonify(wallet_dict)

if __name__=="__main__":
    app.run(debug=True)
