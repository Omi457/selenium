from selenium import webdriver
import time
#import validators    # validatiors
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages
from selenium.webdriver.support.ui import WebDriverWait   #explicit
import random ####form random integer
import names

driver = webdriver.Chrome(r"D:\chromdriver\chromedriver.exe")

driver.get("http://127.0.0.1:5000/loginUser")

driver.maximize_window()
driver.implicitly_wait(10)


userName=driver.find_element_by_name("username")
userName.send_keys("lauserone")
passWord=driver.find_element_by_name("password")
passWord.send_keys("qwerty1234")
driver.find_element_by_xpath("/html/body/div/form/div/div[7]/button/img").click() #login
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/ul/li[2]/a").click()

time.sleep(2)

a=driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[2]/div/div[1]/div/input")
b=names.get_first_name()
a.send_keys(b)

t=driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[4]/div/div[1]/div/input")
l= names.get_last_name()
t.send_keys(l)

driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div/div/label[1]").click()

z=driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[2]/div/div[3]/div/input")
x= b+l +"@gmail.com"
z.send_keys(x)


driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[2]/div/div[4]/div/input").send_keys("Testing")


driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[2]/div/div[5]/label/span[2]").click()

def random_dob_generator():
    day = str(random.randint(1, 30))
    print(day)
    month = str(random.randint(1, 12))
    print(month)
    year = str(random.randint(1950,  2012))
    print(year)
    return '{}-{}-{}'.format(day,month,year)

dob = random_dob_generator()
dobnum = driver.find_element_by_id("PHAge")
dobnum.clear()
dobnum.send_keys(str(dob))



def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}{}{}'.format(first, second, last)

contact_number = random_phone_num_generator()
cnum = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[4]/div/div[3]/div/input")
cnum.clear()
cnum.send_keys(str(contact_number))


driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/form/div/div[5]/div[2]/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/form/div/div[5]/div[3]/div/div/div[3]/button[2]").click()

row_count=len (driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr"))
print("no of rows",row_count)

cal_count=len (driver.find_elements_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div/table/thead/tr/th"))
print("no of colm",cal_count)

driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr[{}]/td[1]".format(row_count)).click()