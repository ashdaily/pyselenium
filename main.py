from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

#Auto login linkedin
driver.get("https://www.linkedin.com/login")

username = driver.find_element_by_id("username")
username.send_keys("put your email here")

password = driver.find_element_by_id("password")
password.send_keys("put your password here")
password.send_keys(Keys.RETURN)