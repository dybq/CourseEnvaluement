import time
import json
from selenium import webdriver

right = ["非常同意", "一定会", "对我帮助大", "4次以上", "4小时以上", "每次", ">12小时","非常同意 ", "一定会 ", "对我帮助大 ", "4次以上 ", "4小时以上 ", "每次 ", ">12小时 "]
a = open("user.txt")
data = a.readlines()
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
time.sleep(5)
# 登陆

mainPage = driver.current_window_handle
print(mainPage)
for page in range(1, 11):

    p = driver.find_element_by_xpath(f'//*[@id="myTaskContainer"]/table/tbody[2]/tr[{page}]/td[7]/a')

    driver.execute_script("arguments[0].scrollIntoView();", p)
    p.click()
    time.sleep(3)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    driver.maximize_window()
    tags = driver.find_elements_by_tag_name("input")
    # 获取所有可点击
    atags = driver.find_elements_by_xpath('//*[@id="divHeader"]/div[3]/div/ul/li')
    for a in atags:
        # 点击各个老师

        driver.execute_script('arguments[0].scrollIntoView();', a)

        a.click()

        for i in tags:
            try:
                driver.execute_script('arguments[0].removeAttribute(\"style\")', i)
                good = eval(str(i.get_attribute("options")))
                print(good['Title'])
                for j in right:

                    if j == good['Title']:

                        i.click()
                        time.sleep(1)
                        break

                driver.execute_script("arguments[0].scrollIntoView();", i)
            except:
                driver.execute_script("arguments[0].scrollIntoView();", i)

                continue
    driver.find_element_by_xpath('//*[@id="btnSave"]').click()
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[4]/button[1]').click()
    time.sleep(5)
    driver.close()
    driver.switch_to.window(mainPage)
