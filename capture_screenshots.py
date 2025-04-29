import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create directory for images if it doesn't exist
os.makedirs("images/gpu_cpu_comparison", exist_ok=True)

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--window-size=800,800")  # Set window size
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the driver with webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Capture CPU operations image
print("Capturing CPU operations image...")
driver.get("file://" + os.path.abspath("cpu_operations.html"))
time.sleep(1)  # Wait for page to fully render
driver.save_screenshot("images/gpu_cpu_comparison/cpu_operations.png")

# Capture GPU operations image
print("Capturing GPU operations image...")
driver.get("file://" + os.path.abspath("gpu_operations.html"))
time.sleep(1)  # Wait for page to fully render
driver.save_screenshot("images/gpu_cpu_comparison/gpu_operations.png")

# Close the driver
driver.quit()

print("Screenshots saved to images/gpu_cpu_comparison/ directory")