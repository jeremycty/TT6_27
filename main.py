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

##create Currency TABLE
class Currency(db.Model):
    __tablename__ = "currency"
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=True)

##create Transaction TABLE
class Transaction(db.Model):
    __tablename__ = "transaction"
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

    def __repr__(self):
        return f'{self.debit_currency} - {self.debit_amount}'
  
db.create_all()
currencyaccountdata=[
  {
    "id": 1,
    "wallet_id": 1,
    "currency": "SGD",
    "amount": 4294.50
  },
  {
    "id": 2,
    "wallet_id": 1,
    "currency": "CAD",
    "amount": 5687.65
  },
  {
    "id": 3,
    "wallet_id": 1,
    "currency": "CNH",
    "amount": 6063.14
  },
  {
    "id": 4,
    "wallet_id": 1,
    "currency": "EUR",
    "amount": 8089.82
  },
  {
    "id": 5,
    "wallet_id": 1,
    "currency": "HKD",
    "amount": 7862.36
  },
  {
    "id": 6,
    "wallet_id": 1,
    "currency": "JPY",
    "amount": 5759.15
  },
  {
    "id": 7,
    "wallet_id": 1,
    "currency": "NZD",
    "amount": 6943.26
  },
  {
    "id": 8,
    "wallet_id": 1,
    "currency": "NOK",
    "amount": 4038.10
  },
  {
    "id": 9,
    "wallet_id": 1,
    "currency": "GBP",
    "amount": 8287.33
  },
  {
    "id": 10,
    "wallet_id": 1,
    "currency": "SEK",
    "amount": 5126.40
  },
  {
    "id": 11,
    "wallet_id": 1,
    "currency": "THB",
    "amount": 147.62
  },
  {
    "id": 12,
    "wallet_id": 1,
    "currency": "USD",
    "amount": 7331.77
  },
  {
    "id": 13,
    "wallet_id": 2,
    "currency": "SGD",
    "amount": 485.19
  },
  {
    "id": 14,
    "wallet_id": 2,
    "currency": "CAD",
    "amount": 2634.58
  },
  {
    "id": 15,
    "wallet_id": 2,
    "currency": "CNH",
    "amount": 3893.29
  },
  {
    "id": 16,
    "wallet_id": 2,
    "currency": "EUR",
    "amount": 3887.15
  },
  {
    "id": 17,
    "wallet_id": 2,
    "currency": "HKD",
    "amount": 4065.34
  },
  {
    "id": 18,
    "wallet_id": 2,
    "currency": "JPY",
    "amount": 1702.47
  },
  {
    "id": 19,
    "wallet_id": 2,
    "currency": "NZD",
    "amount": 3299.38
  },
  {
    "id": 20,
    "wallet_id": 2,
    "currency": "NOK",
    "amount": 7681.32
  },
  {
    "id": 21,
    "wallet_id": 2,
    "currency": "GBP",
    "amount": 3720.37
  },
  {
    "id": 22,
    "wallet_id": 2,
    "currency": "SEK",
    "amount": 4511.50
  },
  {
    "id": 23,
    "wallet_id": 2,
    "currency": "THB",
    "amount": 6216.60
  },
  {
    "id": 24,
    "wallet_id": 2,
    "currency": "USD",
    "amount": 9103.66
  }
]
for account in currencyaccountdata:
    newaccount=Currency(currency=account["currency"],
                amount=account["amount"])
    db.session.add(newaccount)
    db.session.commit()




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
    
    
if __name__=="__main__":
    app.run(debug=True)
