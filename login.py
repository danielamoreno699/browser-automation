from selenium import webdriver

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
   

print(main())
