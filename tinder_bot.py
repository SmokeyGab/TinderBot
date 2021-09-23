#Importing selenium and time module

from selenium import webdriver
from time import sleep

#Excluding switches to overlook "bluetooth adapter" error

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);

#Here is the bot class with all the functions

class TinderBot():

    #Like counter variable for implementing like counting
    like_counter = 0

    #Initialization function that opens up chrome with webdriver for selenium to interact with
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    #Apparently getting the button by xpath isn't viable as the id changed so to use it you must manually find the xpath of the elements
    #Also note that tinder.com is a responsive web page so the size of the windows determines the xpath
    #TODO: find a permanent way to locate the button that doesnt involve changing variables such as 'Xpath'
    #TODO: Rename functions and get all functions for all possible windows sizes so that window may be whatever size the user wants for the bot to function



    #Login function that uses selenium to get the chrome instance to visit tinder.com and click on the login button on the tinder page
    #TODO: Add a sleep timer that checks if button is visible before clicking it
    def login(self):
        self.driver.get('https://tinder.com')
        login_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()

    #Like function that clicks the like button on a profile
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_btn.click()

    #Other like function that clicks on the like button on a profile in a different window size
    def other_like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_btn.click()

    #Like function for the first profile as it is a different like button from the following profiles
    def first_like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_btn.click()

    #Like function for the first profile but with a different window size
    def other_first_like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')

    #Function for closing a popup
    def no_ty_pop_like(self):
        no_ty_pop = self.driver.find_element_by_xpath('//*[@id="o-1268705039"]/div/div/button[2]')
        no_ty_pop.click()

    #Function for closing the match popup
    def close_match(self):
        close_match_btn = self.driver.find_element_by_xpath('//*[@id="o-1268705039"]/div/div/div/div/div[4]/button')
        close_match_btn.click()

    #Function for closing another popup
    def popup_close(self):
        popup = self.driver.find_element_by_xpath('//*[@id="o-1268705039"]/div/div/div[2]/button[2]')
        popup.click()

    #Autoswipe function that takes all the above functions and tries each one starting with the most common one
    #TODO: Sleep until button is visible with some variance to avoid bot detection instead of a hard 2 seconds.
    #TODO: Switch based on visible elements instead of a try/except tree
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


