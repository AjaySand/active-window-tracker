from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
from time import sleep, time
import math
import pickle
from datetime import datetime
from os import path, getenv
import pprint


DEBUG = getenv('DEBUG')


def getForegroundWindowTitle() -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    return buf.value if buf.value else None


def getFileName():
    dateStr = datetime.today().strftime('%Y-%m-%d')
    fileName = 'window-titles-' + dateStr + '.pkl'
    return fileName


def saveToFile(windowTitles):
    fileName = getFileName()
    with open(fileName, 'wb') as fp:
        pickle.dump(windowTitles, fp)
        print('dictionary saved successfully to file')


def loadFromFile(windowTitles):
    fileName = getFileName()
    if path.exists(fileName):
        with open(fileName, 'rb') as fp:
            windowTitles = pickle.load(fp)
            print('dictionary loaded successfully from file')
            # pprint.pprint(windowTitles)
    return windowTitles


def gatherWindowTitles(windowTitles):
    startTime = time()
    windowTitles = loadFromFile(windowTitles)

    while True:
        title = getForegroundWindowTitle()
        if title:
            if title in windowTitles:
                windowTitles[title] += 1
            else:
                windowTitles[title] = 1

        if DEBUG:
            print(title)


        sleep(1)

        elapsed = math.floor(time() - startTime)

        if DEBUG and elapsed % 10 == 0:
            pprint.pprint(windowTitles)

        if elapsed % 30 == 0:
            saveToFile(windowTitles)


def run():
    windowTitles = {}
    gatherWindowTitles(windowTitles)