from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.EdgeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=r'C:\Users\mpopov\Desktop\edgedriver_win64\msedgedriver.exe')    # подключение вебдрайвера
driver = webdriver.Edge(service=service, options=options)
driver.get("https://www.vivus.ru/")    # открытие браузера с нужной страницей
driver.set_window_size(1600, 900) # размер окна (По желанию)


original_window = driver.current_window_handle      # переменная для хранения главной вкладки сайта
count = ""
# for i in range(10):
for a in range(1, 6):       # Пробежка по нужной колонке на сайте
    element = driver.find_element(By.XPATH, f'/html/body/footer/div/div/div[1]/p/a[{a}]')     # поиск элемента страницы с помощью XPATH
    link = element.get_attribute('href')    # поиск ссылки в элементе
    assert link != count    # проверка на ошибку новой ссылки
    print('Прошлый: ', count,  '\n', 'Текущий: ', link, '\n *****************************')
    count = link
    driver.execute_script("arguments[0].scrollIntoView(true);", element)    # прокрутка страницы до определенного элемента
    time.sleep(2)
    element.click()     # прожатие элемента
    time.sleep(2)
    driver.switch_to.window(original_window) # переключение на основную вкладку браузера


time.sleep(2)
driver.quit()     # закрытие браузера

exit()