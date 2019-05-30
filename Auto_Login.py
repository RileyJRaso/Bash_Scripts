#!/usr/bin/env python3

import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

#gets all needed information from the system
UserName_String = sys.argv[1]
password_String = sys.argv[2]
Website_String = sys.argv[3]

#opens Chrome to website given by System
current_browser = webdriver.Chrome(executable_path='/Users/rileyraso/Desktop/Bash Scripts/Python_Installs/chromedriver')
current_browser.get((Website_String))

#Finds Form inputs and copies the information given by system
username = current_browser.find_element_by_id("username")
username.send_keys(UserName_String)
password = current_browser.find_element_by_id("password")
password.send_keys(password_String)
#submits the username and password to the form
signInButton = current_browser.find_element_by_name("submit")
signInButton.click()

exit(0)
