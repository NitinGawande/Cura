import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()
    def test_homePageTitle(self,setup):
        self.logger.info('---------test_001_login---------------')
        self.logger.info('---------verifing homepage title ---------------')
        self.driver,self.wait=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="CURA Healthcare Service":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\"+"testcase1passed.png")
            self.driver.close()
            self.logger.info("Test case is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "testcase1failed.png")
            self.driver.close()
            self.logger.error("title title is wrong")
            assert False


    def test_login(self,setup):
        self.logger.info("Test_case_002")
        self.driver,self.wait = setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver, self.wait)
        self.lp.clickfirst()
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Clicklogin()
        self.logger.info("Site is opened")
        new_title=self.driver.title
        if new_title=="CURA Healthcare Service":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\"+"testcase2passed.png")
            self.driver.close()
            self.logger.info("Everything is fine")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"testcase2failed.png")
            self.driver.close()
            self.logger.error("problem in test case2")
            assert False




