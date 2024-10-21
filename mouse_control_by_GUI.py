from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import math

# Disable PyAutoGUI's fail-safe feature
pyautogui.FAILSAFE = False

# Set up the Selenium WebDriver (you'll need to download the appropriate driver for your browser)
driver = webdriver.Chrome()  # Or webdriver.Firefox() if you're using Firefox

# Maximize the browser window
driver.maximize_window()

# Navigate to the game URL
print("Navigating to the game URL...")
driver.get("https://matrix67.itch.io/pi-day-challenge?s=35")

# Wait for the "Run Game" button to be clickable and then click it
print("Waiting for 'Run Game' button...")
wait = WebDriverWait(driver, 10)
button_selector = "button.button.load_iframe_btn"
run_game_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))

print("Clicking 'Run Game' button...")
run_game_button.click()

# Wait for the game to load (you might need to adjust this time)
print("Waiting for game to load...")
time.sleep(10)

# Get the screen size and calculate the center
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2

# Convert 5cm to pixels (assuming a standard 96 DPI screen)
radius_cm = 5
radius_pixels = int(radius_cm * 37.7952755906)  # 1 cm = 37.7952755906 pixels at 96 DPI

# Move to the starting position
print(f"Moving to starting position: ({center_x + radius_pixels}, {center_y})")
pyautogui.moveTo(center_x + radius_pixels, center_y, duration=2)

# Press and hold the left mouse button
print("Pressing mouse button...")
pyautogui.mouseDown()

# Draw the circle
print("Drawing the circle...")
steps = 100
for i in range(steps + 1):
    angle = 2 * math.pi * i / steps
    x = center_x + int(radius_pixels * math.cos(angle))
    y = center_y + int(radius_pixels * math.sin(angle))
    print(f"Moving to: ({x}, {y})")
    pyautogui.moveTo(x, y, duration=0.1)

# Release the mouse button
print("Releasing mouse button...")
pyautogui.mouseUp()

# Wait for a moment to see the result
# print("Waiting to see the result...")
# time.sleep(5)
print("The browser window will remain open.")
print("Press Enter to close the browser and end the script.")

# Wait for user input before closing the browser
input()

# Close the browser
print("Closing the browser...")
driver.quit()

print("Script completed!")
