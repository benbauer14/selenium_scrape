from selenium import webdriver

WEBPAGE = "https://www.python.org/"

driver = webdriver.Chrome("/Users/benbauer/Documents/VSCode/chromedriver")

driver.get(WEBPAGE)
event_times = driver.find_elements_by_css_selector(".event-widget time")

event_links = driver.find_elements_by_css_selector(".event-widget .menu a")

event_dict = {}

for time in range(0, len(event_times)):
    event_dict[time] = {"time": event_times[time].text, "name": event_links[time].text}
    
print(event_dict)

driver.quit()