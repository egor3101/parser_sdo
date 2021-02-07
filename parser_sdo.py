from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

option = webdriver.FirefoxOptions()
option.headless = True
browser = webdriver.Firefox(options=option)


def actions_on_site(browser):
    browser.get("https://sdo.rgsu.net/")
    sign_in_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/span/div/div/a").click()
    sleep(2)

    login_field = "/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[1]/input"
    password_field = "/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[2]/input"

    browser.find_element_by_xpath(login_field).send_keys("DmitrievED0201680")
    browser.find_element_by_xpath(password_field).send_keys("evD5VtQH")
    browser.find_element_by_xpath(
        "/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[3]/input[1]").click()
    sleep(2.5)
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/a/span").click()
    sleep(2.5)
    objects_name = browser.find_elements(By.ID, "lesson_title")
    for x in objects_name:
        print(x.text)


def output(browser):
    status = browser.find_elements_by_class_name("lesson-status-tab")
    file = open("data.txt", "w")
    for x in status:
        file.write(x.get_attribute("innerHTML") + '\n')
    file.close()


actions_on_site(browser)
output(browser)
