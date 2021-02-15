from selenium import webdriver
from time import sleep


option = webdriver.FirefoxOptions()
option.headless = False
browser = webdriver.Firefox(options=option)


def actions_on_site():
    browser.get("https://sdo.rgsu.net/")
    sign_in_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/span/div/div/a").click()
    sleep(2)

    login_field = "/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[1]/input"
    password_field = "/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[2]/input"

    browser.find_element_by_xpath(login_field).send_keys("DmitrievED0201680")
    browser.find_element_by_xpath(password_field).send_keys("evD5VtQH")
    browser.find_element_by_xpath(
        "/html/body/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/form/dl/dd[3]/input[1]").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/a/span").click()
    sleep(3)
    # objects_name = browser.find_elements(By.ID, "lesson_title")
    # for x in objects_name:
    #    print(x.text)


def output():
    status = browser.find_elements_by_class_name("lesson-status-tab")
    file = open("new_data.txt", "w")
    for x in status:
        file.write(x.get_attribute("innerHTML") + '\n')
    file.close()
    return status


def check_data(status):
    f = open("new_data.txt", 'r')
    contentA = f.read()
    f.close()
    f = open("old_data.txt", 'r')
    contentB = f.read()
    f.close()

    if contentA == contentB:
        return False
    else:
        file = open("old_data.txt", "w")
        for x in status:
            file.write(x.get_attribute("innerHTML") + '\n')
        file.close()
        return True






