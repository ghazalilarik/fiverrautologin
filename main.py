from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'c:/Users/Hm/Downloads/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.fiverr.com/login")

element = driver.find_element_by_id("login")
element.send_keys("youremail")

element = driver.find_element_by_id("password")
element.send_keys("yourpassword")

element.send_keys(Keys.RETURN)
