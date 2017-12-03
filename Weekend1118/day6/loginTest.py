import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from Weekend1118.day5.myTestCase import MyTestCase
from Weekend1118.day6.page_object.loginPage import LoginPage
from Weekend1118.day6.page_object.personalCenterPage import PersonalCenterPage

# class LoginTest(MyTestCase):
#     def test_login(self):
#         #打开网页
#         self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
#         #输入用户名
#         self.driver.find_element(By.ID,"username").send_keys("chengrj")
#         #输入密码
#         self.driver.find_element(By.ID, "password").send_keys("chengrj")
#         #点击登录按钮
#         self.driver.find_element(By.CLASS_NAME, "login_btn").click()
#         #验证是否跳转到管理中心页面
#         expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"  #预期结果
#         time.sleep(5)
#         self.assertIn("我的会员中心",self.driver.title)



class LoginTest(MyTestCase):
    def test_login(self):
        lp=LoginPage(self.driver)  #实例化一个登录页面
        lp.open()
        lp.input_username("chengrj")
        lp.input_password("chengrj")
        lp.click_login_button() #点击提交按钮
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title,self.driver.title)