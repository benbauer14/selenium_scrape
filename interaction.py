from selenium import webdriver

WEBPAGE = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome("/Users/benbauer/Documents/VSCode/chromedriver")

driver.get(WEBPAGE)
articles = driver.find_element_by_css_selector("#articlecount a")

print(articles.text)

driver.quit()