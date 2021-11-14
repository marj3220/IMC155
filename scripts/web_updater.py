#!/usr/bin/env python

import asyncio
import websockets

async def update(websocket, path):
    while True:
        data = "Ree"
        await websocket.send(data)
        await asyncio.sleep(1)

def web_updater():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(update, port=5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()