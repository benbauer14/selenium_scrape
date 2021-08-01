
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBPAGE = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome("/Users/benbauer/Documents/VSCode/chromedriver")

driver.get(WEBPAGE)

searchbar = driver.find_element_by_name("search")

searchbar.send_keys("Python")
searchbar.send_keys(Keys.RETURN)

driver.quit()