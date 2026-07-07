from pages.base_page import BasePage # Import the BasePage

class LoginPage(BasePage):
    sign_in=("xpath","(//a[text()='Sign In'])[1]")
    email_id=("id","email")
    password_id=("id","password")
    remember_me=("id","remember")
    login_button=("id","login_btn")

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    # def signin(self):
    #     self.click(self.sign_in)
    #
    # def emailid(self,email):
    #     self.send_keys(self.email_id,email)
    #
    # def passwordid(self,password):
    #     self.send_keys(self.password_id,password)
    #
    # def rememberme(self):
    #     self.click(self.remember_me)
    #
    # def loginbutton(self):
    #     self.click(self.login_button)

    # def login(self,email,password):
    #     self.signin()
    #     self.emailid(email)
    #     self.passwordid(password)
    #     self.rememberme()
    #     self.loginbutton()
    def login(self, email, password):
        self.click(self.sign_in)
        self.send_keys(self.email_id, email)
        self.send_keys(self.password_id, password)
        self.click(self.remember_me)
        self.click(self.login_button)
