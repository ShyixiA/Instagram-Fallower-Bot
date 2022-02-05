from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'Enter İnstagram Username'
password = 'Enter İnstagram Password'





browser = webdriver.Chrome()

browser.get('https://www.instagram.com/')
time.sleep(2)
username_input = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input') #won't work if instagram updates xpaths
password_input = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input') #won't work if instagram updates xpaths

username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
time.sleep(3)

# First NOTIFICATION
notNow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()  #won't work if instagram updates xpaths

# Second NOTIFICATION
notNow_2 = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click() #won't work if instagram updates xpaths
time.sleep(2)

#show all of them button
notNow_3 = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click() #won't work if instagram updates xpaths
time.sleep(2)

#follow-up cycle
for i in range(3):
	for i in range(10):
		browser.find_element_by_xpath("//button[text()='Takip Et']")\
		.click() #"Takip Et"The button should be written differently in each language.
		time.sleep(3)
browser.refresh()

#cancel
notNow_3 = browser.find_element_by_xpath(
    "/html/body/div[6]/div/div/div/div[3]/button[2]").click()  #won't work if instagram updates xpaths


