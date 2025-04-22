from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Menu import Menu
from time import sleep
import io
from PIL import Image

def getname():
    return "Gazi"


def run():

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (often needed for headl
    chrome_options.add_argument('window-size=2560x1440')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://mediko.gazi.edu.tr/view/page/20412")

    sleep(2)
    #"/html/body/div[2]/div/div[2]/div/div[2]/table[1]/tbody"
    #/html/body/div[2]/div/div[2]/div/div[2]
    screenshot = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]")
    driver.execute_script("document.body.style.zoom='82%'")
    driver.execute_script("arguments[0].scrollIntoView();", screenshot)
    screenshot.screenshot("download_folder/gazi.png")


    driver.quit()

    # Open the image
    image = Image.open("download_folder/gazi.png")

    # Get the dimensions of the image
    width, height = image.size

    crop_box = (0, 70, width, height-10)

    # Crop the image
    cropped_image = image.crop(crop_box)

    # Save the cropped image
    cropped_image.save("download_folder/gazi.png")

    menu_listesi = []

    menu_listesi.append(Menu.fotoile(foto="download_folder/gazi.png"))

    return menu_listesi