import time
from selenium import webdriver
from sys import platform
import pyautogui


if 'linux' in platform:
    driver = webdriver.Chrome('venv/bin/chromedriver')
else:
    driver = webdriver.Chrome('venv/bin/chromedriver.exe')


driver.get('https://mauriciopereyra.com')





for a in range(20):
    offset = {'x':-24,'y':-150}
    screen_position = pyautogui.position()
    browser_position = driver.get_window_position()

    final_position = {
        'x':screen_position.x-browser_position['x']+offset['x'],
        'y':screen_position.y-browser_position['y']+offset['y']
        }

    element = driver.execute_script('return document.elementFromPoint({}, {});'.format(final_position['x'],final_position['y']))
    if element:
        print(element.get_attribute("class"))
        print(final_position)
        driver.execute_script("arguments[0].style.display = 'none';", element)
    time.sleep(3)