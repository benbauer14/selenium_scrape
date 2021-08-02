from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBPAGE = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome("/Users/benbauer/Documents/VSCode/chromedriver")

driver.get(WEBPAGE)

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
submit_button = driver.find_element_by_class_name("btn-block")

first_name.send_keys("Tilly")
last_name.send_keys("Tooter")
email.send_keys("Tilly@tooter.com")
submit_button.click()
