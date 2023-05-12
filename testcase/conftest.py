
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import pytest_html
@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


#******************************* pytest html report *************************

# it is hook for adding  envirement info to report

def pytest_configure(config):
    config._metadata["Porject Name"]='commerce'
    config._metadata["Module Name"] = 'customers'
    config._metadata["Tester"] = 'Hanen Dhifi'
# it is hook for modify/delete  envirement info to report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

