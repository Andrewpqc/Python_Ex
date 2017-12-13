import sys,time
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
song_name=sys.argv[1]
print("Searching for {}".format(song_name))
driver=webdriver.Chrome()
driver.get('http://www.kugou.com')

#酷狗首页的搜索框
search_input_elem=driver.find_element_by_xpath("//input[@type='text']")
search_input_elem.send_keys(song_name,Keys.RETURN)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"song_name"))
)

song_elems=driver.find_elements_by_class_name("song_name")


if len(song_elems)==0:
    print("Sorry,there is no song you want!")
    driver.quit()
else:
    for index,song_elem in enumerate(song_elems):
        print(index+1,song_elem.get_attribute("title").strip())

choice = int(input("Which number do you want? Please give me the number:"))

if choice!=0:
    song_elems[choice-1].click()
    real_song_name=song_elems[choice-1].get_attribute("title").strip()
    # WebDriverWait(driver,5).until(
    #     EC.title_contains
    # )

    #等待新窗口加载完成
    time.sleep(3)

    #切换到新窗口
    current_window=driver.current_window_handle
    windows=driver.window_handles
    for window in windows:
        if window==current_window:continue
        else:
            driver.switch_to_window(window)

    song_url=driver.find_element(By.ID,"myAudio").get_attribute('src')
    request.urlretrieve(song_url,"{}.{}".format(real_song_name,song_url.split(".")[-1]))
    request.urlcleanup()
    driver.quit()
    print("Successed!")

