import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.quit()

def test_open_homepage(driver):
    driver.get("https://www.iamdave.ai/")
    WebDriverWait(driver, 10).until(EC.title_contains("DaveAI"))
    assert "DaveAI" in driver.title
    print("✅ Homepage loaded")

def test_click_book_demo(driver):
    book_demo_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/section[1]/div/div[3]/div/div/div/div/a"))
    )
    book_demo_btn.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Book Demo"))
    print("✅ Book Demo clicked")

def test_form_submission(driver):
    # Wait for form (using ID as safer locator than name)
    form = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='post-4112']/div/section[2]/div/div/div/div/div/div/section[1]/div/div[2]/div/div[4]/div/form"))  # Replace with actual ID
    )

    # Fill fields
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div[1]/div[2]/article/div/section[2]/div/div/div/div/div/div/section[1]/div/div[2]/div/div[4]/div/form/div/div[1]/input").send_keys(
        "Test User")
    driver.find_element(By.XPATH, '//*[@id="form-field-email"]').send_keys("newuser@example.com")
    driver.find_element(By.XPATH, '//*[@id="form-field-field_93bc8cc"]').send_keys("xyz company")
    driver.find_element(By.XPATH, '//*[@id="form-field-field_597bd0b"]').send_keys("6666666777")

    # Submit the form
    driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Submit')]]").click()

    # Print confirmation
    print("✅ Form submitted")
