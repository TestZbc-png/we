from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

btn = driver.find_element_by_xpath("//*[@name='tj_briicon']")
# 初始化鼠标对象
action = ActionChains(driver).move_to_element(btn).perform()

sleep(3)
driver.quit()