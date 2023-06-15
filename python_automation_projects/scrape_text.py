from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\rudua\\Downloads\\chromedriver_win32\\chromedriver.exe')


def get_driver():
    #make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.nasa.gov/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value= "[@id="cards"]/div/div/h2")
    return element.text

print(main())



