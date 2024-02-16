import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield
    browser.quit()