import asyncio
import nest_asyncio
import datetime
import os
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers
nest_asyncio.apply()

async def addNats(loop,to,text):
    nc = NATS()

    await nc.connect("{}:4222".format(os.getenv('NATS')), loop=loop)

    # Stop receiving after 2 messages.
    await nc.publish(to, str(text).encode('utf8'))

    # Terminate connection to NATS.
    await nc.close()


def addNatsRunFind(to,searchJson):
    json_upload = {
        "action":searchJson["action"],
        "data": searchJson,
        "timestamp": datetime.datetime.now().isoformat()


    } 



    loop = asyncio.new_event_loop()
    loop.run_until_complete(addNats(loop,to,json_upload))
    loop.close()
    return {
           "deliverd:{0}".format(to):"ok" 
    }





