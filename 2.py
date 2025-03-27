import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox.click()
    rdbtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rdbtn.click()
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
