# write a script in which scrapes the dynamic values  every 2 sec,
# saves each value  in a different  text file
# a text file should be generated in file directory, 
#the name of each file will reflect the current date time 

from selenium import webdriver
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"] )
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """extract only temperture"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element("xpath", "/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())

