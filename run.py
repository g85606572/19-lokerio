from flask import Flask, render_template, request, redirect, url_for, session, flash

from function import _serial
import time
from database import*
from pprint import pprint
import re
import string


app = Flask(__name__)
app.secret_key = '#############-####my###-secr#3#et-key########'


def search(l, w):
    match_string = w
    matched_sent = [s for s in l if len(re.findall(
        r"\b{}\b".format(w), s, re.IGNORECASE)) > 0]
    return matched_sent


def findMatch(l, word):
    print('A==========')
    print("\n".join(s for s in l if word.lower() in s.lower()))
    print('B==========')
    return [s for s in l if word.lower() in s.lower()]


@app.route('/', methods=['POST', 'GET'])
def home():

    jobstreet = db.reference("jobstreet").order_by_child("id").get().values()
    lokerid = db.reference("lokerid").order_by_child("id").get().values()
    karir = db.reference("karir").order_by_child("id").get().values()
    topkarir = db.reference("topkarir").order_by_child("id").get().values()
    jooble = db.reference("jooble").order_by_child("id").get().values()
    return render_template('index.html', lokerid=lokerid, jobstreet=jobstreet, karir=karir, topkarir=topkarir, jooble=jooble)


@app.route('/search', methods=['POST'])  # JADI
def _search():
    kw = request.form.get('kw')
    src = request.form.get('db')
    sal = request.form.get('sal')
    i_resTitle = search(mylist, kw)
    print(i_resTitle)
    #flash('Menemukan {}  hasil terkait `{}`.'.format( len(i_resTitle), kw.title()))
    return render_template('index.html', lokerid='', jobstreet='', karir='', topkarir='', jooble='', by_company='', by_position='', by_salary='', param=src)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=9900)
