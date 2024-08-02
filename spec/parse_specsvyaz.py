import schedule
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup as bs 
import warnings
import time
import pandas as pd 
import boto3 
import glob 
import os
import datetime as dt
import warnings 

warnings.filterwarnings('ignore')


def job():
    
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
    
    
def load():
    name_file = f'analytics-fileshare/specsvyaz/{dt.date.today().strftime('%Y-%m-%d')}.xlsx'
    bucket_name = 'analytics-fileshare'
    
    ACCESS_KEY='YCAJEeHTlV8i3hU5cNPYnIwmK'
    SECRET_KEY='YCOnqkRxpZOrvE2Jfrc3WPB6aS0fONeIkrgEQKX4'
    ENDPOINT = "https://storage.yandexcloud.net"

    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name="ru-central1"
    )

    s3_client = session.client(
        "s3", endpoint_url=ENDPOINT)
    
    path = r'C:\\Users\Trenkin.Sergey\Downloads\\' # указать папку, в которую падает файл после загрузки
    list_of_files = glob.glob(f'{path}Otchet_po_otpravleniyam*.xlsx') 
    latest_file = max(list_of_files, key=os.path.getctime)

    try: df = pd.read_excel(latest_file, header=6).drop(columns=['Unnamed: 0'])[:-1]
    except: df = pd.read_excel(latest_file)

    df['report_date'] = pd.to_datetime(dt.date.today().strftime('%Y%m%d'))

    df.to_excel(latest_file, index=False)
    
    s3_client.upload_file(latest_file, Bucket= bucket_name, Key= name_file)
    
schedule.every().day.at("15:08").do(job)
schedule.every().day.at("15:09").do(load)

while True:
    schedule.run_pending()