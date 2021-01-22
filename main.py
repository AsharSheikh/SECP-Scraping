from flask import Flask, Response
from selenium import webdriver
import os
import time
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
   chrome_options = webdriver.ChromeOptions()
   
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

   driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
   
   driver.set_window_position(0, 0)
   driver.set_page_load_timeout(20)
   driver.implicitly_wait(20)
   driver.get("https://medium.com")
   driver.set_window_size(1920, 1080)

   time.sleep(3)
   
   png = driver.get_screenshot_as_png()
   with open(Response(png, mimetype="image/png"), "rb") as imageFile:
      str = base64.b64encode(imageFile.read())
      
   print("Finished!")
  
   driver.quit()
   
   return str
