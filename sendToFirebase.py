from firebase import firebase
import json
import datetime


firebase = firebase.FirebaseApplication('https://*.firebaseio.com/', None)

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

	result = firebase.post('/todos/'+user+'/emails/', data, params={'print': 'pretty'})
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

	result = firebase.post('/todos/'+user+'/pages/', data, params={'print': 'pretty'})
	print(result)

def startScanFirebase(user,botid):
	'''
	Set the scan to started
	'''
	now = datetime.datetime.now()

	#Get the running version 
	result = firebase.get('/todos/'+user+'/bot/'+botid, None)

	if result != None:
		print(result)
		result['status'] = "Started"
		result['StartedTime']=now.isoformat()
		result = firebase.put('/todos/'+user+'/bot/', data=result, name=botid)


def doneScanFirebase(user,botid):
	'''
	Set the scan to started
	'''
	now = datetime.datetime.now()

	#Get the running version 
	result = firebase.get('/todos/'+user+'/bot/'+botid, None)
	result['status'] = "Done"
	result['StopedTime']=now.isoformat()



	result = firebase.put('/todos/'+user+'/bot/', data=result, name=botid)

