from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);

class TinderBot():
    like_counter = 0

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get('https://tinder.com')
        login_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_btn.click()

    def other_like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_btn.click()

    def first_like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_btn.click()

    def other_first_like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')

    def no_ty_pop_like(self):
        no_ty_pop = self.driver.find_element_by_xpath('//*[@id="o-1268705039"]/div/div/button[2]')
        no_ty_pop.click()

    def close_match(self):
        close_match_btn = self.driver.find_element_by_xpath('//*[@id="o-1268705039"]/div/div/div/div/div[4]/button')
        close_match_btn.click()

    def popup_close(self):
        popup = self.driver.find_element_by_xpath('//*[@id="o-1268705039"]/div/div/div[2]/button[2]')
        popup.click()


    def autoswipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                try:
                    self.other_like()
                except Exception:
                    try:
                        self.no_ty_pop_like()
                    except Exception:
                        try:
                            self.first_like()
                        except Exception:
                            try:
                                self.popup_close()
                            except Exception:
                                self.close_match()


