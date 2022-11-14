import asyncio
import nats
from nats.errors import TimeoutError

async def main():
    nc = await nats.connect("nats")

    # Create JetStream context.
    js = nc.jetstream()

    # Persist messages on 'foo's subject.
    await js.add_stream(name="que", subjects=["result"], )

    # Create ordered consumer with flow control and heartbeats
    # that auto resumes on failures.


    osub = await js.subscribe("result",durable="worker")
    data = bytearray()

    while True:
        try:
            msg = await osub.next_msg()
            print(msg.data)
            await msg.ack()
        except TimeoutError:
            print("All data in stream:", len(data))


    
if __name__ == '__main__':
    asyncio.run(main())