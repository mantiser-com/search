from googlesearch import search
from getemail import getEmails
import time

dontSearch =['youtube','indeed','wikipedia','twitter','bing','yahoo','templatemonster']



def searchGoogle(words):
	'''
	Search google for this words and get emails fromresult
	'''

	print("###############################################################################################################")
	print(words.encode('utf-8'))
	for url in search(words, stop=100):
		print(url)
		serchthis = True
		for dont in dontSearch:
			if dont in url:
				serchthis = False
			
		if serchthis:
			search_url=[url]
			#try:
			getEmails(search_url,words)
			#except:
			#	print("got some error doing next page")
			time.sleep(30)

	print("################################# The End ######################")

