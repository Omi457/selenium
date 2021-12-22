from selenium import webdriver
import time
import selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   #explicit
from selenium.webdriver.common.action_chains import ActionChains #scrolling pages


driver = webdriver.Chrome(executable_path= "F:\selenium\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(2)



Drag =["box1","box2","box3","box4","box5","box6","box7"]

Drop =["box101","box102","box103","box104","box105","box106","box107"]


object = zip(Drag, Drop)
for element1, element2 in object:
    source= driver.find_element_by_id(element1)
    target = driver.find_element_by_id(element2)
    # actions = ActionChains(driver)
    ActionChains(driver).drag_and_drop(source, target).perform()
    # actions.perform()
    time.sleep(2)

# driver.quit()



