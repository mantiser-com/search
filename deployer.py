#
#
#
# File to start
#
# Lissen for events from the que
#!/usr/bin/env python
import pika
import time
import time
import json

#Helm Deployers
from helmDeployer.emailsearch import deployEmailBot
from helmDeployer.deleteHelm import deleteHelm


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat=600,
                                       blocked_connection_timeout=300))
channel = connection.channel()

channel.queue_declare(queue='deploy_queue', durable=True)



def deployHelm(message):
    '''
    Get data from rabbit and start
    '''
    mess = json.loads(message)

    if mess['action'] == 'create':
        #Lets create the service
        if mess['type'] == 'emailbot':
            deployEmailBot(message)


        else:
            print('No deploy matching')
    elif mess['action']=="delete":
        #Delete the helm deploy
        print('lets delete')
        deleteHelm(message)


    else:
        print('Did not get a valid action')


def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    deployHelm(body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume('deploy_queue',callback)

channel.start_consuming()