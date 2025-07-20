import pytest
import json
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from login_page import LoginPage

with open (r"C:\Users\srikant sahoo\PycharmProjects\MyProject\Datadriven_testing\Pytest_setup1\Orangehrm\data\loginpage.json") as f:
    data=json.load(f)

@pytest.mark.usefixtures('init_driver')
class TestOrangeHRMLogin:


    @pytest.mark.parametrize("credentials",data['valid_credentials'])
    def test_valid_login(self,credentials):
        page=LoginPage(self.driver)
        page.login(credentials['username'],credentials['password'])
        assert "/dashboard" in self.driver.current_url.lower()

    @pytest.mark.negative
    @pytest.mark.parametrize("credentials",data["Invalid_credentials"])
    def test_invalid_credential(self,credentials):
        page = LoginPage(self.driver)
        page.login(credentials['username'], credentials['password'])
        error=page.handle_invalid()
        assert "Invalid" in error.lower()


    @pytest.mark.parametrize("credentials", data["field_required"])
    def test_required_field(self, credentials):
        page = LoginPage(self.driver)
        page.login(credentials['username'], credentials['password'])
        error = page.handle_error()
        assert "Required" in error.lower()

