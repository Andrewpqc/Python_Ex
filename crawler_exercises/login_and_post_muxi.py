from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
# driver.get("http://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=%E5%A6%82%E6%9E%9C%E8%BF%99%E9%83%BD%E4%B8%8D%E7%AE%97%E7%88%B1")
# songs_elems=driver.find_elements_by_class_name("song_name")
# print(songs_elems)
driver=webdriver.Chrome()
# driver=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get("http://auth.muxixyz.com/login/")
username_elem=driver.find_element_by_id("username")
username_elem.send_keys("阿超")
password_elem=driver.find_element_by_id("password")
password_elem.send_keys("pqc19960320")
print("---------")
driver.find_element_by_id("submit").click()
print("000000000000")
time.sleep(2)
WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//a[@href='http://share.muxixyz.com/']"))
print("aaaaaaaaaaa")
with open('1.html','w') as f:
    f.write(driver.page_source)
driver.find_element_by_xpath("//a[@href='http://share.muxixyz.com/']").click()
print("kkkkkkkkkkkkkk")
WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//span[@class='mdl-button__ripple-container']"))
driver.find_element_by_xpath("//a[@href='/send']").click()
WebDriverWait(driver,3).until(lambda x:x.find_element_by_id("title"))
title=driver.find_element_by_id("title")
title.click()
title.send_keys("分享")

category=driver.find_element_by_class_name("mdl-radio__ripple-container mdl-js-ripple-effect mdl-ripple--center")
category.click()

content=driver.find_element_by_id("flask-pagedown-share")
content.click()
content.send_keys("![hhh](http://www.baidu.com)")

# driver.quit()