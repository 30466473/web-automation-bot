import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime

import env.const as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"/Users/kevin.yan/Downloads",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://members.swtc.ca/")

    def get_password(self):
        password = const.password
        return password
    
    def get_username(self):
        username = const.username
        return username

    def set_username(self, user_name):
        user_name_element = self.find_element(By.ID, 'login-form-username')
        user_name_element.clear()
        user_name_element.send_keys(user_name)

    def set_password(self, pass_word):
        pass_word_element = self.find_element(By.ID, 'login-form-password')
        pass_word_element.clear()
        pass_word_element.send_keys(pass_word)
        log_in = self.find_element(By.ID, 'login-form-submit')
        log_in.click()
    
    def select_month(self):
        right = self.find_element(By.CSS_SELECTOR, 'i[class="i-rounded i-small i-light i-alt icon-chevron-right"]')
        right.click()

    def select_date(self,date):
        date_element = self.find_element(By.CSS_SELECTOR, f'button[data-value="{date}"]')
        date_element.click()

    def select_time(self,time_court):
        time_element = self.find_element(By.CSS_SELECTOR, f'button[data-value="{time_court}"]')
        time_element.click()

    def book_submit(self):
        submit_booking = self.find_element(By.ID, 'book-button2')
        submit_booking.click()
        confirm_booking = self.find_element(By.CSS_SELECTOR, 'a[onclick="bookSubmit()"]')
        confirm_booking.click()
    
    def next_month(self):
        target_date = datetime.datetime.now() + datetime.timedelta(days=6)
        target_date_month = target_date.strftime('%Y-%m')
        current_month = datetime.datetime.now().strftime('%Y-%m')
        return target_date_month != current_month



