from pynput.mouse import Button, Controller
from PIL import Image
import easyocr
import pyautogui
import os
import time
import shutil

# Setup
shutil.rmtree('images')
os.makedirs('images')
f = open('script.txt', 'w')
f.close()
f = open('script.txt', 'at')

mouse = Controller()
reader = easyocr.Reader(['en', 'en'])

# Add a little more to the top left
top = 477
left = 121
bottom = 3443
right = 1983

time.sleep(5)


# Collecting the messages

def addMessage():
    pass


for scroll in range(1):

    '''
    # Get initial screenshot
    current = pyautogui.screenshot()
    current.save('current.png')

    # Crop so its only the messages section
    im = Image.open('current.png')
    tmp = im.crop((top, left, bottom, right))
    os.remove('current.png')
    tmp.save('current.png')
    '''

    results = reader.readtext('current.png')
    res = [results[x] for x in range(len(results))]

    realMessages = []
    currentText = []


    def addMessage(arr):
        if arr:
            print(arr)
            totalText = ''
            for y in arr:
                totalText += y[1] + ' '
            realMessages.append([[arr[0][0][0], arr[-1][0][2]], totalText])


    def validMessage(start, end):
        if (end - start) >= 25:
            return False
        return True


    for x in range(len(res)):
        text = res[x][1]
        if validMessage(res[x][0][0][1], res[x][0][2][1]):  # only date
            addMessage(currentText[:-1])
            currentText = []
        elif '2/20/2021' in text:  # Text and date
            addMessage(currentText)
            currentText = []
        elif int(res[x][0][0][0]) == res[x][0][0][0]:
            currentText.append(res[x])

    addMessage(currentText)

    for i in range(len(realMessages)):
        topLeftCord = realMessages[i][0][0]
        bottomRightCord = realMessages[i][0][1]
        text = realMessages[i][1]
        f.write(text + '\n')
        print('hello')
        print(topLeftCord, bottomRightCord, text)


        im = Image.open('current.png')
        tmp = im.crop((int(topLeftCord[0]) - 75, int(topLeftCord[1]) - 55, 1400, int(bottomRightCord[1])))
        tmp.save(f'images/message{i}.png')
