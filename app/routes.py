from app import app
from flask import request,redirect, render_template, session, url_for, escape, jsonify
from collections import namedtuple
import requests, json

@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path 
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

@app.route("/")
def firstpage():
    return redirect(url_for('index'))

@app.route("/index", methods = ['GET'])
@app.route("/index/<name>", methods = ['GET'])
def index(name = None):
    return render_template('index.html', name = name)

@app.route("/salesorderpage", methods = ['GET', 'POST'])
def salesorderpage():
    if request.method == 'GET':
        return render_template('salesorderfind.html')
    
    num = request.form.get('salesnumber')
    print("HERE" + num)
    myJson = getSalesOrder(int(str(num)))
    return render_template('salesorderview.html', data=myJson)

@app.route("/summary")
def summary():
    d = requests.get('http://cbahaph9b.central.cmich.local:8080/sap/bc/114rest_service/0000000156?sap-client=555')
    retval = d.json()
    print(retval['VBELN'])
    return retval

def getSalesOrder(id):
    d = requests.get('http://cbahaph9b.central.cmich.local:8080/sap/bc/114rest_service/' + format(id, '010d') + '?sap-client=555')
    thing = d.text
    myJson = json.loads(thing)
    if myJson:
        return myJson
    return