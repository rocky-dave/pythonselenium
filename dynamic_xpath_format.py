from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


class DynamicXPathFormat():

    def test(self):
        driverLocation = "/Users/Rocky/Desktop/Selenium/ Python_Selenium/chromedriver 2"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com")
        driver.implicitly_wait(10)

        # Login -> Lecture "How to click and type on a web element"
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("Javascript")

        time.sleep(3)

        # Select Course
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(),'{0}')]"  # can add a , '{1}' and then define string in _courseLocator
        _courseLocator = _course.format("JavaScript for beginners")  # replaces the 0 in the curly brace

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()

        time.sleep(5)

gc = DynamicXPathFormat()
gc.test()



