import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://sigaa.ufrn.br/")

username = os.getenv("SIGAA_USERNAME")
password = os.getenv("SIGAA_PASSWORD")

login = driver.find_element(By.CLASS_NAME, "login")
login.click()

input_username = driver.find_element(By.ID, "username")
input_username.send_keys(username)

input_password = driver.find_element(By.ID, "password")
input_password.send_keys(password)

submit = driver.find_element(By.NAME, "submit")
submit.click()

#vinculo = driver.find_element()
#vinculo.click()



