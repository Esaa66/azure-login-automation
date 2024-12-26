def read_config(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def create_driver():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    return driver

def wait_for_element(driver, by, value, timeout=10):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def close_driver(driver):
    driver.quit()