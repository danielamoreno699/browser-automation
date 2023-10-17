from selenium import webdriver

# Specify the path to the ChromeDriver executable
chromedriver_path = "C:\Users\us\Downloads\chromedriver-win64.zip\chromedriver-win64"

# Initialize a Chrome WebDriver instance
driver = webdriver.Chrome(executable_path=chromedriver_path)