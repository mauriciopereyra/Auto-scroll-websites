import time
from typing import final
from selenium import webdriver
from sys import platform
import pyautogui
from pynput import keyboard


if 'linux' in platform:
    driver = webdriver.Chrome('venv/bin/chromedriver')
else:
    driver = webdriver.Chrome('venv/bin/chromedriver.exe')


driver.get('https://mauriciopereyra.com')

elements_to_remove = []
scroll_speed = 1

def on_press(key):
    global scroll_speed
    try:
        k = key.char 
    except:
        k = key.name
    if k == 'd':  
        remove_element()
    elif k == '+':
        scroll_speed += 1
    elif k == '-':
        scroll_speed -= 1
    elif k == '0':
        scroll_speed = 0
        keep = 'r'

def final_position():
    offset = {'x':-24,'y':-150}
    screen_position = pyautogui.position()
    browser_position = driver.get_window_position()
    return {
        'x':screen_position.x-browser_position['x']+offset['x'],
        'y':screen_position.y-browser_position['y']+offset['y']
        }
            

def remove_element():
    position = final_position()
    element = driver.execute_script('return document.elementFromPoint({}, {});'.format(position['x'],position['y']))
    elements_to_remove.append(element)

    if element: # If valid element found
        driver.execute_script("arguments[0].style.display = 'none';", element)


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread


y = 0
while True:
    driver.execute_script("window.scrollTo({},{})".format(0,y)) 
    print(scroll_speed)
    print(y)
    y+=scroll_speed
    # y+=1
    time.sleep(0.1)