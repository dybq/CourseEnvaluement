import time
from bs4 import BeautifulSoup
import re
from selenium import webdriver
a=open("user.txt")
data=a.readlines()
a.close()
driver_option = webdriver.ChromeOptions()
#driver_option.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", chrome_options=driver_option, )
driver.get("http://kcpg.pku.edu.cn/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(data[0])
driver.find_element_by_xpath('//*[@id="password"]').send_keys(data[1])
driver.find_element_by_xpath('//*[@id="logon_button"]').click()
time.sleep(3)

mainPage=driver.current_window_handle
print(mainPage)
for page in range(1,11):
    driver.find_element_by_xpath(f'//*[@id="myTaskContainer"]/table/tbody[2]/tr[{page}]/td[7]/a').click()
    #pages=driver.page_source
    time.sleep(3)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    driver.maximize_window()
    tags=driver.find_elements_by_class_name("radioFivelabel backpo")

    for i in tags:
        try:
            print(i.text)
            i.click()
        except:
            continue
    time.sleep(3)
    driver.close()
    driver.switch_to_window(mainPage)
