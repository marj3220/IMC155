#!/usr/bin/env python

import asyncio
import websockets
from Master_comm import pi_arduino_communicator

def web_updater():
    """Infinite loop that generates the WebSocket server"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(pi_arduino_communicator, port=5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()