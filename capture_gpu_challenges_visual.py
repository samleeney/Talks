import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--window-size=850,650")  # Set window size

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

# Get the absolute path to the HTML file
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "gpu_challenges_visual.html")
file_url = f"file://{html_path}"

# Navigate to the HTML file
driver.get(file_url)

# Wait for the page to fully render
time.sleep(1)

# Create images directory if it doesn't exist
images_dir = os.path.join(current_dir, "images")
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Create gpu_challenges directory if it doesn't exist
gpu_challenges_dir = os.path.join(images_dir, "gpu_challenges")
if not os.path.exists(gpu_challenges_dir):
    os.makedirs(gpu_challenges_dir)

# Take a screenshot and save it
screenshot_path = os.path.join(gpu_challenges_dir, "gpu_programming_challenges_visual.png")
driver.save_screenshot(screenshot_path)

print(f"Screenshot saved to: {screenshot_path}")

# Close the driver
driver.quit()