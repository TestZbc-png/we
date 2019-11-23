"""
因为验证码是实施获取的，可以减少恶意请求的数量，防止系统瘫痪，同时增加系统安全性
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 添加cookie信息

value = driver.add_cookie({"name":"BDUSS",
                   "value":"xGQjlJVE5qN"
                           "zBBMGdpQjhMRE"
                           "RVMExIcDNzYmZOeGZKZnN"
                           "0dVo4WjFIRjhpfk5kRVFBQUFBJC"
                           "QAAAAAAAAAAAEAAAD0FsyRsbG3vcDH1"
                           "d~Ezb~LAAAAAAAAAAAAAAAAAAAAAAAAAA"
                           "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                           "AAAAAHz-y118~stdMG"})

print("值为== {}".format(value))
driver.refresh()
sleep(3)
driver.quit()
print(123132)
