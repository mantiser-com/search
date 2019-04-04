import json
import subprocess
from helmDeployer.initConfig import setupGcloud

def deployEmailBot(message):
    '''
    Will setup and deploy the emailbot with helm
    '''
    print("Settup helm")
    setupGcloud()



    print(message)
    jsonMessage = json.loads(message)

    if jsonMessage['userMailChimpKey'] != 'nne':

        searchWord = jsonMessage['words']
        botName = 'searchbot-'+str(jsonMessage['botid']).lower().replace('_','-')
        userEmail = jsonMessage['email']
        userID = jsonMessage['user']
        mailChimpKey = jsonMessage['userMailChimpKey']
        mailChimpList = jsonMessage['MailChimpList']
        cronSetting = jsonMessage['cronMin']+" "+jsonMessage['cronHour']

        if jsonMessage['repete'] == 'daily':
            cronSetting = cronSetting + " * * *"
        elif jsonMessage['repete'] == 'weekly':
            cronSetting = cronSetting + " * * *"
        elif jsonMessage['repete'] == 'monthly':
            cronSetting = cronSetting + " * * *"
        else:
            cronSetting = cronSetting + " * * *"
        
        #Deploy to kubernetes
        process = subprocess.Popen('''helm install --name {0} --debug helm/mrsender/ --namespace=finder --set firebase="https://fins-dff79.firebaseio.com",firebase_auth="/keys/fins.json",user_id="{6}",match="{1}",mailchimp_list="{4}",mailchimp_api="{3}",how_many=5,delete_after=false,cron="{5}",name={0}'''.format(botName,searchWord,userEmail,mailChimpKey,mailChimpList,cronSetting,userID), shell=True, stdout=subprocess.PIPE)
        print(process.communicate())
        if process.returncode == 0:
    	    print("Sucessfull activted cluster ref")
        else:
    	    print("Error activated cluster")


    else:
        print("Need api key")