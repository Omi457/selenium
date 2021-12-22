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


### Mapple apple

mapple = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[24]/div/button/img")
mapple.click()
time.sleep(2)

### patient set-up
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[5]/div/button").click()
time.sleep(35)

### start test
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[1]/button").click()



## gender

randongen = random.randint(1,2)
if randongen == 1 :
    male = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/button[1]")
    male.click()
    time.sleep(1)
else: 
    female = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/button[2]")
    female.click()
    time.sleep(1)



###   level 

randomlevel = random.randint(1,3)
if randomlevel == 1:
    level1 = driver.find_element_by_xpath("/html/body/div/div/button[1]")
    level1.click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/button[1]").click()        #### how  to play                      
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/button").click()
    time.sleep(20)

if randomlevel == 2:
    level2 = driver.find_element_by_xpath("/html/body/div/div/button[2]")
    level2.click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/button[1]").click()        #### how  to play                      
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/button").click()
    time.sleep(45)

if randomlevel == 3:
    level3 = driver.find_element_by_xpath("/html/body/div/div/button[3]")
    level3.click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/button[1]").click()        #### how  to play                      
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[5]/button").click()
    time.sleep(70)

#### After godot end

driver.find_element_by_xpath("/html/body/div/div/div[2]/div[6]/button[1]").click()
driver.find_element_by_xpath("/html/body/div/div/div[3]/button").click()
driver.quit()
