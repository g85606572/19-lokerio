from flask import Flask, render_template, request, redirect, url_for, session

from function import _serial
import time
from database import*
from pprint import pprint
import re
import string


app = Flask(__name__)


def findMatch(l, word):
    print("\n".join(s for s in l if word.lower() in s.lower()))
    print('==========')
    return [s for s in l if word.lower() in s.lower()]


#word = 'Jaka'
#l = ['it', 'jakarta', 'juta', 'jakabaring']
#findMatch(l, word)


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
    print("keword : ", kw)
    src = request.form.get('db')
    sal = request.form.get('sal')
    search = db.reference(src).order_by_child('company').get()
    myList = []
    for i in search.values():
        com = i.get('company')
        pos = i.get('position')
        sala = i.get('salary')
        myList.append(com)
        myList.append(pos)
        myList.append(sala)
    print(myList)

    x = findMatch(myList, kw)
    print('x : ', x)
    for result in x:
        # print(result)
        match_company = db.reference(src).order_by_child(
            'company').equal_to(result).get().values()
        match_position = db.reference(src).order_by_child(
            'position').equal_to(result).get().values()
        match_salary = db.reference(src).order_by_child(
            'salary').equal_to(result).get().values()
        #print('match : ', match_company)
        print("++++++++++")
        return render_template('index.html', lokerid='', jobstreet='', karir='', topkarir='', jooble='', search=match_company, by_position=match_position, by_salary=match_salary, param=src)
    return render_template('index.html', lokerid='', jobstreet='', karir='', topkarir='', jooble='', search='', param=src)


y = 'Rp 3.8juta - Rp 4juta'
#y = '-'


def Gaji(nilai_acak):
    extract = y.split(' ')
    juta = y.replace('juta', '000000')
    print(extract, juta)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=9900)
