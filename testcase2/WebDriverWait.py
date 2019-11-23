"""
需求：打开注册A等待页面，完成以下操作
    1).使用显式等待定位用户名输入框，如果元素存在，就输入admin
"""
from selenium import webdriver
from time import sleep
# 导包
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8CA.html')
element = WebDriverWait(driver, 10).until(lambda x : x.find_element_by_id('userA'))
element.send_keys("admin")
# 初始化等待对象并调用方法

# 注意:
# 1. 显示等待类初始化默认传递三个参数, 分别是浏览器对象, 超时时长, 方法执行间隔时间(默认 0.5s, 可以不传)
# 2. until()需要传入方法作为参数, 元素定位返回的是元素对象, 因此使用匿名函数包装成可以当参数传递的方法
# 2. 当使用显示等待包装元素定位方法时, 智能提示失效, 需要手写元素操作方法

sleep(3)
driver.quit()
