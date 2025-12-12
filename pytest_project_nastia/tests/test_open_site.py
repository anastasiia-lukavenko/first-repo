from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# def test_auto_in_title():
#     browser = webdriver.Chrome()    
#     browser.get("https://auto.ria.com/") 
#     title = browser.title           #создаем переменную для тайтла страницы
#     print(title)                 #показываем в терминале


#     assert "AUTO" in title, "'AUTO' not in title"
    
#     # here was time.sleep(10)
#     browser.quit()

# зайти на тот же сайт, и по нажимать на кнопки такие как тип транспорта "легковые", марка "бмв", год выпуска 2025,
# цена от 20_000 до 50_000, затем нажать кнопку поиск 
def test_search_auto():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()   # 👈 делает окно на весь экран
    browser.get("https://auto.ria.com/")
    # here was time.sleep(1)

#  закрыть куки-баннер, если он есть
    try:
        gdpr = browser.find_element(By.CLASS_NAME, "gdpr")
        try:
        # пробуем найти любую кнопку внутри баннера и кликнуть
            btn = gdpr.find_element(By.XPATH, ".//button[contains(., 'Погод') or contains(., 'Зрозум') or contains(., 'Agree') or contains(., 'OK')]")
            btn.click()
        except:
        # если текст не совпал — жмём по первому доступному <button>
            gdpr.find_element(By.TAG_NAME, "button").click()
        # here was # here was time.sleep(1)
    except:
        pass


    button_v_type = browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[2]/div[1]/div/label/button')
    button_v_type.click()
    # here was time.sleep(1)
    
    legkovye = browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[2]/div[1]/div/div/div/div[2]/div/label[2]/span[2]/label')
    legkovye.click()
    # here was time.sleep(1)

    button_mark = browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[2]/div[2]/div/label/button')
    button_mark.click()
    # here was time.sleep(1)

    search_bmw = browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[2]/div[2]/div/div/div/div[2]/div[1]/input')
    search_bmw.click()
    # here was time.sleep(1)
    search_bmw.send_keys("BMW")
    # here was time.sleep(1)

    button_bmw = browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[2]/div[2]/div/div/div/div[2]/div[2]/label[1]/span[2]/span')
    button_bmw.click()
    # here was time.sleep(1)

    next_but = browser.find_element(By.CSS_SELECTOR, '#searchForm > div:nth-child(2) > div:nth-child(2) > div > div > div.button-main.mx-16.mt-8 > button')
    next_but.click()
    # here was time.sleep(1)

    iskat = browser.find_element(By.XPATH, '//*[@id="searchForm"]/div[3]/div[1]/div/button')
    iskat.click()
    # here was time.sleep(1)

    browser.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
    # here was time.sleep(2)

    browser.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
    # here was time.sleep(5)

    
    browser.quit()

















