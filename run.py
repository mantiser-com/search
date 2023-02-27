#!/usr/bin/env python
import time
from gsearch import searchGoogle, searchGoogleLiveddg
from addNats import addNatsRunFind
import time
import json
import uuid
import os
from logg import loggNice



'''
Get the serach word and send to search engines to search for it
'''
from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)


def setValues(payload):
        #Setup defaults
        try: 
            userid = payload['userid']
        except:
            userid = "1"
        try: 
            postid = payload['postid']
        except:
            #If we dont have a postid we create one
            postid = str(uuid.uuid1())
        try: 
            scannerid = payload['scannerid']
        except:
            scannerid = "1" 
        try: 
            getemail = payload['getemail']
        except:
            getemail = "false" 
        try: 
            prefix = payload['prefix']
        except:
            prefix = "none"
        try: 
            project = payload['project']
        except:
            project = "mantiser"
        try: 
            dest = payload['dest']
        except:
            dest = []
        try: 
            deep = payload['deep']
        except:
            deep = 5


        jsonData = {
                    "userid":userid,
                    "postid":postid,
                    "scannerid":scannerid,
                    "getemail":getemail, 
                    "project": project,
                    "prefix": prefix,
                    "dest": dest,
                    "deep": deep 
                    } 
        return jsonData



@app.route("/search/",methods = ['GET', 'POST'])
def spider():
    if request.method == 'POST':
        #Get payload as text
        payload = request.get_data(as_text=True)
        #Convert paylaod to json
        json_payload = json.loads(payload)
        Private = False
        #Setup values
        try: 
            action = json_payload['action']
        except:
            action = "search"
        try: 
            search = json_payload['action']
        except:
            search = "none"
        try: 
            scannerid = json_payload['scannerid']
        except:
            scannerid = str(uuid.uuid1()) 

        #Set json_payload the the default values
        json_payload=setValues(json_payload)
        # Doing Google search
        for result in searchGoogle(search):
            json_payload['action']=action
            json_payload['url']=result
            json_payload['search']=search
            json_payload['scannerid']=scannerid
            loggNice(json_payload)
            
            #Send to nats
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
            action = "page"
        try: 
            url = json_payload['url']
        except:
            url = "none"


        #Set json_payload the the default values
        json_payload=setValues(json_payload)
        json_payload['action']=action
        json_payload['url']=url
        print(json_payload)
        
        #Send to nats
        response = addNatsRunFind("result",json_payload)
        loggNice(response)
        loggNice("Page added to que !")
        return "Page added to que !"
        #except:
        #    return "Bad data"


        
    else:
        return "dont want GET"
#
# Support the mantiser app
#

@app.route("/livesearch/",methods = ['GET', 'POST'])
def livesearch():
    if request.method == 'POST':
        #Get payload as text
        payload = request.get_data(as_text=True)
        #Convert paylaod to json
        json_payload = json.loads(payload)
        search = json_payload['search']
        # Doing Google search
        return searchGoogleLiveddg(search,20)
    else:
        return "Only accept POST"