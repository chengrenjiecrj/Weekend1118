import unittest

import time
from selenium.webdriver.common.by import By

from Weekend1118.day5.myTestCase import MyTestCase
from Weekend1118.day6.database.connectDB import connDb


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME,"username").send_keys("crj")
        driver.find_element(By.NAME,"password").send_keys("crj123456")
        driver.find_element(By.NAME,"userpassword2").send_keys("crj123456")
        driver.find_element(By.NAME,"mobile_phone").send_keys("15632658532")
        driver.find_element_by_name("email").send_keys("4563@13.com")
        driver.find_element(By.CLASS_NAME,"reg_btn").click()

        #检查数据库中新增的记录的用户名he输入的用户名是否一致
        expected = "crj"
        time.sleep(3)
        actual = connDb()[1]
        self.assertEquals(expected,actual)

        print(connDb()[1])