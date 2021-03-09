#!/usr/bin/env python
import pika
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


for result in searchGoogle(os.getenv('SEARCH')):
    result_json ={
    	"action": "searchGoogle",
    	"url" : result,				
    }
    loggNice(result_json)
    #addTask(result_json,in_seconds=None)
    addNatsRun("result",result_json)


loggNice("Google Search done !")
