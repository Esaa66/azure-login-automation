from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to Edge WebDriver
edge_driver_path = r"C:\Users\Ahmad\Downloads\edgedriver_win64\msedgedriver.exe"

# Create a Service object
service = Service(executable_path=edge_driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Edge(service=service)

try:
    # Step 1: Open Azure Login Page
    azure_login_url = "https://portal.azure.com/"
    driver.get(azure_login_url)
    time.sleep(4)  # Allow page to load

    # Step 2: Enter Username
    username_field = driver.find_element(By.NAME, "loginfmt")  # Adjust if needed
    username = "My_username_here"  # Replace with your username
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Allow transition to password field

    # Step 3: Enter Password
    password_field = driver.find_element(By.NAME, "passwd")  # Adjust if needed
    password = "My_password_here"  # Replace with your password
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(15)  # Allow for login process

    print("Login process complete!")

except Exception as e:
    print(f"An error occurred: {e}")


