

import pytest
from selenium import webdriver

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    bro = ReadConfigurations.read_configuration("basic info","bro")
    driver=None
    if bro.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif bro.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif bro.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info","URL")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()