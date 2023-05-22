from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get('https://lambdatest.github.io/sample-todo-app/')
driver.implicitly_wait(100)

driver.find_element(By.NAME, "li1").click()


email_text_field = driver.find_element(By.ID, "sampletodotext")
sample_text = "Kyle"
email_text_field.send_keys(sample_text)
driver.implicitly_wait(100)

driver.find_element(By.ID, "addbutton").click()
driver.close()