import os

from flask import Flask, jsonify, request

import time

from flask_mysqldb import MySQL

from flask import render_template

from flask import Response

from datetime import datetime

from time import sleep

import config

from werkzeug.utils import secure_filename

import cv2

import requests

import random

from datetime import timedelta


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


app = Flask(__name__)

app.send_file_max_age_default = timedelta(seconds=1)


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


@app.route("/imgupload", methods=['POST', 'GET'])
def imgUpload():
    if request.method == 'POST':
        f = request.files['file']

        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})

        user_input = request.form.get("name")

        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # upload_path = os.path.join(basepath, 'static/images','test.jpg')  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)

        # 使用Opencv转换一下图片格式和名称
        img = cv2.imread(upload_path)

        rand = random.randint(1, 1000)
        strNow = time.strftime('USER_%Y_%m_%d_%H_%M_%S', time.localtime())
        fileNameStr = '%s_%s.jpg' % (strNow, str(rand))
        cv2.imwrite(os.path.join(basepath, 'static/images', fileNameStr), img)

        return "<h1>Upload Successful!</h1>"

    return render_template("img_upload.html")


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
