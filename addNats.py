import asyncio
import nest_asyncio
import datetime
import os
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers
nest_asyncio.apply()

async def addNats(to,text):
    nc = NATS()

    await nc.connect("{}:4222".format(os.getenv('NATS')))

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



    asyncio.run(addNats(to,json_upload))
    #addNats(to,json_upload)
    return {
           "deliverd:{0}".format(to):"ok" 
    }





