import pyautogui
import time
import os
import keyboard
from tkinter import messagebox, Tk

# Interval between each action (seconds)
interval = 1
# Folder to save screenshots
screenshot_folder = 'screenshots'
# Counter for screenshots
counter = 0

# Create the folder if it doesn't exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Initialize the Tkinter root
root = Tk()
root.withdraw()

# Show initial information messagebox
messagebox.showinfo("Information", "Press 'x' to stop the script.")
time.sleep(1)
while True:
    # Check if 'x' key is pressed to break the loop
    if keyboard.is_pressed('x'):
        # Show stopping messagebox and wait for user to close it
        messagebox.showinfo("Information", "Stopping script...")
        break

    # Take a screenshot
    screenshot_path = os.path.join(screenshot_folder, f'screenshot_{counter + 1}.png')
    pyautogui.screenshot(screenshot_path)

    # Click the specified position on the screen
    pyautogui.press('pgdn')

    # Wait for the interval
    time.sleep(interval)

    # Increment the counter
    counter += 1

# Show final information messagebox
messagebox.showinfo("Information", f'Done! {counter} screenshots saved in "{screenshot_folder}" folder.')

# Destroy the Tkinter root to clean up
root.destroy()
