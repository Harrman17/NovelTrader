"""
image_scraper.py

📸 A Python script to automatically scrape and download car listing images from:
    - eBay (product images)
    - AutoTrader UK (car gallery images)

🛠️ Dependencies:
    - Selenium (requires ChromeDriver)
    - requests
    - shutil, os, re, time

📂 Features:
    - Automatically opens browser sessions using Selenium
    - Scrapes all high-resolution images from the provided listing link
    - Saves the images into a cleanly named folder based on the item/car title
    - Handles lazy-loaded and duplicate image scenarios

🔧 Available Functions:
    - create_or_replace_dir(dir_path): Safely recreates a directory
    - get_imgs_ebay(link): Downloads images from an eBay product listing
    - get_imgs_autotrader(link): Downloads car images from an AutoTrader UK listing

Example usage:
    get_imgs_ebay("https://www.ebay.co.uk/itm/example")
    get_imgs_autotrader("https://www.autotrader.co.uk/car-details/example")
"""
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

def create_or_replace_dir(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path)
    
def get_imgs_ebay(link):
    """
    Extracts and downloads all car images from an AutoTrader listing.

    - Opens the image gallery and scrolls to trigger lazy-loading.
    - Scrapes image URLs and saves them locally in a folder named after the car title.

    Args:
        link (str): The URL of the AutoTrader listing.

    Notes:
        - Requires Selenium and ChromeDriver.
        - Handles both <picture> and <img> tags for image retrieval.
    """
    driver_path = "chromedriver-win64/chromedriver.exe"

    options = Options()
    # Comment this if you want to see the browser
    # options.add_argument('--headless')

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(link)
    time.sleep(3)

    # Wait for images to load
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".image-treatment img"))
        )
    except:
        print("❌ Could not find image elements.")
        driver.quit()
        return

    # Extract image URLs
    image_elements = driver.find_elements(By.CSS_SELECTOR, ".image-treatment img")
    image_urls = []

    for img in image_elements:
        url = img.get_attribute("src") or img.get_attribute("data-src")
        if url and "ebayimg.com" in url:
            image_urls.append(url)

    image_urls = list(set(image_urls))  # remove duplicates
    print(f"📸 Found {len(image_urls)} images.")

    # Get car title to use as folder name
    try:
        title = driver.find_element(By.ID, "itemTitle").text
        title = re.sub(r'[^a-zA-Z0-9_-]', '_', title.strip())
    except:
        title = "ebay_car"

    create_or_replace_dir(title)

    # Download images
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            with open(f"{title}/image_{i+1}.jpg", "wb") as f:
                f.write(response.content)
            print(f"✅ Saved image_{i+1}.jpg")
        except Exception as e:
            print(f"❌ Failed to download {url}: {e}")

    driver.quit()

def get_imgs_autotrader(link):
    """
    Extracts and downloads all car images from an AutoTrader listing.

    - Opens the image gallery and scrolls to trigger lazy-loading.
    - Scrapes image URLs and saves them locally in a folder named after the car title.

    Args:
        link (str): The URL of the AutoTrader listing.

    Notes:
        - Requires Selenium and ChromeDriver.
        - Handles both <picture> and <img> tags for image retrieval.
    """
    driver_path = "chromedriver-win64/chromedriver.exe"

    options = Options()
    # Comment this line below to debug visually (i.e., see the browser)
    # options.add_argument('--headless')

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(link)
    time.sleep(2)  # Let base page load

    # Click gallery button safely
    try:
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-testid, 'open-carousel')]"))
        )
        gallery_btn = driver.find_element(By.XPATH, "//button[contains(@data-testid, 'open-carousel')]")
        driver.execute_script("arguments[0].click();", gallery_btn)
        print("✅ Gallery opened")
        time.sleep(2)
    except Exception as e:
        print(f"❌ Failed to open gallery: {e}")

    # Scroll to ensure lazy-loaded images show
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "picture"))
        )
    except:
        print("❌ Image elements did not load.")
        driver.quit()
        return

    pictures = driver.find_elements(By.TAG_NAME, "picture")
    print(f"🔍 Found {len(pictures)} <picture> tags")

    image_urls = []
    for picture in pictures:
        url = None
        try:
            source = picture.find_element(By.TAG_NAME, "source")
            url = source.get_attribute("srcset")
        except:
            try:
                img = picture.find_element(By.TAG_NAME, "img")
                url = img.get_attribute("src")
            except:
                pass

        if url and url.startswith("https://"):
            image_urls.append(url)

    image_urls = list(set(image_urls))  # Remove duplicates
    print(f"📸 Extracted {len(image_urls)} image URLs")

    # Get car name from heading and sanitize
    try:
        car_name = driver.find_element(By.XPATH, "//h1").text
        safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', car_name.strip())
    except:
        safe_name = "car_images"

    create_or_replace_dir(safe_name)

    for i, url in enumerate(image_urls):
        try:
            img_data = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).content
            with open(f"{safe_name}/image_{i+1}.jpg", "wb") as f:
                f.write(img_data)
            print(f"✅ Downloaded image_{i+1}.jpg")
        except Exception as e:
            print(f"❌ Failed to download {url}: {e}")

    driver.quit()


def get_imgs_cargurus(link):

    driver_path = "chromedriver-win64/chromedriver.exe"

    options = Options()
    # Comment this out to see the browser (for debugging)
    # options.add_argument('--headless')

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(link)
    time.sleep(2)

    # Wait for any main image to load
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.vdp__photo"))
        )
    except:
        print("❌ Could not find image elements.")
        driver.quit()
        return

    # Click through image arrows to load all photos
    for _ in range(35):  # up to 35 images
        try:
            next_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Next image')]")
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(0.5)
        except:
            break

    # Get all image URLs
    img_elements = driver.find_elements(By.CSS_SELECTOR, "img.vdp__photo")
    image_urls = []

    for img in img_elements:
        url = img.get_attribute("src")
        if url and "cargurus" in url:
            image_urls.append(url)

    image_urls = list(set(image_urls))
    print(f"📸 Found {len(image_urls)} images.")

    # Get car title to name the folder
    try:
        title = driver.find_element(By.CSS_SELECTOR, "h1").text
        safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', title.strip())
    except:
        safe_name = "cargurus_car"

    create_or_replace_dir(safe_name)

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            with open(f"{safe_name}/image_{i+1}.jpg", "wb") as f:
                f.write(response.content)
            print(f"✅ Saved image_{i+1}.jpg")
        except Exception as e:
            print(f"❌ Failed to download {url}: {e}")

    driver.quit()

get_imgs_cargurus("https://www.cargurus.co.uk/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2412&zip=HA8+0AU#listing=154777506/FEATURED/DEFAULT")