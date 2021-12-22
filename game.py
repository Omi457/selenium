from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


driver = webdriver.Chrome(executable_path = "F:\selenium\chromedriver.exe")  
driver.maximize_window()
driver.get("http://127.0.0.1:5000/loginUser")
time.sleep(2)


## Game login page
driver.find_element_by_xpath("/html/body/div[1]/div/form/div/div[3]/div/input").send_keys("lauserone")
driver.find_element_by_xpath("/html/body/div[1]/div/form/div/div[6]/div/input").send_keys("qwerty1234")
driver.find_element_by_xpath("/html/body/div[1]/div/form/div/div[7]/button/img").click()
time.sleep(2)


### patient page
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/button/img").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[3]").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[3]/button[4]").click()
time.sleep(2)


# ### mat set-up
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[4]/div/button/img[1]").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/label[1]/span").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/label[2]/span").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[2]/div/button").click()
time.sleep(7)
driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div/div[3]/button").click()
time.sleep(2)






# ### Square game
# square = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[12]/div/button/img")
# square.click()
# time.sleep(1)
# driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[12]/div/div/div/div/div[2]/div[1]/button").click()
# time.sleep(70)
# driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()


# # ### Star game   /html/body/div/div[4]/div[2]/div[14]/div/button/img
# star = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[14]/div/button/img")
# star.click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[14]/div/div/div/div/div[2]/div[1]/button").click()
# time.sleep(70)
# driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()


# ### Hour glass game                   
# Hour = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[16]/div/button/img")
# Hour.click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[16]/div/div/div/div/div[2]/div[1]/button").click()
# time.sleep(80)
# driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()


# ### circle game
circle = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[18]/div/button/img")
circle.click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[18]/div/div/div/div/div[2]/div[1]/button").click()
time.sleep(70)
driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()


### zig zag
# zig = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[20]/div/button/img")
# zig.click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[20]/div/div/div/div/div[2]/div[1]/button").click()
# time.sleep(70)
# driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()


### spiral game
# spiral = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[22]/div/button")
# spiral.click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[22]/div/div/div/div/div[2]/div[1]/button").click()
# time.sleep(70)
# driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()


## 8 shape                               
# eight = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[26]/div/button/img")
# eight.click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[26]/div/div/div/div/div[2]/div[1]/button").click()
# time.sleep(70)
# driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()


### IF conditon for shape game
# click1 =["/html/body/div/div[4]/div[2]/div[12]/div/button/img","/html/body/div/div[4]/div[2]/div[14]/div/button/img","/html/body/div/div[4]/div[2]/div[16]/div/button/img","/html/body/div/div[4]/div[2]/div[18]/div/button/img","/html/body/div/div[4]/div[2]/div[20]/div/button/img","/html/body/div/div[4]/div[2]/div[26]/div/button/img"]
# start =["/html/body/div[1]/div[4]/div[2]/div[12]/div/div/div/div/div[2]/div[1]/button","/html/body/div[1]/div[4]/div[2]/div[14]/div/div/div/div/div[2]/div[1]/button","/html/body/div[1]/div[4]/div[2]/div[16]/div/div/div/div/div[2]/div[1]/button","/html/body/div[1]/div[4]/div[2]/div[18]/div/div/div/div/div[2]/div[1]/button","/html/body/div[1]/div[4]/div[2]/div[20]/div/div/div/div/div[2]/div[1]/button","/html/body/div[1]/div[4]/div[2]/div[26]/div/div/div/div/div[2]/div[1]/button"]

# object = zip(click1, start)
# for element1, element2 in object:
#     driver.find_element_by_xpath(element1).click()
#     time.sleep(2)
#     driver.find_element_by_xpath(element2).click()
#     time.sleep(90)
#     driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button").click()

# driver.quit()










