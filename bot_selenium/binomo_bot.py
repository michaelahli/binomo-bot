from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
from datetime import datetime

username = "example@email.com"
password = "12345678"
#compensation = ["14000", "18000", "40000","90000", "203000", "406000", "1030000"]
#compensation = ["14000", "32000", "58000", "131200", "294400"]
compensation = ["5", "12", "32", "78", "195", "488"]
compen_index = 0

Iterate = True


class BinomoBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='./drivers/chromedriver')

    def login(self):
        self.driver.get('https://id-binomo.com/auth')

        sleep(2)

        email = self.driver.find_element_by_xpath(
            '//*[@id="qa_auth_LoginEmailInput"]/vui-input/div[1]/div[2]/vui-input-text/input')
        email.send_keys(username)

        passcode = self.driver.find_element_by_xpath(
            '//*[@id="qa_auth_LoginPasswordInput"]/vui-input/div[1]/div[2]/vui-input-password/input')
        passcode.send_keys(password)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="qa_auth_LoginBtn"]/button')
        login_btn.click()

    def autoclick(self, compen):
        bid = self.driver.find_element_by_xpath(
            '//*[@id="amount-counter"]/div[1]/div[1]/vui-input-number/input')

        bid.send_keys(Keys.CONTROL, 'a')
        sleep(1)
        bid.send_keys(Keys.CONTROL, 'a')
        bid.send_keys(compen)
        sleep(2)

        binary = randint(0, 1)

        if binary == 0:
            self.open_buy()
        else:
            self.open_sell()

    def open_buy(self):
        open_buy = self.driver.find_element_by_xpath(
            '//*[@id="qa_trading_dealUpButton"]/button')
        try:
            open_buy.click()
        except:
            pop_up = self.driver.find_element_by_xpath(
                '//*[@id="analytics-demo"]/button')
            pop_up.click()
            sleep(2)
            open_buy.click()

    def open_sell(self):
        open_sell = self.driver.find_element_by_xpath(
            '//*[@id="qa_trading_dealDownButton"]/button')
        try:
            open_sell.click()
        except:
            pop_up = self.driver.find_element_by_xpath(
                '//*[@id="analytics-demo"]/button')
            pop_up.click()
            sleep(2)
            open_sell.click()

    def checkbalance(self):
        balance = self.driver.find_element_by_xpath(
            '//*[@id="qa_trading_balance"]').text
        balance = balance.replace('Rp', '')
        balance = balance.replace('₮', '')
        balance = balance.replace(',', '')
        balance = balance[:-3]
        balance = int(balance)
        return balance


start = BinomoBot()
start.login()

for s in range(120):
    print(120-s, "Second Left")
    sleep(1)

# get our first current balance
start.autoclick(compensation[compen_index])
current_balance = start.checkbalance()
previous_balance = current_balance


# Keep looping until we tell it to stop
while Iterate == True:
    current_second = datetime.now().second
    if current_second == 38:
        current_balance = start.checkbalance()
        # check whether if compensation index isout of bonds
        if compen_index < len(compensation)-1:
            # If loss, go to next compensation
            if current_balance < previous_balance:
                compen_index = compen_index+1
            elif current_balance == previous_balance:
                compen_index = compen_index
            # If win, restart the compensation's index
            else:
                compen_index = 0
        else:
            compen_index = 0
            if current_balance > 500000:
                Iterate = False

        # save the previous balance's value
        previous_balance = current_balance

        start.autoclick(compensation[compen_index])
