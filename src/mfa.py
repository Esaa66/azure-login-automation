from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyotp
import time

# Path to Edge WebDriver
edge_driver_path = r"C:\Users\Ahmad\Downloads\edgedriver_win64\msedgedriver.exe"

# Replace this with TOTP secret key from the authenticator app
totp_secret = "My_TOTP_SECRET_HERE"

def perform_mfa(driver):
    try:
        # Generate the current TOTP code
        totp = pyotp.TOTP(totp_secret)
        mfa_code = totp.now()
        print(f"Generated TOTP: {mfa_code}")

        # Wait for the MFA input field to appear
        time.sleep(5)  # Adjust based on application's behavior

        # Locate the MFA input field
        mfa_input = driver.find_element(By.NAME, "mfaCode") 
        mfa_input.send_keys(mfa_code)
        mfa_input.send_keys(Keys.RETURN)

        # Wait for the login process to complete
        time.sleep(5) 
        print("MFA code submitted successfully!")
    except Exception as e:
        print(f"An error occurred during MFA submission: {e}")

if __name__ == "__main__":
    # Initialize Edge WebDriver
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)
    
    try:
        # Navigate to the login page
        azure_login_url = "https://portal.azure.com/"
        driver.get(azure_login_url)
        time.sleep(4)  # Wait for the page to load

        # Perform the username and password steps
        username_field = driver.find_element(By.NAME, "loginfmt")
        username_field.send_keys("My_username@example.com")
        username_field.send_keys(Keys.RETURN)
        time.sleep(2)

        password_field = driver.find_element(By.NAME, "passwd")
        password_field.send_keys("My_password_here")
        password_field.send_keys(Keys.RETURN)
        time.sleep(15)

        # Perform the MFA step
        perform_mfa(driver)

        print("Login process complete!")

    finally:
        # Keep the browser open for debugging purposes
        pass  # Do not quit the driver unless needed
