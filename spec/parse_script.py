from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import timedelta
from bs4 import BeautifulSoup as bs 
from selenium.webdriver.common.keys import Keys
import time

def scrape():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    browser = webdriver.Chrome(options=options)
    
    actions = ActionChains(browser)

    browser.get('https://cccb.ru/')
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/header/div[1]/div/div[1]/a[3]').click()
    time.sleep(1)
    login = browser.find_element(By.XPATH, '//*[@id="auth-modal"]/div/form/div[2]/div[1]/div/input')
    login.send_keys('regentgold')
    time.sleep(1)
    password = browser.find_element(By.XPATH, '//*[@id="auth-modal"]/div/form/div[2]/div[2]/div/input')
    password.send_keys('kvT5P22i')
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="auth-modal"]/div/form/div[2]/div[5]/div/input').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/aside/ul/li[5]/a').click()
    time.sleep(1)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)
    html = browser.page_source
    soup = bs(html)
    current_id = soup.find_all('input', class_='input-text startDatePicker hasDatepicker')[0]['id']
    calendar = browser.find_element(By.XPATH, f'//*[@id="{current_id}"]')
    calendar.click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[@class='ui-state-default ui-state-highlight']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="lk_tab-1"]/div/div/form/div/div/input[2]').click()
    time.sleep(5)
    browser.close()
