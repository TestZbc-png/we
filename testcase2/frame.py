from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
# driver.switch_to.frame('idframe1')
# driver.switch_to.frame(0)
driver.find_element_by_id('userA').send_keys('admin1')
sleep(1)
driver.switch_to.default_content()
sleep(1)
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[1])
# driver.switch_to.frame('myframe2')
# driver.switch_to.frame(1)
driver.find_element_by_id('userB').send_keys('admin2')
sleep(3)

driver.quit()
