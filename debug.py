from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://vanphongdientu.utc.edu.vn/Login')
driver.find_element(By.NAME, 'userpwd').send_keys('123456')
driver.find_element(By.CLASS_NAME, 'submit_login').click()
time.sleep(2)
html = driver.page_source
with open('debug_html.txt', 'w', encoding='utf-8') as f:
    f.write(html)
driver.quit()
