import time
import struct
from algo_decision import compute_data
from smbus import SMBus

DATA = {}
slave = [0x08]               # array of slave addresses
nb_slaves = len(slave)      # amount of slave devices
nb_sensors = 4              # amount of sensors per slave device

bus = SMBus(1)

temperature_matrix = [[0 for c in range(nb_sensors)] for r in range(nb_slaves)]     # array of all temperature values

cadeau = [[0 for c in range(2)] for r in range(2)]

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
    return temperature

def pi_arduino_communicator():
    while True:
        for i in range(nb_slaves):
            #print("Asking for data")
            for j in range(nb_sensors):
                #readSensorSlave(i,j)
                time.sleep(0.25)
                temp = receiveFromSlave(i,j)
                if (temp != None):
                    temperature_matrix[i][j] = temp
        k = 0
        for i in range(2):
            for j in range(2):
                cadeau[i][j] = temperature_matrix[0][k]
                k=k+1
        print(cadeau)
        print()    
        global DATA
        DATA = compute_data(cadeau)
        time.sleep(3)
