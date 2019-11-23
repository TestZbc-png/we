# 时间戳
"""
因为验证码是实施获取的，可以减少恶意请求的数量，防止系统瘫痪，同时增加系统安全性
"""
import time

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8CA.html")
driver.find_element_by_id('userA').send_keys('admin')
time = time.strftime('%Y%m%d%H%M%S')
driver.get_screenshot_as_file('./info_{}.png'.format(time))
sleep(3)
driver.quit()