import asyncio
import os
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def addNats(loop,to,text):
    nc = NATS()

    await nc.connect("{}:4222".format(os.getenv('NATS')), loop=loop)

    # Stop receiving after 2 messages.
    await nc.publish(to, str(text).encode('utf8'))

    # Terminate connection to NATS.
    await nc.close()


def addNatsRun(to,text):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(addNats(loop,to,text))
    loop.close()
    return {
           "deliverd":"ok" 
    }