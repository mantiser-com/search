from googlesearch import search
from getemail import getEmails


def searchGoogle(words):
	'''
	Search google for this words and get emails fromresult
	'''

	print("###############################################################################################################")
	print(words)
	for url in search(words, stop=20):
	    
	    search_url=[url]
	    getEmails(search_url,words)


