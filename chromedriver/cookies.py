import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import auth_data
import pickle #модуль для сохранения куки файлов

url = "https://iterius.smissltd.com/home"
driver = webdriver.Chrome(executable_path='/Users/daramuravskaa/PycharmProjects/selenium/chromedriver/chromedriver')


try:
    # driver.get(url=url)
    # time.sleep(2)
    # close_button = driver.find_element(By.CLASS_NAME, '_closeBtn_70ilu_37')
    # close_button.click()
    # time.sleep(2)
    # login_button = WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, '_button_1wo2a_1._login_1wo2a_148')))
    # login_button = driver.find_element(By.CLASS_NAME, '_button_1wo2a_1._login_1wo2a_148')
    # login_button.click()
    # time.sleep(2)
    # email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[1]/div[2]/input')))
    # email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[1]/div[2]/input')
    # email.click()
    # email.send_keys(auth_data.email)
    # password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[2]/div[2]/input')))
    # password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/label[2]/div[2]/input')
    # password.click()
    # password.send_keys(auth_data.password)
    # voity = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/form/div/button')
    # voity.click()
    # time.sleep(10)
    #
    # pickle.dump(driver.get_cookies(), open(f"{auth_data.email, auth_data.password}_cookies", "wb")) #создаем и открываем на запись файл с куками
    driver.get("https://iterius.smissltd.com/home/modal/login")
    time.sleep(5)

    for cookies in pickle.load(open(f"{auth_data.email, auth_data.password}_cookies", "rb")):
        driver.add_cookie(cookies)
    time.sleep(2)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()