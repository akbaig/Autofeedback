#This is program that automates the feedback for the 4th semester CS dept

import sys, os, time
import random
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

def check_element(element):
    if is_firefox:
        try:
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, element)))
        except TimeoutException:
            print ("Loading took too much time!")

if __name__ == "__main__":

    #Take students registration number and password
    studentId = input("Enter your registration number: ")
    studentPassword = input("Enter your password: ")
    is_firefox = False
    
    if getattr(sys, 'frozen', False): 
    # executed as a bundled exe, the driver is in the extracted folder
        try:
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            browser = Chrome(chromedriver_path)
            
        except WebDriverException:
            geckodriver_path = os.path.join(sys._MEIPASS, "geckodriver.exe")
            browser = Firefox(executable_path=geckodriver_path)
            is_firefox = True
            delay = 5
    else:
    # executed as a simple script, the driver should be in `PATH`
        try:
            browser = Chrome()
        except WebDriverException:
            browser = Firefox()
            is_firefox = True
            delay = 5

    browser.get("http://111.68.99.200/SRA-n/")

    #NOTE: I am continuously using find_by_element instead of storing it in a variable
    #because our universities bad coding practices resest the entire DOM and makes the
    #variable invalid
    
    check_element('ddlDegreeProg')
    # navigate to the page
    select = Select(browser.find_element_by_id("ddlDegreeProg"))
    print ([o.text for o in select.options]) # these are string-s
    select.select_by_visible_text("BS Computer and Information Sciences")

    id = browser.find_element_by_id("txtRegNo")
    id.send_keys(studentId)
    
    password = browser.find_element_by_id("a63542B5")
    password.send_keys(studentPassword,Keys.RETURN)
    
    check_element('cmdViewTranscript')

    (browser.find_element_by_id("cmdViewTranscript")).send_keys(Keys.RETURN)
    check_element('btnfeedback')
    (browser.find_element_by_id("btnfeedback")).send_keys(Keys.RETURN)
    
    check_element('_ctl0_ContentPlaceHolder1_ddlCourse')
    course_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))
    courses = course_id.options
    print(len(courses))

    #Loops through the entire feedback and sets a random value for every question
    for name in range(len(courses) - 1):
        (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))).select_by_index(name)

        (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))).select_by_index(0)

        if name == 6:
            (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))).select_by_index(1)

        for i in range(0,18):
            score = "_ctl0_ContentPlaceHolder1_txt" + (chr(ord('A') + i))
            randNumber = random.randrange(1,6)
            (browser.find_element_by_id(score)).send_keys(randNumber)#You can change the value here and set it between 1-5

    #Writes the messages in the two text areas. You can change the messages
        (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtComments")).send_keys("""No Comment""")
        (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtCommentsCourse")).send_keys("""No Comment""")

        (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit")).send_keys(Keys.RETURN)
        (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset")).send_keys(Keys.RETURN)
