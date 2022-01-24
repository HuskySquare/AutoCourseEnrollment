import os
import pickle
import time
from sys import platform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

if platform == 'linux':
    chrome_path = os.path.abspath("./chromedriver")
else: #windows
    chrome_path = os.path.abspath("./chromedriver.exe")

username = ""
password = ""
browser = webdriver.Chrome(executable_path=chrome_path)
browser.delete_all_cookies()

browser.get("https://acorn.utoronto.ca/sws/#/")
default_page = browser.current_url

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

time.sleep(5)
cookies = browser.get_cookies()
pickle.dump(cookies, open(os.path.abspath("./cookie.txt"), 'wb'))

