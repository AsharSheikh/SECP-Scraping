from flask import Flask, Response, request
from selenium import webdriver
import os
import time
from base64 import b64decode

app = Flask(__name__)

@app.route('/')
def hello_world():
   chrome_options = webdriver.ChromeOptions()
   
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")C
   chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
   
   CUIN = request.args.get("cuin", "")
   
   if not CUIN:
        return "Example: <a href='http://secp-scraping.herokuapp.com/?cuin=0155624'>" \
               "http://secp-scraping.herokuapp.com/?cuin=0155624</a>"
      
   driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
   
   driver.set_window_position(0, 0)
   driver.set_page_load_timeout(20)
   driver.implicitly_wait(20)
   driver.get("https://www.secp.gov.pk/company-name-search/company-details/?companyCUIN=" + CUIN)
   driver.set_window_size(1920, 1080)

   time.sleep(3)
   
   src_base64 = driver.get_screenshot_as_base64()
   
      
   print("Finished!")
  
   driver.quit()
   
   return "<img src='data:image/png;base64," + src_base64 + "'/>"
