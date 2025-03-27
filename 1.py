import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    email.send_keys("Ivan@Petrov")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()