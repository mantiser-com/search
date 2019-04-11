import json
import subprocess
import sendToFirebase
from helmDeployer.initConfig import setupGcloud

def deleteHelm(message):
    '''
    Will delete helm chart
    '''
    print("Settup helm")
    setupGcloud()



    print(message)
    jsonMessage = json.loads(message)
    chartName=''


    if jsonMessage['type'] == 'emailbot':
        chartName= 'searchbot-'+str(jsonMessage['botid']).lower().replace('_','-')
    else:
        chartName= str(jsonMessage['botid']).lower().replace('_','-')

        
    #Delete to kubernetes
    process = subprocess.Popen('''helm del --purge {0} '''.format(chartName), shell=True, stdout=subprocess.PIPE)
    print(process.communicate())
    if process.returncode == 0:
        print("Sucessfull deployed")
        sendToFirebase.helmEbotDeleted(jsonMessage['user'],jsonMessage['botid'])


    else:
        print("Error deploying")
