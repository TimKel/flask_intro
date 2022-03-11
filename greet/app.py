from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/home')
def welcome2():
    return f"<h1>Welcome home</h1>"

@app.route('/welcome/back')
def welcome3():
    return f"<h1>Welcome BACK</h1>"

