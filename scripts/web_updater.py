#!/usr/bin/env python

import asyncio
import websockets
from algo_decision import DATA
import json

async def update(websocket, path):
    """Coroutine that sends data through websocket"""
    while True:
        if DATA:
            data = json.dumps(DATA.pop())
            await websocket.send(data)
        await asyncio.sleep(5)

def web_updater():
    """Infinite loop that generates the WebSocket server"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(update, port=5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()