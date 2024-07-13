import pyautogui
import time

def open_browser():
    # Open the browser (assumes Chrome is pinned to the taskbar at position 1)
    pyautogui.hotkey('win', '1')
    time.sleep(2)  # Wait for the browser to open

def navigate_to_gmail():
    pyautogui.typewrite('https://mail.google.com/')
    pyautogui.press('enter')
    time.sleep(5)  # Wait for Gmail to load

def log_in(email, password):
    # Type email
    pyautogui.typewrite(email)
    pyautogui.press('enter')
    time.sleep(3)  # Wait for the password field to appear

    # Type password
    pyautogui.typewrite(password)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for Gmail to log in

def mark_unread_as_read():
    # Locate and click on the "Unread" filter (adjust if necessary)
    pyautogui.click(pyautogui.locateCenterOnScreen('unread_filter.png'))
    time.sleep(3)  # Wait for the filter to apply

    # Select all unread emails (adjust coordinates if necessary)
    pyautogui.click(100, 200)  # Coordinates for the "Select all" checkbox
    time.sleep(1)

    # Mark as read (adjust coordinates if necessary)
    pyautogui.click(150, 150)  # Coordinates for the "Mark as read" button
    time.sleep(2)

if __name__ == "__main__":
    email = '******'
    password = '*****'

    open_browser()
    navigate_to_gmail()
    log_in(email, password)
    mark_unread_as_read()
