import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(y)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox.click()
    rdbtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rdbtn.click()
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()