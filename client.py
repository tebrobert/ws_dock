#!/usr/bin/env python

"""Client using the asyncio API."""

MY_URI = "ws://localhost:4000"
#MY_URI = "ws://...:..."

import asyncio
from websockets.asyncio.client import connect
from datetime import datetime

async def receiver(websocket):
    while True:
        message = await websocket.recv()
        print(datetime.now(), "got", message)

async def getter(websocket):
    while True:
        message = input("Your message:")
        await websocket.send(message)
        await asyncio.sleep(0.1)


async def hello():
    async with connect(MY_URI) as websocket:
        t1 = asyncio.create_task(receiver(websocket))
        t2 = asyncio.create_task(getter(websocket))
        await t1, t2

if __name__ == "__main__":
    asyncio.run(hello())
