import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    #Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_smarthome'\
              '&response_type=code&scope=openid&redirect_uri=https%3A%2F%2Flk.smarthome.rt.ru%2Foauth2%2Fcallback')
    driver.maximize_window()
    yield driver
    driver.quit()