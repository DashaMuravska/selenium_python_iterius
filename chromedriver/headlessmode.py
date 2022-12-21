from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import auth_data

url = "https://iterius.smissltd.com/home"
driver = webdriver.Chrome(executable_path='/Users/daramuravskaa/PycharmProjects/selenium/chromedriver/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('headless') #опция зауска браузера в фоновом режиме
driver = webdriver.Chrome(options=options)

try:
    driver.get(url=url)
    time.sleep(2)
    print("Open Iterius home page unlogged...")

    close_button = driver.find_element(By.CLASS_NAME, '_closeBtn_70ilu_37')
    close_button.click()
    time.sleep(2)
    print("Close cookies pop-up...")

    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, '_button_1wo2a_1._login_1wo2a_148')))
    login_button = driver.find_element(By.CLASS_NAME, '_button_1wo2a_1._login_1wo2a_148')
    login_button.click()
    time.sleep(2)
    print("Click the Login button...")

    email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[1]/div[2]/input')))
    email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[1]/div[2]/input')
    email.click()
    email.send_keys(auth_data.email)

    password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[2]/div[2]/input')))
    password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[2]/div[2]/input')
    password.click()
    password.send_keys(auth_data.password)

    voity = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/button')
    voity.click()
    time.sleep(5)
    print("Log in to system...")
    print("Close browser...")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()