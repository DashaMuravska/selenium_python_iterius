from selenium import webdriver
import time
import random
from fake_useragent import UserAgent # подмена юзер агента

useragent = UserAgent() # объект класса UserAgent()
options = webdriver.ChromeOptions() # объект опций для передачи опций
options.add_argument(f"user-agent={useragent.random}")# с помощью add_argument добавляем все что нам нужно
driver = webdriver.Chrome(executable_path='/Users/daramuravskaa/PycharmProjects/selenium/chromedriver/chromedriver',
                           options=options) #путь к драйверу и применяем опции
try: # проверка юзер агента
    driver.get(url='https://wtools.io/ru/check-my-user-agent')
    time.sleep(5) #браузер закроется через 5 секунд
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()