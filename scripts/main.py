from threading import Thread
from alert_sender import AlertSender
from server import web_server
from web_updater import web_updater


if __name__ == "__main__":
    threads = [Thread(target=web_updater), Thread(target=web_server)]
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    