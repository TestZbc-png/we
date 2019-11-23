from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8CA.html")
user = driver.find_elements_by_link_text('新浪')[0]
print("user=" + user.text)
print(user.get_attribute('href'))
sleep(2)
driver.quit()