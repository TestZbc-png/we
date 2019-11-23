from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
sleep(2)
current_handle = driver.current_window_handle
# print("当前句柄值为：" + current_handle)
# 点击注册 A 页面链接
driver.find_element_by_link_text('注册A页面').click()
sleep(2)
# 获取所有窗口句柄
handles = driver.window_handles
print("其他窗口句柄值= {}".format(handles) )
driver.switch_to.window(handles[1])
# 循环遍历， 条件判断获取新窗口句柄，完成创窗口切换
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')
driver.switch_to.window(handles[0])
# for i in handles:
#     if i != current_handle:
#         # 切换窗口
#         driver.switch_to.window(1)
#
#
#         # 填写注册信息
#         driver.find_element_by_id('userA').send_keys('admin')
#         driver.find_element_by_id('passwordA').send_keys('123456')


sleep(3)
driver.quit()