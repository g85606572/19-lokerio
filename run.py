from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

from function import _serial
import time
from database import*
from pprint import pprint
import re
import string
import random

from function import _serial
from collections import OrderedDict, Counter


app = Flask(__name__)
app.secret_key = '#############-####my###-secr#3#et-key########'


# $Internal Functions


def r_pK():
    try:
        pK = []
        other = ['.', '..', '...']
        ref = db. reference('populer').order_by_child('id').get()

        for k in ref.values():
            refs = k.get('position')
            url = k.get('url')

            pK.append(refs.title()+' | ' + str(url))
        return pK
    except Exception as e:
        return other


def popularKeywords():
    c = Counter(r_pK())
    mc = c.most_common(3)
    newMc = []
    for row in mc:
        a = row[0]
        print(a)
        newMc.append(a)
    return newMc


def randColor():
    col = ['danger', 'primary', 'dark', 'secondary', 'success', 'warning']
    return random.choice(col)


@app.route('/', methods=['POST', 'GET'])
def home():

    jobstreet = db.reference("jobstreet").order_by_child("id").get().values()
    lokerid = db.reference("lokerid").order_by_child("id").get().values()
    karir = db.reference("karir").order_by_child("id").get().values()
    topkarir = db.reference("topkarir").order_by_child("id").get().values()
    jooble = db.reference("jooble").order_by_child("id").get().values()
    return render_template('index.html', lokerid=lokerid, jobstreet=jobstreet, karir=karir, topkarir=topkarir, jooble=jooble, populer=popularKeywords(), randColor=randColor)


@app.route('/populer', methods=['POST', 'GET'])  # J
def popl():
    id = _serial()
    a = request.form.get('position')
    b = request.form.get('url')
    data = {"id": id, "position": a, "url": b}
    db.reference("populer").child(id).update(data)
    return redirect(b, code=302)


'''auto scrap setiap jam 8 pagi'''
import schedule #ini schedule.py
from scrap import jobstreet,karir,topkarir,jooble,loker_id
'''auto scrap setiap jam 8 pagi'''
def scrapOtomatis():
    jobstreet()
    loker_id()
    karir()
    jooble()
    topkarir()
    return 
schedule.every().day.at("08:00").do(scrapOtomatis)
'''auto scrap setiap jam 8 pagi'''

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=9900)
