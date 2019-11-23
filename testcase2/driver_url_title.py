from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print("标题是===={}".format(driver.title))
print("地址是===={}".format(driver.current_url))
sleep(2)
driver.quit()

