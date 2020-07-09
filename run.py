from flask import Flask, render_template,request,redirect,url_for,session

from function import _serial
import time
from database import*

#garifin 
#kanye

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    jobstreet = db.reference("jobstreet").order_by_child("id").get().values()
    loker = db.reference("loker").order_by_child("id").get().values()
    return render_template('index.html',loker=loker,jobstreet=jobstreet)

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=9900)
