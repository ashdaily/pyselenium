import argparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LinkedIn:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.driver = webdriver.Chrome()

    def get_password(self):
        return self.__password

    def login(self):
        self.driver.get("https://www.linkedin.com/login")

        username = self.driver.find_element_by_id("username")
        username.send_keys(self.username)
        
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.get_password())
        password.send_keys(Keys.RETURN)      


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='linkedin username', type= str)
    parser.add_argument('--password', help='linkedin password', type= str)
    args = parser.parse_args() 

    account = LinkedIn(args.username, args.password)
    account.login()