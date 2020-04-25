from flask import Flask

from flask import render_template

app = Flask(__name__)


# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)


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


@app.route("/")
def root_page():
    return "<h1 style='color:blue;text-align:center;margin:200px auto;border:1px solid blue;padding:10px " \
           "20px;width:300px;'>Root Page!</h1> "


@app.route("/user/<username>")
def show_profile(username):
    return "<h1 style='color:blue;text-align:center;margin:200px auto;border:1px solid blue;padding:10px " \
           "20px;width:300px;'>User %s!</h1>" % username


if __name__ == "__main__":
    app.run(host='0.0.0.0')
