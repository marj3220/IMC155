#!/usr/bin/env python

import asyncio
import websockets
import json

from Master_comm import pi_arduino_communicator

async def update(websocket, path):
    """Coroutine that sends data through websocket"""
    unchecked_data = pi_arduino_communicator()
    while True:
        print("In true")
        try:
            checked_data = next(unchecked_data)
            print(checked_data)    
            data = json.dumps(checked_data)
            print("ree")
            print(data)
            await websocket.send(data)
        except StopIteration:
            pass
        await asyncio.sleep(1)

def web_updater():
    """Infinite loop that generates the WebSocket server"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(update, port=5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()