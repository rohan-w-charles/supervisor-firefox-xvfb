from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from xvfbwrapper import Xvfb
vdisplay = Xvfb(width=1280, height=740, colordepth=16)
vdisplay.start()
browser = webdriver.Firefox()
browser.get("https://www.google.com/")
browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("smgt")
browser.find_element_by_xpath('//*[@id="hplogo"]').click()
browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]').click()
print(browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]//a").get_attribute("href"))
browser.close()
vdisplay.stop()
