from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import names    



driver = webdriver.Chrome(executable_path = "F:\selenium\chromedriver.exe")  
driver.maximize_window()
driver.get("http://127.0.0.1:5000/KyaLiveViz")
time.sleep(2)


######## KYA LIVEVIZ ######

# driver.get("http://127.0.0.1:5000/KyaLiveViz")
# time.sleep(5)


# HOME
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[1]/button").click()
time.sleep(3)

#  Regestration Page
# Name
a = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[1]/div/input")
b = names.get_full_name()
a.send_keys(b)
time.sleep(3)



###   Gender
randongen = random.randint(1,3)
if randongen == 1 :
    male = driver.find_element_by_id("imagepic1")
    male.click()
    time.sleep(3)
if randongen == 2: 
    female = driver.find_element_by_id("imagepic2")
    female.click()
    time.sleep(3)
if randongen == 3:
    other = driver.find_element_by_id("imagepic3")
    other.click()
    time.sleep(3)


# Date of Birth
# driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[3]/div/input").send_keys("23-10-2021")
# time.sleep(5)


def random_dob_generator():
    day = str(random.randint(1, 30))
    print(day)
    month = str(random.randint(1, 12))
    print(month)
    year = str(random.randint(1950,  2012))
    print(year)
    return '{}-{}-{}'.format(day,month,year)

dob = random_dob_generator()
dobnum = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[3]/div/input")
dobnum.clear()
dobnum.send_keys(str(dob))
time.sleep(3)




### Hight 

hight = random.randint(1,2)
if hight == 1:
             # #  Hight cm
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[4]/div/button[1]/div").click()
    start = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[5]/div/div/div/div[4]/div[1]/div/input")
    end = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[5]/div/div/div/div[4]/div[1]/div/p")
    try:                                  
        ActionChains(driver).drag_and_drop(start, end).perform()
    except:
        pass
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[5]/div/div/div/div[2]/div/button").click()
else: 
        # Hight ft-inc
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[4]/div/button[1]/div").click()
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[5]/div/div/div/ul/li[2]/a").click()
    feet_source = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[5]/div/div/div/div[4]/div[2]/div/input")
    feet_target = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[5]/div/div/div/div[4]/div[2]/div/p")
    try:
        ActionChains(driver).drag_and_drop(feet_source, feet_target).perform()
    except:
        pass
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[5]/div/div/div/div[3]/div/button").click()
    time.sleep(1)


# Weight
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[4]/div/button[2]/div").click()
weight_source = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[6]/div/div/div/div[3]/div/div/input")
weight_target = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[6]/div/div/div/div[3]/div/div/p")
try:
    ActionChains(driver).drag_and_drop(weight_source, weight_target).perform()
except:
    pass                       
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[6]/div/div/div/div[2]/div/button").click()
time.sleep(5)

# Mobile 
# driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[7]/div/input").send_keys("9920181823")
# time.sleep(5)
def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}{}{}'.format(first, second, last)

contact_number = random_phone_num_generator()
cnum = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[7]/div/input")
cnum.clear()
cnum.send_keys(str(contact_number))
time.sleep(3)




# Email-ID
d = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[8]/div/input")

# y = str(b.split()[0])
# z = str(b.split()[1])
# v = y + z + "@gmail.com"
# d.send_keys(v)
d.send_keys(b.split()[0] + b.split()[1] + "@gmail.com" )



### Terms and condition
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/div/form/div/div/div/div[9]/div/div/label/span[2]").click()
time.sleep(5)


# Next
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[2]/button[2]").click()
time.sleep(5)

# Next stepp cop movement
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[3]/button[2]").click()
time.sleep(80)

### After cop movement   ##Next step1
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[3]/button[3]").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/fieldset[3]/button[3]").click()
time.sleep(1)
driver.quit()


