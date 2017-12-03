from selenium.webdriver.common.by import By


class LoginPage:
    #构造方法的作用  实例化LoginPage对象的时候,必须妖精调用构造方法,需要吧dirver作为参数
    #python构造方法必须是固定写法__init__
    #便于别的属性he方法使用driver
    def __init__(self,driver):
        self.driver = driver

    title = "我的会员中心 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"

#小括号表示元组,元组中有两个值,第一个元素是空间的定位方式,第二个元素是控件定位方式的具体的值
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        #self.driver.find_element_by_id("username").send_key(username)
        #self.driver.find_element(By.ID,"username").send_keys(username)
        #*星号的作用就是把一个元组中的元素分别传入方法参数中,传入的不是一个元组了
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        #self.driver.find_element(By.CLASS_NAME, "login_btn").click()
        self.driver.find_element(*self.login_button_loc).click()


