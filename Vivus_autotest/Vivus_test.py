from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.EdgeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=r'C:\Users\mpopov\Desktop\edgedriver_win64\msedgedriver.exe')    # подключение вебдрайвера
driver = webdriver.Edge(service=service, options=options)
driver.get("https://www.vivus.ru/")    # открытие браузера с нужной страницей


original_window = driver.current_window_handle
actions = ActionChains(driver)
for a in range(1, 6):
    element = driver.find_element(By.XPATH, f'/html/body/footer/div/div/div[1]/p/a[{a}]')     # поиск элемента страницы с помощью XPATH
    driver.execute_script("arguments[0].scrollIntoView(true);", element)    # прокрутка страницы до определенного элемента
    time.sleep(2)
    element.click()     # прожатие элемента
    time.sleep(2)
    driver.switch_to.window(original_window) # переключение на основную вкладку браузера


time.sleep(5)
driver.quit()     # закрытие браузера
exit()