from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

email = "mail"
password = "pass"
promised_speed = 50

path = Service("chromedriver.exe")


class InternetSpeedTwitterBot():
    def __init__(self,path):
        self.driver = webdriver.Chrome(service=path)
        self.speed = 0
    
    def get_internet_speed(self):
        self.driver.get("https://fast.com/#")
        time.sleep(20)
        self.speed = self.driver.find_element(By.XPATH,'//*[@id="speed-value"]')
        print(self.speed.text)
        self.speed = int(self.speed.text)
        if self.speed < 27:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        # self.speed = 50
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        # enter email
        Enter_email = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        Enter_email.send_keys(email)
        # continue
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(2)
        # enter password
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
        # LOGIN
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        time.sleep(10)
        # clicking on tweet button
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
        time.sleep(2)
        # typing tweet
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(f"dear, provider Why is my speed {self.speed}mbps when I pay for {promised_speed}mbps")
        time.sleep(2)
        # entering the tweet
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click()
        time.sleep(5)


run = InternetSpeedTwitterBot(path=path)
run.get_internet_speed()
