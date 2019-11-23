import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("file://C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8CA.html")
time.sleep(3)
driver.find_element_by_link_text("访问 新浪 网站").click()
password = driver.find_element_by_id('passwordA')
password1 = driver.find_element_by_name('passwordA')
tel = driver.find_element_by_class_name('telA')
driver.find_element_by_tag_name('input').send_keys('admin')
driver.find_element_by_xpath('//*[@contains[@属性,"属性值任意部分内容"]]')
driver.find_element_by_xpath('//*[text()="全部信息"]')

# //a[contains(text(),'部分信息')]
time.sleep(3)
driver.close()
time.sleep(3)
driver.quit()

