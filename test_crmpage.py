import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver

    driver.quit()

def test_login_and_open_crm(driver):

    driver.get("https://luliaenterprise1.odoo.com/web/login?redirect=%2Fodoo%3F")
    time.sleep(3)

    email_input = driver.find_element(By.XPATH, "//input[@name='login']")
    email_input.send_keys("srikantsahoo822@gmail.com")

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys("Papigudia@8780")

    login_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
    login_button.click()

    time.sleep(5)

    crm = driver.find_element(By.XPATH, '//*[@id="result_app_3"]/img')
    crm.click()

    time.sleep(3)

    driver.find_element(By.XPATH, '//div/button[@type="button"]').click()
    time.sleep(3)

    # click on sales
    driver.find_element(By.XPATH, '(//div/button[@class="fw-normal o-dropdown dropdown-toggle dropdown"])[1]').click()
    sales_iteam = driver.find_elements(By.TAG_NAME, 'a')
    for i in sales_iteam:
        print(i.text)
    time.sleep(3)

    # click on reporting
    driver.find_element(By.XPATH, '//span[text()="Reporting"]').click()
    reporting_iteam = driver.find_elements(By.TAG_NAME, 'a')
    for j in reporting_iteam:
        print(j.text)
    time.sleep(3)

    # Click on configuration
    driver.find_element(By.XPATH, "//span[text()='Configuration']").click()
    configuration_iteam = driver.find_elements(By.TAG_NAME, 'a')
    for k in configuration_iteam:
        print(k.text)
    time.sleep(3)

    # click on search
    driver.find_element(By.XPATH, '//div/input[@type="text"]').click()
    time.sleep(3)


    assert "crm" in driver.current_url.lower() or "crm" in driver.title.lower()
