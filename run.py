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
    lokerid = db.reference("lokerid").order_by_child("id").get().values()
    karir = db.reference("karir").order_by_child("id").get().values()
    topkarir = db.reference("topkarir").order_by_child("id").get().values()
    jooble = db.reference("jooble").order_by_child("id").get().values()
    return render_template('index.html',lokerid=lokerid,jobstreet=jobstreet,karir=karir,topkarir=topkarir,jooble=jooble)

@app.route('/search', methods=['POST'])
def search():
    kw = request.form.get('kw') 
    src = request.form.get('db') 
    sal = request.form.get('sal') 
    data = db.reference(src).order_by_child('id').get().values()
    return render_template('index.html',lokerid=data,jobstreet='',karir='',topkarir='',jooble='')
    #return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=9900)
