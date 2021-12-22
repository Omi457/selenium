from selenium import webdriver
import XLUtils
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path= "F:\selenium\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:5000/loginUser")
time.sleep(2)

path = "C://Users/Admin/Desktop/writeexcel.xlsx"

row = XLUtils.getRowCount(path, "Sheet1")    ### statement for get the row count

for r in range(2, row +1):
    UserName = XLUtils.readData(path, "Sheet1", r, 1)
    Password = XLUtils.readData(path, "Sheet1", r, 2)
    
    driver.find_element_by_name("username").send_keys(UserName)
    driver.find_element_by_name("password").send_keys(Password)
    driver.find_element_by_xpath("/html/body/div[1]/div/form/div/div[7]/button/img").click()
    time.sleep(1)   

if driver.find_element_by_link_text == "lauserone" :
    print("test is passed")
    XLUtils.writeData(path,"Sheet1", r, 3,"test passed")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/a[2]/button/img").click()
else:
    print("test failed")    
    XLUtils.writeData(path,"Sheet1", r, 3 , "test failed")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div/button").click()
    time.sleep(1)
