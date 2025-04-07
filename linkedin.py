from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gemini_test import *
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach' , True)


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH , value =xpath)
    except NoSuchElementException:
        return False
    return True


def delay():
    time.sleep(4)
# load the job page
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4199441352&f_AL=true&keywords=ai%20automation&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")











#check for 2 conditions of sign in 
if check_exists_by_xpath('//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button'):
    sigin = driver.find_element(By.XPATH , value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    sigin.click()
elif check_exists_by_xpath('/html/body/div[1]/header/nav/div/a[2]'):
    sigin = driver.find_element(By.XPATH , value='/html/body/div[1]/header/nav/div/a[2]')
    sigin.click()

#fill out login details
email = driver.find_element(By.XPATH , value = '//*[@id="base-sign-in-modal_session_key"]')
email.send_keys("baloch.hb69@gmail.com")
password = driver.find_element(By.XPATH, value= '//*[@id="base-sign-in-modal_session_password"]')
password.send_keys("Plzdaddychill69")
okay = driver.find_element(By.XPATH , value = '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
okay.click()

#verify button 
# time.sleep(10)


#store the jobs in an array and then clicks on the jobs one by one 
#
try:
    # Wait up to 20 seconds for a specific element to appear
    jobs = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div/ul/li'))
    )
    jobs = driver.find_elements(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul/li')
    
except:
    print("Element not found within time limit.")

print(len(jobs))
for job in jobs:
    job =WebDriverWait(driver, 10).until(EC.element_to_be_clickable(job))
    job.click()
    print('job clicked ')
    apply_button = driver.find_element(By.CLASS_NAME ,value='jobs-apply-button')
    apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(apply_button))
    apply_button.click()
    print('apply button clicked ')
    
    if check_exists_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/input[1]"):
        location = driver.find_element(By.XPATH , '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/input[1]')
        location.send_keys("Lahore, Punjab, Pakistan")
        
    # next = driver.find_element(By.XPATH , value = '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/footer[1]/div[2]/button[1]')
    next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH ,'/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/footer[1]/div[2]/button[1]'))
    next.click()
    
    #next2 = driver.find_element(By.XPATH , value = '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/footer[1]/div[2]/button[2]')
    next2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH , '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/footer[1]/div[2]/button[2]'))
    next2.click()
    
    



""""
to do 
1.inside for loop create a function called apply.
2.in apply , for every element on each page check its existence using the (check_exists_by_path) function and if that exists parse its title and
send to gemini to get the answer and send keys with it.if that is dropdown menu , radio button figure that out also.
3.Finally click on apply button and then proceed to next job. 

"""















# job.click()
# jobs = driver.find_elements(By.CLASS_NAME , value = 'display-flex job-card-container relative job-card-list')

# delay()

# delay()




# loc = driver.find_element(By.XPATH , value = '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]')

# select = Select(loc)
# select.select_by_visible_text("Lahore")

# print('lahore selected')

# uni = driver.find_element(By.XPATH , value = '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[1]')


# uni_input = driver.find_element(By.CSS_SELECTOR , value= '#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4193161187-3135609928832765951-text')
# uni_input.send_keys(generate(uni.text))
# print(uni.text)









# discard.click()