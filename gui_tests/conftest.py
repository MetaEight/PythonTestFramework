import pytest
from selenium import webdriver
import allure

from allure_commons.types import AttachmentType


# Generating a report when a test fails
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# Webdriver setting
@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(
        executable_path="drivers/chromedriver.exe")
    driver.maximize_window()
    yield driver
    # If the test fails, save the screenshot
    if request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=AttachmentType.PNG)
        except:
            pass
    driver.quit()
