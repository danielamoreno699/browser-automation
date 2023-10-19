from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#local from selenium.webdriver.chrome.service import Service
# service = Service("absolute path of chromediver.exe")
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"] )
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()

    driver.find_element("id", "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element("id", "id_password").send_keys("automatedautomated" + Keys.RETURN)
    #print(driver.current_url)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)
   

print(main())
