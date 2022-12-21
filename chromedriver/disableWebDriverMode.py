from selenium import webdriver
import time

options = webdriver.ChromeOptions() # объект опций для передачи опций
driver = webdriver.Chrome(executable_path='/Users/daramuravskaa/PycharmProjects/selenium/chromedriver/chromedriver', options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
     "source": """
          const newProto = navigator.__proto__
          delete newProto.webdriver
          navigator.__proto__ = newProto
          """
    })#скрипт для скрытия работы сайта через селениум (имитация работы человеком)

try:
    driver.get("https://bot.sannysoft.com/")
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()