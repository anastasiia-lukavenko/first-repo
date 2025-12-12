from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def test_choose_year(driver: WebDriver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://zakupivli.pro/")

    btn_srch = driver.find_element(By.XPATH, '//*[@id="js-header"]/div/div[2]/a/span')
    btn_srch.click()

    line_srch = driver.find_element(By.XPATH, '//*[@id="search_on_main_page"]')
    line_srch.click()

    line_srch.send_keys("авто")
    line_srch.send_keys(Keys.ENTER)
    results = driver.find_elements(By.CSS_SELECTOR, '#move-page-up > div.zkb-layout > main > div > ul > li:nth-child(1) > div.zkb-list__main-block')
    assert results, "Нет результатов поиска — список пустой"

    first_result = results[0]
    first_result.click()






