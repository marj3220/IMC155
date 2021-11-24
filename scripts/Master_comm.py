import time
import struct
from scripts.algo_decision import compute_data
from smbus import SMBus

slave = [0x08]               # array of slave addresses
nb_slaves = len(slave)      # amount of slave devices
nb_sensors = 4              # amount of sensors per slave device

bus = SMBus(1)

temperature_matrix = [[0 for c in range(nb_sensors)] for r in range(nb_slaves)]     # array of all temperature values

def readSensorSlave(i,j):
    print("Sending msg")
    bus.write_byte(slave[i],j)
    return

def receiveFromSlave(i,j):
    print("receiving from slave")
    temperature = 0.00
    dataString = ""
    block = bus.read_i2c_block_data(slave[i],j,7)
    for c in range(len(block)):
        dataString = dataString + chr(block[c])
    temperature = float(dataString)
    return temperature

def pi_arduino_communicator():
    while True:
        for i in range(nb_slaves):
            print("Asking for data")
            for j in range(nb_sensors):
                #readSensorSlave(i,j)
                time.sleep(0.1)
                temperature_matrix[i][j] = receiveFromSlave(i,j)
        print(temperature_matrix)
        print()    
        compute_data(temperature_matrix)
        time.sleep(3)
