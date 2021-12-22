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

### shrinking 
shrinking = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[6]/div/button/img[1]")
shrinking.click()
time.sleep(3)


### Gender
randongen = random.randint(1,2)
if randongen == 1 :
    male = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/button[1]")
    male.click()
    time.sleep(1)
else :
    female = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/button[2]")
    female.click()
    time.sleep(1)


####  level


randomlevel = random.randint(1,7)
if randomlevel == 1:
    level1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/button")
    level1.click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div/button").click()                         ## skip
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[5]/button").click()
    time.sleep(100)
if randomlevel == 2:
    level2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/button")
    level2.click() 
    time.sleep(4)     
    driver.find_element_by_xpath("/html/body/div/button").click()                         ## skip
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[5]/button").click()
    time.sleep(100)
if randomlevel == 3:
    level3 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[3]/button")
    level3.click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div/button").click()                         ## skip
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[5]/button").click()
    time.sleep(100)
if randomlevel == 4:
    level1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[5]/button")
    level1.click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div/button").click()                         ## skip
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[5]/button").click()
    time.sleep(100)
if randomlevel == 5:
    level1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[6]/button")
    level1.click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div/button").click()                         ## skip
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[5]/button").click()
    time.sleep(100)
if randomlevel == 6:
    level1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[6]/button")
    level1.click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div/button").click()                         ## skip
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[5]/button").click()
    time.sleep(100)
if randomlevel == 7:
    level1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[7]/button")
    level1.click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div/button").click()                         ## skip
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[5]/button").click()
    time.sleep(100)


#### After godot end 

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[7]/button").click()
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[8]/button").click()
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[9]/button").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/button").click()
driver.quit()
