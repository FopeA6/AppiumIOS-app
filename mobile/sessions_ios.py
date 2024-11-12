from appium import webdriver
from os import path
from appium.options.common import AppiumOptions

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'https://localhost:4723'

# CAPS = {
#     'platformName': 'iOS',
#     'platformVersion': '13.6',
#     'deviceName': 'iPhone 11',
#     'automationName': 'XCUITest',
#     'app': APP,
# }

options = AppiumOptions()
options.platform_name = 'iOS',
options.platform_version = '13.6',
options.device_Name = 'iPhone 11',
options.automation_name = 'XCUITest'
options.app = APP

# options.set_capability('platformName', 'iOS')
# options.set_capability('deviceName', 'iPhone 12')
# options.set_capability('app', APP)



driver = webdriver.Remote(
    command_executor=APPIUM,
    options=options
)
driver.quit()