from selenium import webdriver


class FacebookBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='./drivers/chromedriver')

    def login(self):
        self.driver.get('https://id-id.facebook.com/')

        email = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
        email.send_keys('michael.ahli99@gmail.com')
        password = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input')
        password.send_keys('koko25285282ahli0410')
        login_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
        login_btn.click()

        getValue = self.driver.find_element_by_xpath(
            '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/h3/span/div/div[1]/span/span')
        print(getValue.text)
        while(True):
            pass


start = FacebookBot()
start.login()

# driver.get('http://www.google.com/')
# while(True):
#    pass
