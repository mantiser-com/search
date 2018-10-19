from googlesearch import search
from getemail import getEmails
import time

dontSearch =['youtube','indeed','wikipedia','twitter','bing','yahoo']



def searchGoogle(words):
	'''
	Search google for this words and get emails fromresult
	'''

	print("###############################################################################################################")
	print(words)
	for url in search(words, stop=20):
		print(url)
		serchthis = True
		for dont in dontSearch:
			if dont in url:
				serchthis = False
			
		if serchthis:
			search_url=[url]
			getEmails(search_url,words)
			time.sleep(30)



