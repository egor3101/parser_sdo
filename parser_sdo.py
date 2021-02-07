from selenium import webdriver
from time import sleep

option = webdriver.FirefoxOptions()
option.headless = True

browser = webdriver.Firefox(options = option)
browser.get("https://sdo.rgsu.net/")

sign_in_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/span/div/div/a").click()
sleep(1)

login_field = "/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[1]/input"
password_field ="/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[2]/input"

browser.find_element_by_xpath(login_field).send_keys("DmitrievED0201680")
browser.find_element_by_xpath(password_field).send_keys("evD5VtQH")
browser.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[3]/input[1]").click()
sleep(2.5)
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/a/span").click()
sleep(2.5)

status = browser.find_elements_by_class_name("lesson-status-tab")
for x in status:
    print(x.get_attribute("innerHTML"))

