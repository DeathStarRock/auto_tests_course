import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book").click()
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(y)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()