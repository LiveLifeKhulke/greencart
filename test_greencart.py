import time

import pytest
from selenium.webdriver.support.select import Select

from BaseClass import BaseClass

class TestGreenCart(BaseClass):
    def test_greencart(self,dataload):

        log=self.getlogger()

        self.driver.implicitly_wait(6)
        self.driver.find_element_by_css_selector("[class='search-keyword']").send_keys(dataload["keyword"])
        time.sleep(4)
        cart = self.driver.find_elements_by_css_selector("[class='product-action'] button")

        print(len(cart))
        for add in cart:
            # if add.find_element_by_xpath("parent::div/parent::div/h4").text == dataload["cart1"]:
                add.click()
                log.info("First choice is"+dataload["cart1"])

        self.driver.find_element_by_css_selector("[class='cart-icon']").click()
        self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
        sum = 0
        price=self.driver.find_elements_by_xpath("//tr/td[5]/p")
        for p in price:
            sum+= int(p.text)
        log.info("total sum is"+str(sum))
        self.driver.find_element_by_css_selector("[class='promoCode']").send_keys(dataload["promocode"])
        self.driver.find_element_by_xpath("//button[text()='Apply']").click()
        print(self.driver.find_element_by_css_selector("[class='promoInfo']").text)
        self.driver.find_element_by_xpath("//button[text()='Place Order']").click()
        dropdown = Select(self.driver.find_element_by_css_selector("[class='wrapperTwo'] div select"))
        dropdown.select_by_visible_text("India")
        self.driver.find_element_by_css_selector("[class='chkAgree']").click()
        self.driver.find_element_by_xpath("//button[text()='Proceed']").click()


    @pytest.fixture(params=[{"keyword":"ma","promocode":"rahulshettyacademy","cart1":"Mango - 1 Kg"}])
    def dataload(self,request):
        return request.param