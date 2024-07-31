from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup as bs 
import warnings
import time

warnings.filterwarnings('ignore')

options_chrome = webdriver.ChromeOptions()
cService = webdriver.ChromeService(executable_path=r'C:\Users\Trenkin.Sergey\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe') # указать путь до хромдрайвера

# https://googlechromelabs.github.io/chrome-for-testing/#stable 
# по ссылке можно скачать версию chromedriver актуальную для машины

browser = webdriver.Chrome(service = cService, options=options_chrome)
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