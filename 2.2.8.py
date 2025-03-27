import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "228.txt"
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    First_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("бу")
    Last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("яя")
    Email = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("fewfwe@sfafsa.cm")

    x = browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()