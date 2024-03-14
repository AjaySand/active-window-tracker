from tracker import run
from server import run as serverRun
from multiprocessing import Process
from os import getenv


DEBUG = getenv('DEBUG')


if __name__ == '__main__':
    application_tracker = Process(target=run)
    application_tracker.start()

    application_server = Process(target=serverRun)
    application_server.start()

    # application_tracker.join()
    # application_server.join()