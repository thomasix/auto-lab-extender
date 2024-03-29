import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

username = os.environ.get('LAB_USERNAME')
password = os.environ.get('LAB_PASSWORD')

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://awsacademy.instructure.com/login/canvas')
print(driver.title)
driver.find_element("id", 'pseudonym_session_unique_id').send_keys(username)
driver.find_element("id", 'pseudonym_session_password').send_keys(password)
driver.find_element("id", 'login_form').submit()
print(driver.title)

driver.get('https://awsacademy.instructure.com/courses/33379/modules/items/2785620')
print(driver.title)
# Wait for 30 seconds
driver.implicitly_wait(30)
# switch to the iframe
driver.switch_to.frame(driver.find_element("id", "tool_content"))
print(driver.title)
#click launchclabsbtn button 
driver.find_element("id", 'launchclabsbtn').click()

# Wait for 30 seconds
driver.implicitly_wait(30)

# Open aws details
driver.find_element("id", "detailbtn2").click()
# Wait for 30 seconds
driver.implicitly_wait(30)

# Open aws details
try:
    driver.find_element("id", "clikeyboxbtn").click()
except:
    driver.find_element("id", "clikeyboxbtn").click()
# Wait for 30 seconds
driver.implicitly_wait(30)

# get text from text area
credentials = driver.find_element("id", "clikeybox").find_element("tag name", "span").text

# Write credentials to file
os.makedirs(os.path.dirname(".aws/credentials"), exist_ok=True)
with open(".aws/credentials", "w") as f:
    f.write(f"{credentials}\n")
# switch back to the main window
driver.switch_to.default_content()

# Exit
driver.quit()



