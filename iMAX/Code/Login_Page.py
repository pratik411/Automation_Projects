class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)


class Homepage(BasePage):
    url = "http://192.168.2.20:1601/public/index.php"
    def getSignupForm(self):
        return SignupPage(self.driver)


class SignupPage(BasePage):
    url = "http://192.168.2.20:1601/public/index.php"
    def setName(self, username, password):
        self.driver.find_element_by_id("txtUserName").clear()
        self.driver.find_element_by_id("txtUserName").send_keys(username)
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtPassword").send_keys(password)
        self.driver.find_element("id","sbtnLogin").click()
        #self.driver.save_screenshot("login.pnp")