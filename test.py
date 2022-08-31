from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver

def open_brower(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    sleep(5)
    driver.close()

if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.binary_location = r'D:\Google chrome\Google\Chrome\Application\chrome.exe'
    option.binary_location = r'C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.1\bin\chromedriver.exe'


