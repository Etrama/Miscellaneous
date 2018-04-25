# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 15:52:18 2018

@author: kmoudgalya
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
