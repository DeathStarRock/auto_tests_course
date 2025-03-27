import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    print(x)
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    print(y)
    z = str(int(x) + int(y))

    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(z)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()