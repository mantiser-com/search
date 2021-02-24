from googlesearch import search
import time
import pprint
from googleapiclient.discovery import build
import json
import re







def searchGoogle(words,botid,user):
  #	'''
  #	Search google for this words and get emails fromresult
  #	'''
  #
  #
  #Get list of excluded sites

  with open('exclude.json') as json_file:
    data = json.load(json_file)

  print("###############################################################################################################")
  #print(words.encode('utf-8'))
  url_list=[]


  for url in search(words, stop=50):
      isNotBlocked=True 
      for pattern in data['sites']:
        if re.search(pattern, url):
            print('found a match!')
            print('blocked site {0}'.format(url))
            isNotBlocked=False
      
      if isNotBlocked:     
          url_list.append(url)
  return url_list
