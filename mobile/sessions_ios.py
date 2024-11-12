from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'https://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platoformVersion': '13.6',
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capacbilities=CAPS
)
driver.quit()