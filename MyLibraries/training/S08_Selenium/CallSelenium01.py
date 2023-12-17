# Selenium tutorial part 1.
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# C:\Program Files (x86)\Google

from configFiles import SelenumConstants
selCD = SelenumConstants()

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
