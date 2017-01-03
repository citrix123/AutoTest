from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "/usr/bin/firefox"
geckodriver="/opt/geckodriver"

driver = webdriver.Firefox(capabilities=caps) #, executable_path="/usr/bin/firefox") #1

######################## It Works from Here ########################
#Algo ; To open Profile Page
#1. open firefox
#2. open URL http://localhost/rahjain_ws7/index.php/login
#3. put login and password and Enter
#4. click on Profile
####################################################################
driver.get("http://localhost/rahjain_ws7/index.php/login") #2

user = driver.find_element_by_id("username") #3
user.send_keys("msptransporter") #3
print "putting Username"
password = driver.find_element_by_id("password") #3
password.send_keys("admin") #3
print "put password"
user.send_keys(Keys.ENTER) #3
print "pressed Enter"

try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "Profile"))
    )
    print element
    element.click()
    print "finding id Profile "

    Profile = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "CompanyName")))
    Profile.send_keys("AMD Company") #3

finally:
    print "I am here"
    #driver.quit()

print "Pressed Enter"


#driver.quit()
