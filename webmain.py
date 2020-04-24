from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "<h1 style='color:blue;text-align:center;margin:200px auto;border:1px solid blue;padding:10px 20px;width:300px;'>Welcome to Flask!</h1>"

@app.route("/index")
def index():
    return "<h1 style='color:blue;text-align:center;margin:200px auto;border:1px solid blue;padding:10px 20px;width:300px;'>Index Page!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
