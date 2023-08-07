# Python Test Automation Framework

Description
=============
Test Automation Framework using selenium and Python with the below features:

* Framework is based on page object model.
* Reporting using Allure report.
* Reading locators and test data from JSON files.


Install dependencies
=====================
* Install Allure-framework
* Install the depended packages in ``requirements.txt`` using ``pip install -r requirements.txt``
* Download chrome webdriver. Create new folder 'drivers' and move driver to it  



Run the tests
==================

Run GUI tests:

``python -m pytest -v -n 2 gui_tests --alluredir=allure_results``

Run API tests:

``python -m pytest -v -n 2 api_tests --alluredir=allure_results``


Generate Allure report
=========================

``allure serve allure_results``
