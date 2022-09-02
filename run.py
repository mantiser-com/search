#!/usr/bin/env python
import time
from gsearch import searchGoogle
from addNats import addNatsRunFind
import time
import json
import os
from logg import loggNice



'''
Get the serach word and send to search engines to search for it
'''
from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/search/",methods = ['GET', 'POST'])
def spider():
    if request.method == 'POST':
        #Get payload as text
        payload = request.get_data(as_text=True)
        #Convert paylaod to json
        json_payload = json.loads(payload)
        Private = False
        try: 
            action = json_payload['action']
        except:
            action = "search"
        search = json_payload['search']
        # Doing Google search
        for result in searchGoogle(search):
            json_payload['action']=action
            json_payload['url']=result
            loggNice(json_payload)
            response = addNatsRunFind("result",json_payload)
            loggNice(response)
        loggNice("Search done !")



        return "Spider Done !"
    else:
        return "Spinder dont want GET"

@app.route("/page/",methods = ['GET', 'POST'])
def page():
    if request.method == 'POST':
        #Get payload as text
        payload = request.get_data(as_text=True)
        #Convert paylaod to json
        json_payload = json.loads(payload)
        try: 
            action = json_payload['action']
        except:
            action = "search"
        json_payload['action']=action
        loggNice(json_payload)
        response = addNatsRunFind("result",json_payload)
        loggNice(response)
        loggNice("Page added to que !")
        return "Page added to que !"
        #except:
        #    return "Bad data"


        
    else:
        return "dont want GET"