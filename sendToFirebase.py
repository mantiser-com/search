# -*- coding: utf-8 -*
import json
import datetime
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate('/keys/fins-dff79-7e8d54a5f33e.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fins-dff79.firebaseio.com',
    'storageBucket': 'fins-dff79.appspot.com'
})
bucket = storage.bucket()




def upload_blob(botid):
	"""Uploads a file to the bucket."""
	bucket = storage.bucket()
	#file is just an object from request.files e.g. file = request.files['myFile']
	blob = bucket.blob("email/"+botid+".csv")
	blob.upload_from_string("out/"+botid+".csv")
	#os.remove("out/"+botid+".csv") 

	print(blob.public_url)






def addEmailFirebase(email,user,site,words,botid):
	'''
	Add the email to the database
	'''
	now = datetime.datetime.now()


	data   = {
		'email':email,
		'site':site,
		'words':words,
		'botid':botid,
		'datetime': now.isoformat()
	}

	save_ref= 	ref = db.reference('/todos/'+user+'/emails/')
	result = save_ref.push(data)
	print(result)


def addUrlsFirebase(user,site,words,botid):
	'''
	Add the email to the database
	'''

	now = datetime.datetime.now()


	data   = {
		'site':site,
		'words':words,
		'botid':botid,
		'datetime': now.isoformat()

	}

	save_ref= 	ref = db.reference('/todos/'+user+'/pages/')
	result = save_ref.push(data)
	print(result)

def startScanFirebase(user,botid):
	'''
	Set the scan to started
	'''
	now = datetime.datetime.now()

	#Get the running version 
	ref = db.reference('/todos/'+user+'/bot/'+botid)
	result = ref.get()
	
	if result != None:
		#print(result.encode('utf8'))
		result['status'] = "Started"
		result['StartedTime']=now.isoformat()
		save_ref= 	ref = db.reference('/todos/'+user+'/bot/'+botid)
		result = save_ref.set(result)
		

def doneScanFirebase(user,botid):
	'''
	Set the scan to started
	'''
	now = datetime.datetime.now()

	#Get the running version 
	ref = db.reference('/todos/'+user+'/bot/'+botid)
	refdone = db.reference('/todos/'+user+'/botdone/'+botid)
	result = ref.get()
	result['status'] = "Done"
	result['StopedTime']=now.isoformat()


	result_done = refdone.set(result)
	save_ref= 	ref = db.reference('/todos/'+user+'/bot/'+botid)
	result = save_ref.set(result)

