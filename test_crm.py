import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_odoo_login_and_open_crm(setup_browser):
    driver = setup_browser
    driver.get("https://cyrus.odoo.com/web/login?redirect=%2Fodoo%3F")
    time.sleep(3)

    # Log in
    driver.find_element(By.ID, "login").send_keys("nityaranjanbarick@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Cyrus@123456")
    driver.find_element(By.XPATH, "//div/button[@type='submit']").click()
    time.sleep(3)

    # Click on CRM
    driver.find_element(By.XPATH, '//*[@id="result_app_3"]/img').click()
    time.sleep(3)

    #Click on NEW button
    driver.find_element(By.XPATH,'//div/button[@type="button"]').click()
    time.sleep(3)

    #click on sales
    driver.find_element(By.XPATH,'(//div/button[@class="fw-normal o-dropdown dropdown-toggle dropdown"])[1]').click()
    sales_iteam=driver.find_elements(By.TAG_NAME,'a')
    for i in sales_iteam:
        print(i.text)
    time.sleep(3)

    #click on reporting
    driver.find_element(By.XPATH,'(//div/button[@class="fw-normal o-dropdown dropdown-toggle dropdown"])[2]').click()
    reporting_iteam =driver.find_elements(By.TAG_NAME,'a')
    for j in reporting_iteam:
        print(j.text)
    time.sleep(3)

    #Click on configuration
    driver.find_element(By.XPATH,"//span[text()='Configuration']").click()
    configuration_iteam = driver.find_elements(By.TAG_NAME,'a')
    for k in configuration_iteam:
        print(k.text)
    time.sleep(3)

    #click on search
    driver.find_element(By.XPATH,'//div/input[@type="text"]').click()
    time.sleep(3)