import asyncio
import os
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers
import requests
import json
'''
To test that the search adds data to nats we can use this python file
'''
async def run(loop):
    
    nc = NATS()
    async def disconnected_cb():
        print("Got disconnected...")
    async def reconnected_cb():
        print("Got reconnected...")

   

    sc = STAN()
    await sc.connect("mantiser", "worker", nats=nc)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))
    
    total_messages = 0
    future = asyncio.Future(loop=loop)
    async def cb(msg):
        nonlocal future
        nonlocal total_messages
        print("Received a message (seq={}): {}".format(msg.seq, msg.data))
        total_messages += 1
        if total_messages >= 2:
            future.set_result(None)


    # Simple publisher and async subscriber via coroutine.
    sid = await sc.subscribe("result",start_at='last_received"', cb=cb)
    await asyncio.wait_for(future, 1, loop=loop)


    # Stop receiving after 2 messages.
    #await nc.publish("result", b'Im here ')







if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()