from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from colorama import *
import random
import keyboard
import sys
import getpass

optionsOpenB = Options()
optionsOpenB.headless = True

current_rate = 68 # start at a rate of 68 beats per minute
fluctuation_sum = 0 # keep track of the total fluctuation over time
stop = False # Define a function to be called when the "q" key is pressed

#  Algorithm

username = 'kang49'
password = getpass.getpass('Enter VRC password: ')

# Initialize webdriver and open VRChat login page
driver = webdriver.Chrome(options=optionsOpenB)
driver.get('https://vrchat.com/home/login')
# Maximize the browser window
driver.execute_script('document.body.requestFullscreen() || document.body.mozRequestFullScreen() || document.body.webkitRequestFullscreen()')

# Fill in login form and submit
login_fill = driver.find_element(By.XPATH, '//*[@id="username_email"]')
login_fill.send_keys(username)

pass_fill = driver.find_element(By.XPATH, '//*[@id="password"]')
pass_fill.send_keys(password)

login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button')
login_button.click()
time.sleep(10)

# Check for and handle two-factor authentication
try:
    twofa_fill = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[2]/div/form/div[3]/input')
    twofa_fill.send_keys(input('Enter 2FA: '))

    twofa_login = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[2]/div/form/div[4]/button')
    twofa_login.click()
    time.sleep(10)
except:
    pass

# Navigate to profile page
driver.get('https://vrchat.com/home/user/')
time.sleep(10)


# Press 'q' to quit.
def on_q_key_pressed(event):
    global stop
    stop = True
    click_status_box = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[3]')
    click_status_box.click() # click to status box

    status_fill = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[3]/input')
    status_fill.send_keys(Keys.BACK_SPACE * 20)
    status_fill.send_keys('HeartRate nan BPM')
    status_fill.send_keys(Keys.ENTER)
    sys.exit()

# Bind the function to the "q" key
keyboard.on_press_key("q", on_q_key_pressed)

# Start listening for key presses
keyboard.hook(on_q_key_pressed)

while True:
    # Generate a random number between -3 and 3
    fluctuation = random.randint(-3, 3)
    # Add the fluctuation to the current heart rate
    heart_rate = current_rate + fluctuation
    # Make sure the heart rate stays within the range of 72-100
    heart_rate = max(72, heart_rate)
    heart_rate = min(100, heart_rate)
    # Add the fluctuation to the sum
    fluctuation_sum += fluctuation
    # If the sum of fluctuations exceeds 10 within a 30-minute period, reset the sum
    if fluctuation_sum > 10 or fluctuation_sum < -10:
        fluctuation_sum = 0
    # If the heart rate is over 80, gradually decrease it
    if heart_rate > 80:
        heart_rate -= 1
    print(f'HeartRate {heart_rate} BPM')
    current_rate = heart_rate

    click_status_box = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[3]')
    click_status_box.click() # click to status box

    status_fill = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[3]/input')
    status_fill.send_keys(Keys.BACK_SPACE * 20)
    status_fill.send_keys(f'HeartRate {heart_rate} BPM')
    status_fill.send_keys(Keys.ENTER)
    time.sleep(10)
    if stop == True:
        break