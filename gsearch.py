from googlesearch import search
from getemail import getEmails
from sendToFirebase import *
import time

dontSearch =['youtube','indeed','wikipedia','twitter','bing','yahoo','templatemonster']



def searchGoogle(words,botid,user,email,mailchimpkey,mailchimplist):
	'''
	Search google for this words and get emails fromresult
	'''

	startScanFirebase(user,botid)

	print("###############################################################################################################")
	print(words.encode('utf-8'))
	for url in search(words, stop=3):
		print(url)
		serchthis = True
		for dont in dontSearch:
			if dont in url:
				serchthis = False
			
		if serchthis:
			search_url=[url]
			#try:
			getEmails(search_url,words,user,botid,mailchimplist,mailchimpkey)
			print(words.encode('utf8'))
			#except:
			#	print("got some error doing next page")
			
	print("################################# The End ######################")
	upload_blob(botid)
	doneScanFirebase(user,botid)
