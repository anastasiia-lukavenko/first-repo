import pytest
from src.calculator import Calculator

@pytest.fixture(scope="module")
def calc():
    return Calculator()

@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / "example.txt"
    f.write_text("hello")
    yield f
    if f.exists():
        f.unlink()

@pytest.fixture(autouse=True)
def _log_start_end(caplog):
    caplog.set_level("INFO")
    yield

import pytest

@pytest.fixture
def driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    # Если вдруг захочешь запускать без окна браузера — можно включить Headless:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)  # ждём элементы до 5 секунд, если они не сразу появляются

    yield driver  # отдаём браузер тесту

    driver.quit()  # после завершения теста закрываем браузер полностью

import requests

@pytest.fixture
def api_client():
    
    session = requests.Session()
    session.base_url = "https://jsonplaceholder.typicode.com"
    return session


