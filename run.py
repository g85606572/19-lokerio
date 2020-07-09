from flask import Flask, render_template,request,redirect,url_for,session

from function import _serial,AInc
import time
from database import*


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    jobstreet = db.reference("jobstreet").order_by_child("id").get().values()
    loker = db.reference("loker").order_by_child("id").get().values()
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=9900)
