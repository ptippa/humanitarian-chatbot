from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

search_url = "https://www.who.int/data/collections"
driver.get(search_url)

box = driver.find_element(By.XPATH, '//*[@id="PageContent_C035_Col00"]/label/input')
box.send_keys("tuberculosis")
box.send_keys(Keys.RETURN)
time.sleep(5)
first_result_link = driver.find_element(By.CSS_SELECTOR, "#collections > div:nth-child(14) > div > a")
first_result_url = first_result_link.get_attribute("href")
print("First search result URL:", first_result_url)

driver.close()