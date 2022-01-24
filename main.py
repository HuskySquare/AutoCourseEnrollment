import pickle, os, time
from selenium import webdriver
from sys import platform

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if platform == 'linux':
    chrome_path = os.path.abspath("./chromedriver")
else: #windows
    chrome_path = os.path.abspath("./chromedriver.exe")


browser = webdriver.Chrome(executable_path=chrome_path)
browser.delete_all_cookies()

cookies = pickle.load(open(r"C:\Users\leo20\PycharmProjects\Auto_Course_Enrollment\cookie.txt", 'rb'))
browser.get("https://acorn.utoronto.ca/sws/#/")
for cookie in cookies:
    browser.add_cookie(cookie)



browser.refresh()

browser.get("https://acorn.utoronto.ca/sws/#/courses/1")
driver_wait = WebDriverWait(browser, 2)

x_button_wait = WebDriverWait(browser, 0.05)

# -------- Course Selection ------------


for i in browser.find_elements_by_class_name("updateEnrolment"):
    while True:
        try:
            i.click()
            
            submit_enrol = driver_wait.until((EC.presence_of_element_located((By.ID, "enrolFromPlan"))))
            submit_enrol.click()


        except Exception as e:

            print(e)

        try:
            close_btn = x_button_wait.until((EC.presence_of_element_located((By.CLASS_NAME, "close"))))
            close_btn.click()
            break

        except Exception as e:
            print(e)
            print("Maybe x button doesn't exist")
            break

