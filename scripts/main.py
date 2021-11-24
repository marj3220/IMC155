from threading import Thread
from server import web_server
from web_updater import web_updater
from Master_comm import pi_arduino_communicator


if __name__ == "__main__":
    threads = [Thread(target=pi_arduino_communicator), Thread(target=web_updater), Thread(target=web_server)]
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    