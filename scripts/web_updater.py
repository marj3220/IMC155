#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets

async def update(websocket, path):
    while True:
        data = "Ree"
        await websocket.send(data)
        await asyncio.sleep(1)

start_server = websockets.serve(update, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()