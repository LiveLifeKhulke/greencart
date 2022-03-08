import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(6)
driver.find_element_by_css_selector("[class='search-keyword']").send_keys("ma")
time.sleep(4)
cart=driver.find_elements_by_css_selector("[class='product-action'] button")

print(len(cart))
for add in cart:
    if add.find_element_by_xpath("parent::div/parent::div/h4").text == "Mango - 1 Kg":
        add.click()
        break
driver.find_element_by_css_selector("[class='cart-icon']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector("[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[text()='Apply']").click()
print(driver.find_element_by_css_selector("[class='promoInfo']").text)
driver.find_element_by_xpath("//button[text()='Place Order']").click()
dropdown=Select(driver.find_element_by_css_selector("[class='wrapperTwo'] div select"))
dropdown.select_by_visible_text("India")
driver.find_element_by_css_selector("[class='chkAgree']").click()
driver.find_element_by_xpath("//button[text()='Proceed']").click()


