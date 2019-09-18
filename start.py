#
#
#
# File to start
#
# Lissen for events from the que
#!/usr/bin/env python
import pika
import time
from gsearch import searchGoogle
from addToTask import addTask
import time
import json
from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/search/",methods = ['GET', 'POST'])
def doGoogleSearch():
	if request.method == 'POST':
		#Get payload as text
		payload = request.get_data(as_text=True)
		#Convert paylaod to json
		json_payload = json.loads(payload)

		for result in searchGoogle(json_payload['data'],json_payload['id'],json_payload['uid']):
			result_json ={
				"action": "scrapeEmail",
				"url" : result,
				"uid" : json_payload["uid"],
				"id" : json_payload["id"],
				"word": json_payload['data']				
			}
			print(result_json)
			addTask(result_json,in_seconds=None)
		#Adding the close worker you
		result_json ={
				"action" : "close",
				"uid" : json_payload["uid"],
				"id" : json_payload["id"],
				}
		addTask(result_json,in_seconds=None)

		
		return "Google Search done !"
	else:
		return "We got get"

@app.route("/", methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		return "We got post at /"
	else:
		return "We got get at /"

