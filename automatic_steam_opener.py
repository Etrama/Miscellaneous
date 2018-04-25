# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 21:47:29 2018

@author: kmoudgalya
"""
"""
ABANDONED because:
    1.The file explorer does not always open in full screen
    2.The move to click timing is not streamlining properly.

"""
import pyautogui
import time

pyautogui.moveTo(508L, 701L,duration = 1)
pyautogui.click()
pyautogui.moveTo(83L, 628L, duration = 1)
pyautogui.click()
pyautogui.moveTo(1117L, 155L,duration = 1)
pyautogui.click()
pyautogui.typewrite('steam\n')
time.sleep(50)
pyautogui.doubleClick(x=181L, y=199L)
pyautogui.doubleClick(x=187L, y=257L)
pyautogui.doubleClick(x=187L, y=257L)