#!/usr/bin/env python3
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys
from random import randint
import logging
import random

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Utilities:
    """
    this class contains all the method related to driver behaviour,
    like scrolling, waiting for element to appear, it contains all static
    method, which accepts driver instance as a argument

    @staticmethod
    def method_name(parameters):
    """

    @staticmethod
    def wait_until_tweets_appear(driver) -> None:
        """Wait for tweet to appear. Helpful to work with the system facing
        slow internet connection issues
        """
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="tweet"]')))
        except WebDriverException:
            logger.exception(
                "Tweets did not appear!, Try setting headless=False to see what is happening")

    @staticmethod
    def scroll_down(driver) -> None:
        """Helps to scroll down web page"""
        try:
            start = time.time()
            body = driver.find_element(By.CSS_SELECTOR, 'body')
            for _ in range(randint(2, 4)):
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(random.uniform(0.2, 0.3))
            print("scroll_down took " + str(time.time()-start));
        except Exception as ex:
            logger.exception("Error at scroll_down method {}".format(ex))

    @staticmethod
    def wait_until_completion(driver) -> None:
        """waits until the page have completed loading"""
        try:
            state = ""
            start = time.time()
            while state != "complete":
                time.sleep(random.uniform(0.1, 0.2))
                state = driver.execute_script("return document.readyState")
            print("wait_until_completion() took " + str(time.time()-start));
        except Exception as ex:
            logger.exception('Error at wait_until_completion: {}'.format(ex))