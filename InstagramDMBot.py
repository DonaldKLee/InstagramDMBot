from selenium import webdriver
# To wait for side load
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Allows us to use keyboard keys
from selenium.webdriver.common.keys import Keys
import time

myemail = ""                # Enter in your email for Instagram inside the quotation marks
mypassword = ""             # Enter in your password for Instagram inside the quotation marks
friendusernames = [""]      # Enter in the username of the recipient inside the quotation marks! To send this to mutiple users, seperate users by commas! Ex)  friendusernames = ["@friend1", "@friend2", "@friend3"]
numoftimes = ""             # Enter in the number of times you would like to send the message to the recipient Ex) "2"

# The message being sent
message = ""

PATH = ""                   # Step 4 of the installations instructions

driver = webdriver.Chrome(PATH)

url = "https://www.instagram.com/"
driver.get(url)

try:
    try:
        # Waits for the login box to appear on the webpage
        usernamebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        # Login to Instagram
        usernamebox.send_keys(myemail)
        passwordbox = driver.find_element_by_name('password')
        passwordbox.send_keys(mypassword)
        loginbutton = driver.find_element_by_css_selector('.Igw0E')
        loginbutton.click()
        print("Logging in")
    except:
        print("Could not login!")

    try:
        dmbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xWeGp')))
        dmbtn.click()
    except:
        print ("Could not find or click the direct message button")

    try:
        notificationsnotnow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.HoLwm')))
        notificationsnotnow.click()
    except:
        print ("Could not click not now on the notifications pop up!")

    for friendusername in friendusernames:
        try:
            searchuser = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.EQ1Mr')))
            searchuser.click()
        except:
            print ("Could not click on the new message button!")
        try:
            searchuserbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.j_2Hd')))
            searchuserbox.send_keys(friendusername)
        except:
            print ("Could not find the enter username box!")

        try:
            time.sleep(2)
            firstuser = driver.find_element_by_css_selector('.HVWg4')
            firstuser.click()
        except:
            print("Could not click on the first user!")

        try:
            pressingnext = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rIacr')))
            pressingnext.click()
        except:
            print ("Could not press \"Next\"!")

        try:
            messagebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.focus-visible')))
            messagebox.click()
        except:
            print ("Could not find the text box!")

        try:
            # Finds the text box
            textbox = driver.find_element_by_css_selector('.focus-visible')
        except:
            print("Could not find the text box!")

        try:
            # Sends the message
            for i in range(int(numoftimes)):
                textbox.send_keys(message)
                textbox.send_keys(Keys.RETURN)
        except:
            print("Error sending the message!")

except:
    print("An error has occurred")
    time.sleep(1)
    driver.quit()