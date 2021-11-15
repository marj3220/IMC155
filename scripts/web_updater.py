#!/usr/bin/env python

import asyncio
import websockets
import random

from algo_decision import DATA

async def producer():
    """Coroutine that produces the data that is destined to be sent to the webpage"""
    while True:
        # Produce a random number and send it to the consumer
        r = random.randint(0, 20)
        # Wait here until next() is called
        yield r


async def update(websocket, path):
    """Coroutine that sends data through websocket"""
    while True:
        if DATA:
            data = DATA.pop()
            await websocket.send(data)
        await asyncio.sleep(5)

def web_updater():
    """Infinite loop that generates the WebSocket server"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(update, port=5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()