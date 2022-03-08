import pytest

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name=='chrome':
        driver=webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    elif browser_name =="firefox":
        driver=webdriver.Firefox(executable_path="c:\\geckodriver.exe")
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    request.cls.driver=driver