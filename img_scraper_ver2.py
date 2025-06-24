import time
import os
import requests
import shutil
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_imgs(link, platform):

    driver_path = "chromedriver-win64/chromedriver.exe"

    if platform == "gumtree":
        parent_xpath = "/html/body/div[2]/div[1]/div/main/div[3]"
        accept_button = True
        accept_button_xpath = "/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[1]"
    elif platform == "autotrader":
        parent_xpath = "/html/body/div[2]/main"
        accept_button = True
        accept_button_xpath = "/html/body/div/div[2]/div[4]/button[3]"
    elif platform == "ebay":
        parent_xpath = "/html/body/div[2]/main/div[1]/div[1]/div[4]"
        accept_button = False
    elif platform == "motors":
        parent_xpath = "/html/body/section/section"
        accept_button = False


    elif platform == "cargurus":
        parent_xpath = "/html/body/main/div[2]/div/div[2]/div[2]/div/div"
        accept_button = False
        accept_button_xpath = "/html/body/div/div[2]/div[4]/button[3]"

    elif platform == "heycar":
        parent_xpath = "/html/body/div[1]/div[1]/main/div[2]/div[1]/div[1]/div[1]/div"

        accept_button = True
        accept_button_xpath = "/html/body/div[3]/div/div/div/div[2]/div/button[2]"

    elif platform == "aa":
        parent_xpath = "/html/body/div[1]/div[3]/main/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]"
        accept_button = True
        accept_button_xpath = "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[3]"
    
    elif platform == "exchangeandmart":
        parent_xpath = "/html/body/div[3]/div/div/form[1]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]"
        accept_button = True
        accept_button_xpath = "/html/body/div/div[2]/div[6]/button[2]"

    options = Options()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    try:
        if accept_button:
            button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH,accept_button_xpath)))
            button.click()
    except:
        print("didint need to accept")
    #get first images
    
    image_tags = driver.find_elements(By.XPATH, f"{parent_xpath}//img")

    img_urls = []
    for img in image_tags:
        url = img.get_attribute("src") or img.get_attribute("data-src") or img.get_attribute("srcset")
        if url:
            # Handle srcset: split and use the first URL
            if "," in url:
                url = url.split(",")[0].split()[0]
            img_urls.append(url)

    #create directory/folder
    if os.path.exists("car_images"):
        shutil.rmtree("car_images")
    os.makedirs("car_images")
    print(img_urls)
    #store imgs in the folder
    for i, url in enumerate(img_urls):
        try:
            response = requests.get(url)
            with open(f"car_images/image_{i+1}.jpg", "wb") as f:
                f.write(response.content)
            print(f"✅ Saved image_{i+1}.jpg")
        except Exception as e:
            print(f"❌ Failed to download {url}: {e}")




get_imgs("https://heycar.com/uk/auto/audi-a1-2022-25-tfsi-sport-5dr-s-tronic-6a4caec2", "heycar")