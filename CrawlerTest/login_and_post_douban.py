from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
driver=webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
#driver=webdriver.Chrome()
print("go!")
try:
    driver.get("http://www.douban.com")
    driver.get_screenshot_as_file("douban.png")
    username = driver.find_element_by_name("form_email")
    password = driver.find_element_by_name("form_password")
    submit=driver.find_element_by_class_name("bn-submit")
    username.send_keys("13636038496")
    password.send_keys("pqc19960320")
    submit.click()
    #显式等待
    WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"editor"))
    )
    print("entered douban!")
    text=driver.find_element_by_id("isay-cont")
    text.click()
    text.send_keys("this is a small test for selenium")
    driver.find_element_by_id("isay-submit").click()
    sleep(1)
    driver.get_screenshot_as_file("douban.png")
    print("down!")
finally:
    driver.close()
