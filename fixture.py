import pytest
from selenium import webdriver
from config import URL

@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.get(URL)
    yield chrome
    chrome.quit()