from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from links import *
import os
import time

linkedin_mail = os.environ.get('LINKEDIN_GMAIL')
linkedin_pass = os.environ.get('LINKEDIN_PASS')
class Login:
        def __init__(self):
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_experimental_option('detach', True)
            self.driver = webdriver.Chrome(options= self.chrome_options) 
            self.driver.get(linkedin)
            self.login()
        def login(self):
              self.signin_button = self.driver.find_element(By.XPATH, value = signin)
              self.signin_button.click()
              self.email = self.driver.find_element(By.ID , value= email)
              self.email.send_keys(linkedin_mail)
              self.password = self.driver.find_element(By.ID , value = password)
              self.password.send_keys(linkedin_pass)
              self.keep_me = self.driver.find_element(By.XPATH , value = keep_me_logged_in)
              self.keep_me.click()
              self.signin1_button = self.driver.find_element(By.XPATH , value= signin1)
              self.signin1_button.click()
              


