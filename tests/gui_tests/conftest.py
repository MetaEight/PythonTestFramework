import os

import allure
import pytest
from allure_commons.types import AttachmentType

from utils.config_browser import BrowserConfig


# Generating a report when a test fails
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    """ pytest --option variables from shell
        --env:
            local: Run tests in local environment
            remote: Run tests in selenoid environment
        --browser:
            chrome= Run tests with Chrome driver.
            firefox= Run tests with Firefox driver.
        """
    parser.addoption('--env', default='local')
    parser.addoption('--headless', default='true')
    parser.addoption('--browser', default='chrome')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["browser"] = config.getoption('browser')


@pytest.fixture()
def driver(request):
    driver = BrowserConfig().select_browser()
    driver.maximize_window()
    yield driver

    if request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=AttachmentType.PNG)
        except:
            pass
    driver.quit()
