import asyncio
import nats
from nats.errors import TimeoutError

async def main():
    nc = await nats.connect("nats")

    # Create JetStream context.
    js = nc.jetstream()

    # Persist messages on 'foo's subject.

    for i in range(0, 10):
        ack = await js.publish("result", f"hellt: {i}".encode())
        print(ack)

if __name__ == '__main__':
    asyncio.run(main())