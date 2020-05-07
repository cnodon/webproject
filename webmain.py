from flask import Flask

from flask_mysqldb import MySQL

from flask import render_template

from flask import Response

from datetime import datetime

from time import sleep

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'oDon2158'
app.config['MYSQL_DB'] = 'classicmodels'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route("/auto")
def auto():
    cur = mysql.connection.cursor()
    cur.execute('''select * from offices;''')
    results = cur.fetchall()
    return str(results)


@app.route("/movie")
def movie():
    return render_template('movie.html', title='Movie')


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'PKR'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/user/<username>")
def show_profile(username):
    return "<h1 style='color:blue;text-align:center;margin:200px auto;border:1px solid blue;padding:10px " \
           "20px;width:300px;'>User %s!</h1>" % username


if __name__ == "__main__":
    app.run(host='0.0.0.0')
