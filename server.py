#!/usr/bin/env python

"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve
from datetime import datetime

async def process(websocket):
    async for message in websocket:
        print(datetime.now(), websocket.remote_address, "got", message)
        try:
            result = str(int(message) * 2)
            print(datetime.now(), websocket.remote_address, "sendind", result)
            await websocket.send(result)
        except: pass

async def ad(websocket):
    while True:
        await asyncio.sleep(10)
        await websocket.send("go to our web site!")

async def processConnection(websocket):
    t1 = asyncio.create_task(process(websocket))
    t2 = asyncio.create_task(ad(websocket))
    await t1, t2


async def main():
    async with serve(processConnection, "0.0.0.0", 8080) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
