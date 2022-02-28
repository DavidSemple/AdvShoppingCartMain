import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome(r"C:\Users\david\Desktop\PycharmProjects\advantage_shopping_cart\chromedriver.exe")

def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.advantageshopping_url)
    print(driver.title)
    if driver.current_url == locators.advantageshopping_url and driver.title == " Advantage Shopping":
       print(f'We\'re at Advantage Shopping Homepage -- {driver.current_url}')
       print(f'We\'re seeing title message -- "Advantage Shopping"')
       sleep(1)

def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        sleep(5)
        driver.close()
        driver.quit()
        old_instance = sys.stdout
        log_file = open('message.log', 'w')
        sys.stdout = log_file
        print(f'Email: {locators.email}\nUsername: {locators.new_username}\nPassword: {locators.new_password}\n')
        sys.stdout = old_instance
        log_file.close()


setUp()
tearDown()