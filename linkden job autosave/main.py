from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin 
from selenium.webdriver import ActionChains
import time

email = "mail"
password = "pass"

path = Service("chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# login
login = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login.click()
Enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
Enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
login = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
Enter_email.send_keys(email)
Enter_password.send_keys(password)
login.click()

# check
time.sleep(15)

jobs = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[1]/div/ul')


for job in jobs:
    job.click()
    time.sleep(1)
    saveBtn = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button/span[1]')
    saveBtn.click()



