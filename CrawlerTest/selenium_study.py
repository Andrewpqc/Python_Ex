# # from selenium import webdriver
# # import time
# # driver=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
# # # 使用浏览器请求页面
# # driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# # # 加载3秒，等待所有数据加载完毕
# # time.sleep(3)
# # # 通过id来定位元素
# # # .text获取元素的文本数据
# # print(driver.find_element_by_id('content').text)
# #
# # # 关闭浏览器
# # driver.close()
#
#
# # #静态请求页面
# # url="http://pythonscraping.com/pages/javascript/ajaxDemo.html"
# # url2="https://movie.douban.com/tag/#/"
# #
# # # url4="https://s.taobao.com/search?868.53.7e9aadc4MWgiUp&q=T恤男&acm=lb-zebra-241046-2071168.1003.4.1812194&scm=1003.4.lb-zebra-241046-2071168.OTHER_14952591088251_1812194"
# #
# # import urllib.request
# # url3="https://s.taobao.com/search?spm=a21wu.241046-us.6977698868.53.7e9aadc4MWgiUp&q=" \
# #      ""+urllib.request.quote("T恤男")+"&acm=lb-zebra-241046-2071168.1003.4.1812194&scm=1003.4." \
# #     "lb-zebra-241046-2071168.OTHER_14952591088251_1812194"
# # file=urllib.request.urlretrieve(url3,filename="1.html")
# # # print(file.read())
#
# # from selenium import webdriver
# # import time
# #
# # driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
# # driver.get("https://world.taobao.com")
# # time.sleep(7)
# # print(driver.page_source)#获取页面的html
# # driver.get_screenshot_as_file("2.png") # 获取页面截图
# #
# # driver.close()
#
#
# # #selenium匿名
# # from selenium import webdriver
# # #假定9999端口开启tor服务
# # service_args = ['--proxy=localhost:9999', '--proxy-type=socks5', ]
# # driver =webdriver.PhantomJS(executable_path="phantomjs.exe",service_args=service_args)
# # driver.get("target_url")
# # print(driver.page_source)
# # driver.close()
#
# # from selenium import webdriver
# # browser=webdriver.Chrome()
# # browser.get('https://www.baidu.com')
# # print(browser.page_source)
#
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from time import sleep
# print('asdf')
# driver = webdriver.Chrome()
# # driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
# # driver = webdriver.Firefox()
# # driver = webdriver.Remote()
# driver.get("https://www.douban.com")
#
# username = driver.find_element_by_name("form_email")
# password = driver.find_element_by_name("form_password")
# submit=driver.find_element_by_class_name("bn-submit")
# username.send_keys("13636038496")
# password.send_keys("pqc19960320")
# submit.send_keys(Keys.RETURN)
#
# sleep(3)
# text=driver.find_element_by_id("isay-cont")
# text.click()
# text.send_keys("this is a small test for selenium")
# driver.find_element_by_id("isay-submit").click()
#
# # elem.send_keys("肖生克的救赎")
# # elem.send_keys(Keys.RETURN)
# # sleep(5)
# # print(driver.page_source)
# # driver.get_screenshot_as_file("2.png") # 获取页面截图
# # driver.quit()
#
#



