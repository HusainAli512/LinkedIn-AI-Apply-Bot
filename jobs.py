from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
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
        
        self.jobs_button.click()
        self.job_input = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH , job_input)))
        
        self.job_input.send_keys(jobname + Keys.ENTER)
        self.filter = WebDriverWait(self.driver , 30).until(EC.presence_of_element_located((By.XPATH , easy_apply)))
        self.filter.click()
    def submit_button_func(self):
            try:
                if self.check_exists_by_xpath(submit_button):
                    time.sleep(2)
                    self.submit_button = self.driver.find_element(By.XPATH , value = submit_button)
                    self.submit_button.click()
                    self.done_func()
                    return True
                return False
            except:
                return False
    def final_button_func(self):
            try:
                if self.check_exists_by_xpath(final_submit):
                    time.sleep(2)
                    self.final_submit = self.driver.find_element(By.XPATH , value = final_submit)
                    self.final_submit.click()
                    self.done_func()
                    return True
                return False
            except:
                return False

    def next_buttons_func(self, next_button):
        try:
            # if self.check_exists_by_xpath(location):
                
            #     if self.location.text == 'Location (city)':
            #         self.put_location = self.driver.find_element(By.XPATH , value = location_input)
            #         time.sleep(3)
            #         self.put_location.send_keys('Lahore, Punjab, Pakistan')
            #         time.sleep(2)

                    
            #         time.sleep(10)
            # if self.check_exists_by_xpath(next_button):
            #     time.sleep(2)
            #     self.next_button = self.driver.find_element(By.XPATH , value = next_button)
            #     self.next_button.click()
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


                        print('tag name:', tagname)
                        print('attribute:', attribute)
                        print('id:', fieldid)
                        print('question:', question)
                        print("---------------------------------------------------------------------------------")

                        if tagname == "input":
                            if attribute == "text":
                                
                                current_value = field.get_attribute("value")
                                if not current_value:
                                    print("-> Sending keys to text input")
                                    field.send_keys(generate(question))
                        elif tagname == "input" and attribute == "radio":
                            print("-> Handling radio buttons")

                            try:
                                # Get all radio buttons with the same name attribute
                                radio_name = field.get_attribute("name")
                                radio_buttons = self.driver.find_elements(By.NAME, radio_name)

                                answer = generate(question).lower()
                                matched = False

                                for radio in radio_buttons:
                                    value = radio.get_attribute("value").lower()
                                    if answer in value:
                                        radio.click()
                                        print(f"-> Selected radio with value: {value}")
                                        matched = True
                                        break

                                if not matched:
                                    # Fallback: click first enabled radio button
                                    for radio in radio_buttons:
                                        if radio.is_enabled():
                                            radio.click()
                                            print(f"-> Fallback: clicked radio with value: {radio.get_attribute('value')}")
                                            break

                            except Exception as e:
                                print("-> Error handling radio buttons:", e)


                        elif tagname == "select":
                            print("-> Handling dropdown/select field")
                            try:
                                select = Select(field)
                                options = [o.text.strip() for o in select.options]

                                # Try to find the best match or use a default
                                answer = generate(question)
                                matched = False
                                for option in options:
                                    if answer.lower() in option.lower():
                                        select.select_by_visible_text(option)
                                        matched = True
                                        print(f"-> Selected option: {option}")
                                        break

                                if not matched:
                                    # Fallback to first non-default option (skip 'Select an option')
                                    for option in options:
                                        if option.lower() not in ["select an option", "choose", ""]:
                                            select.select_by_visible_text(option)
                                            print(f"-> Fallback selected: {option}")
                                            break

                            except Exception as e:
                                print("-> Error selecting dropdown:", e)
                if self.check_exists_by_xpath(next_button):
                    time.sleep(2)
                    self.next_button = self.driver.find_element(By.XPATH , value = next_button)
                    self.next_button.click()
                    return True
                print('returned false')                        
                return False
        except:
            return False
    def done_func(self):
        try:
            print("⏳ Waiting for 'Done' button...")
            self.done = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, done))
            )
            self.driver.execute_script("arguments[0].click();", self.done)  # JavaScript click
            print('✅ Done button clicked')
        except Exception as e:
            print(f'❌ Failed to click Done button: {e}')

    def jobsinfo(self):
        time.sleep(3)
        self.easy_apply_in_job_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH , easy_apply_in_job)))
        
        self.easy_apply_in_job_button.click()
        if self.submit_button_func():
            
            print("submit_button_clicked")
            
        elif self.next_buttons_func(next_button1):
            print('next button 1 clicked')
            if self.submit_button_func():
                
                print('submitted on second page')
                
            if self.next_buttons_func(next_button2):
                print('next button 2 clicked')
                if self.submit_button_func():
                    
                    print('submitted on third page')
                    
                if self.next_buttons_func(next_button3):
                    print('next button 3 clcked ')
                    if self.submit_button_func():
                        
                        print('submitted on 4 page')
                        
                    if self.final_button_func():
                        
                        print('submited successfully')
                    if self.next_buttons_func(review):
                        if self.submit_button_func():
                            
                            print('final submision')
                            
                        elif self.final_button_func():
                            
                            print('submited successfully')
                            







            