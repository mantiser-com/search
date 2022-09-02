from googlesearch import search
from duckduckgo_search import ddg
from logg import loggNice
import time
import pprint
from googleapiclient.discovery import build
import json
import re
import os
from bs4 import BeautifulSoup
import requests, lxml

from googleapiclient.discovery import build
my_api_key = os.getenv('API_KEY')
my_cse_id = os.getenv('CSE_ID')


headers = {
  'User-agent':
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}




def get_organic_results(searchWord):


  params = {
    'q': searchWord,
    'source': 'web'
  }
  html = requests.get('https://search.brave.com/search', headers=headers, params=params)
  soup = BeautifulSoup(html.text, 'lxml')

  data = []
  result = soup.select('.snippet.fdb')
  for r in result:
    netloc= r.select(".netloc")
    print("brave: "+ netloc[0].text)
    data.append(netloc[0].text)
  return data






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
  #Uisng ddg
  results_ddg = ddg(searchWord, region='wt-wt', safesearch='Moderate', time='y', max_results=60)
  #
  for url in results_ddg:
    print("ddg: "+ url['href'])
    isNotBlocked=True
    for pattern in data['sites']: 
      if re.search(pattern, url['href']):
          loggNice('found a match!')
          loggNice('blocked site {0}'.format(url['href']))
          isNotBlocked=False

      if isNotBlocked:     
          url_list.append(url['href'])
    

  results_ddg = ddg(searchWord, region='se-sv', safesearch='Moderate', time='y', max_results=60)
  #
  for url in results_ddg:
    print("ddg: "+ url['href'])
    isNotBlocked=True
    for pattern in data['sites']: 
      if re.search(pattern, url['href']):
          loggNice('found a match!')
          loggNice('blocked site {0}'.format(url['href']))
          isNotBlocked=False

      if isNotBlocked:     
          url_list.append(url['href'])




  # using google custom search
  service = build("customsearch", "v1", developerKey=my_api_key)
  results_cse = service.cse().list(q=searchWord, cx=my_cse_id).execute()
  for url in results_cse['items']:
    print("custom search : "+ url['link'])
    for pattern in data['sites']:
      if re.search(pattern, url['link']):
          loggNice('found a match!')
          loggNice('blocked site {0}'.format(url['link']))
          isNotBlocked=False

      if isNotBlocked:     
          url_list.append(url['link'])

  braveurl = get_organic_results(searchWord)
  for url in braveurl:
      for pattern in data['sites']:
        if re.search(pattern, url):
            loggNice('found a match!')
            loggNice('blocked site {0}'.format(url))
            isNotBlocked=False

        if isNotBlocked:     
            url_list.append(url)  



  #for url in search(searchWord, stop=30):
  #    isNotBlocked=True 
  #    for pattern in data['sites']:
  #      if re.search(pattern, url):
  #          loggNice('found a match!')
  #          loggNice('blocked site {0}'.format(url))
  #          isNotBlocked=False
  #    
  #    if isNotBlocked:     
  #        url_list.append(url)
  res_url = [*set(url_list)]
  return res_url


#searchGoogle("braveops")
