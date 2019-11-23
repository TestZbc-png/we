from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/page/%E6%B3%A8%E5%86%8CA.html')
# 准备js代码
js_down = "window.scrollTo(0,1000)" # 向下
sleep(2)
js_up = "window.scrollTo(0,0)"
# 调用 js 代码
driver.execute_script(js_down)
sleep(2)
driver.execute_script(js_up)
sleep(2)
driver.quit()