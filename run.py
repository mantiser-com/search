#!/usr/bin/env python
import time
from gsearch import searchGoogle
from addNats import addNatsRun
import time
import json
import os
from logg import loggNice



'''
Get the serach word and send to search engines to search for it
'''

# Doing Google search
for result in searchGoogle(os.getenv('SEARCH')):
    result_json ={
    	"action": "searchGoogle",
    	"url" : result,
        "user_id": 	os.getenv('USER_ID')			
    }
    loggNice(result_json)
    response = addNatsRun("result",result_json)
    loggNice(response)

loggNice("Search done !")
