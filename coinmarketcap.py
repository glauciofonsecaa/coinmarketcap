import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib3 import disable_warnings
from time import sleep

disable_warnings()

Service(ChromeDriverManager().install())
nopecha_key = ''

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

with open('ext.crx', 'wb') as f:
    f.write(requests.get('https://nopecha.com/f/ext.crx').content)
options.add_extension('ext.crx')

driver = webdriver.Chrome(options=options)
driver.set_window_size(1395, 970)
driver.get(f"https://nopecha.com/setup#{nopecha_key}")
sleep(3)


driver.get('https://coinmarketcap.com/')
sleep(7)
login_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/button/div[1]/div')
login_button.click()
sleep(2)
cookies_accept = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
cookies_accept.click()
sleep(2)

usuario = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/input')
usuario.send_keys('')
senha = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[2]/div[2]/input')
senha.send_keys(r'')
login = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[3]/button/div[1]')
login.click()

driver.quit()