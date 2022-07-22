from flask import Flask, redirect, url_for, render_template, request, jsonify, make_response, session

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route("/", methods=["POST", "GET", "ET"])
def home():
        return render_template("index.html")


if __name__== "__main__":
    app.run(debug=True)
