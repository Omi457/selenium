from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path = "F:\selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.myheritage.com/deep-nostalgia")
time.sleep(4)

            # C:/Users/Admin/Desktop/New folder/photo.jp                        
upload = ("C:\\Users\\Admin\\Desktop\\New folder/photo.jpg")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/div/div/div/div[1]/div[2]/section/div[1]/div[1]/button/span/input").send_keys(upload)