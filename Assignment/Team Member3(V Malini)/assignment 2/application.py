from flask import Flask, render_template
import sqlite3 as sql

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/about')
def about():
     return render_template('about.html')

if __name__=='__main__':
    app.run(host='0.0.0.0' ,port=8000,debug=True)
    
