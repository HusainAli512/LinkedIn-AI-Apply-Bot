from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from links import *
import time
from gemini_test import *
class Jobs:
    def __init__(self , driver ):
        self.driver = driver
    
    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element(By.XPATH , value =xpath)
        except NoSuchElementException:
            return False
        return True
        
    def jobs_filter(self , jobname):
        
        self.jobs_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, jobs_button)))
        # self.jobs_button = self.driver.find_element(By.XPATH , jobs_button)
        self.jobs_button.click()
        self.job_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH , job_input)))
        # self.job_input = self.driver.find_element(By.XPATH , job_input)
        self.job_input.send_keys(jobname + Keys.ENTER)
        self.filter = WebDriverWait(self.driver , 30).until(EC.presence_of_element_located((By.XPATH , easy_apply)))
        self.filter.click()

    def jobsinfo(self):
        self.easy_apply_in_job_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH , easy_apply_in_job)))
        # self.easy_apply_in_job_button = self.driver.find_element(By.XPATH , value = easy_apply_in_job)
        self.easy_apply_in_job_button.click()
        if self.check_exists_by_xpath(submit_button):
                    time.sleep(2)
                    self.submit_button = self.driver.find_element(By.XPATH , value = submit_button)
                    self.submit_button.click()
        if self.check_exists_by_xpath(location):
            print(self.location.text)
            if self.location.text == 'Location (city)':
                self.put_location = self.driver.find_element(By.XPATH , value = location_input)
                self.put_location.send_keys('Lahore')
                time.sleep(2)
                self.put_location.send_keys(Keys.ARROW_DOWN)
                self.sleep(2)
                self.put_location.send_keys(Keys.ARROW_DOWN)
                self.sleep(2)
                self.put_location.send_keys(Keys.ENTER)
                time.sleep(2)

        elif self.check_exists_by_xpath(next_button1):
            time.sleep(2)
            self.next_button1 = self.driver.find_element(By.XPATH , value = next_button1)
            self.next_button1.click()
            if self.check_exists_by_xpath(form):
                self.form = self.driver.find_element(By.XPATH , value = form) 
                # print(self.form.text)
                self.fields = self.form.find_elements(By.XPATH, ".//input | .//select | .//textarea")
                print(len(self.fields))
                for field in self.fields:
                    tagname = field.tag_name
                    attribute = field.get_attribute('type')
                    fieldid = field.get_attribute('id')
                    question = ""
                    try:
                        # Try to find nearby label by for=ID
                        if fieldid:
                            label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{fieldid}']")
                            question = label.text
                        else:
                            # Try going up the DOM to find any visible text prompt
                            question = field.find_element(By.XPATH, "./ancestor::div[1]").text
                    except:
                        question = "No label found"


                    print('tag name ' , tagname)
                    print('attritbute ', attribute)
                    print('id' , fieldid)
                    print('question ', question)
                    print("---------------------------------------------------------------------------------")
                    if tagname == "input":
                        # if attribute == "radio":
                        #     print("-> Clicking radio button")
                        #     field.click()

                        if attribute == "text":
                            current_value = field.get_attribute("value")
                            if not current_value:
                                print("-> Sending keys to text input")
                                
                                field.send_keys(generate(question))
                # innerhtml = self.form.get_attribute('innerHTML')
                # print(f"inner html === {innerhtml}")
            if self.check_exists_by_xpath(next_button2):
                time.sleep(2)
                self.next_button2 = self.driver.find_element(By.XPATH , value = next_button2)
                self.next_button2.click()
                if self.check_exists_by_xpath(form):
                    self.form = self.driver.find_element(By.XPATH , value = form)
                    self.fields = self.form.find_elements(By.XPATH, ".//input | .//select | .//textarea")
                    print(len(self.fields))
                for field in self.fields:
                    tagname = field.tag_name
                    attribute = field.get_attribute('type')
                    fieldid = field.get_attribute('id')
                    question = ""
                    try:
                        # Try to find nearby label by for=ID
                        if fieldid:
                            label = self.driver.find_element(By.CSS_SELECTOR, f"label[for='{fieldid}']")
                            question = label.text
                        else:
                            # Try going up the DOM to find any visible text prompt
                            question = field.find_element(By.XPATH, "./ancestor::div[1]").text
                    except:
                        question = "No label found"


                    print('tag name ' , tagname)
                    print('attritbute ', attribute)
                    print('id' , fieldid)
                    print('question ', question)
                    print("---------------------------------------------------------------------------------")
                    if tagname == "input":
                        # if attribute == "radio":
                        #     print("-> Clicking radio button")
                        #     field.click()
                        if attribute == "text":
                            current_value = field.get_attribute("value")
                            if not current_value:
                                print("-> Sending keys to text input")
                                
                                field.send_keys(generate(question))