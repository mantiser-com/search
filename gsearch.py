from googlesearch import search
from logg import loggNice
import time
import pprint
from googleapiclient.discovery import build
import json
import re

def searchGoogle(searchWord):
  #	'''
  #	Search google for this words and get emails fromresult
  #	'''
  #
  #
  #Get list of excluded sites

  with open('exclude.json') as json_file:
    data = json.load(json_file)

  #print(words.encode('utf-8'))
  url_list=[]


  for url in search(searchWord, stop=1):
      isNotBlocked=True 
      for pattern in data['sites']:
        if re.search(pattern, url):
            loggNice('found a match!')
            loggNice('blocked site {0}'.format(url))
            isNotBlocked=False
      
      if isNotBlocked:     
          url_list.append(url)
  return url_list
