import pickle, os, time
from selenium import webdriver
from sys import platform

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if platform == 'linux':
    chrome_path = os.path.abspath("./chromedriver")
else:  # windows
    chrome_path = os.path.abspath("./chromedriver.exe")

username = ""
password = ""
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)
browser.delete_all_cookies()

browser.get("https://acorn.utoronto.ca/sws/#/")

default_page = "https://acorn.utoronto.ca/sws/#/"

driver_wait = WebDriverWait(browser, 60)


login_name = driver_wait.until(EC.presence_of_element_located((By.ID, 'username')))
login_name.send_keys(username)

login_pwd = driver_wait.until(EC.presence_of_element_located((By.ID, 'password')))
login_pwd.send_keys(password)


while True:
    try:
        login_btn = browser.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/form/button")
        login_btn.click()
        break
    except:
        print("Login button not found")

# landing_wait = WebDriverWait(browser, 100000)
# landing_btn = landing_wait.until((EC.element_to_be_clickable((By.CLASS_NAME, "landing-btn"))))
# landing_btn.click()


while True:
    if browser.current_url == default_page:
        break



browser.get("https://acorn.utoronto.ca/sws/#/courses/1")

time.sleep(0.5)
driver_wait = WebDriverWait(browser, 2)

x_button_wait = WebDriverWait(browser, 0.05)

# -------- Course Selection ------------

elements = []
while len(elements) != 5:
    elments = browser.find_elements_by_class_name("updateEnrolment")


for i in elments:
    while True:
        try:
            i.click()

            submit_enrol = driver_wait.until((EC.presence_of_element_located((By.ID, "enrolFromPlan"))))
            submit_enrol.click()
            #break

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

