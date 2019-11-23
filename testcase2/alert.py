from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8CA.html")
# driver.find_element_by_id('confirma').click()
# driver.find_element_by_id('alerta').click()
driver.find_element_by_id('prompta').click()
sleep(2)
alert = driver.switch_to.alert
print(alert.text)
# alert.accept()
alert.dismiss()
driver.find_element_by_id('userA').send_keys('admin')
sleep(1)
driver.quit()