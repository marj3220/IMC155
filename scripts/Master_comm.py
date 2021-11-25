import time
from algo_decision import DecisionTaker
from smbus import SMBus
import asyncio
import json

slave = [0x08]               # array of slave addresses
nb_slaves = len(slave)      # amount of slave devices
nb_sensors = 6              # amount of sensors per slave device

bus = SMBus(1)

temperature_matrix = [[0 for c in range(nb_sensors)] for r in range(nb_slaves)]     # array of all temperature values

cadeau = [[0 for c in range(3)] for r in range(2)]

def readSensorSlave(i,j):
    bus.write_byte(slave[i],j)
    return

def receiveFromSlave(i,j):
    temperature = 0.00
    dataString = ""
    try:
        block = bus.read_i2c_block_data(slave[i],j,7)
        time.sleep(0.2)
        for c in range(len(block)):
            dataString = dataString + chr(block[c])
        temperature = float(dataString)
    except IOError:
        temperature = None
        time.sleep(0.5)
    return temperature

async def pi_arduino_communicator(websocket, path):
    decision_taker = DecisionTaker()
    while True:
        for i in range(nb_slaves):
            for j in range(nb_sensors):
                temp = receiveFromSlave(i,j)
                if (temp != None):
                    temperature_matrix[i][j] = temp
        k = 0
        for i in range(2):
            for j in range(3):
                cadeau[i][j] = temperature_matrix[0][k]
                k=k+1   
        data = decision_taker.compute_data(cadeau)
        try: 
            data_to_send = json.dumps(data)
            await websocket.send(data_to_send)
        except StopIteration:
            pass
        await asyncio.sleep(1)
        time.sleep(3)
