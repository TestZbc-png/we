from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8CA.html")

username = driver.find_element_by_id('userA')
username.send_keys('aa')
sleep(2)
# 键盘backspce键删除一个字符
username.send_keys(Keys.BACK_SPACE)
sleep(2)
username.send_keys(Keys.CONTROL, 'c')
sleep(2)
pwd = driver.find_element_by_id('passwordA')
pwd.send_keys(Keys.CONTROL, 'v')

sleep(3)
driver.quit()