#
#
#
# File to start
#
# Lissen for events from the que
#!/usr/bin/env python
import pika
import time
from gsearch import searchGoogle
import time
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat=600,
                                       blocked_connection_timeout=300))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)



def DotheSearch(message):
	'''
	Get data from rabbit and start
	'''
	mess = json.loads(message)

	#Get all google search
	if mess['type'] =='google' and mess['words'] != '':		
		print('Start Google seacrh')
		searchGoogle(mess['words'],mess['botid'],mess['user'],mess['email'],mess['MailChimpList'],mess['userMailChimpKey'])

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    DotheSearch(body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
