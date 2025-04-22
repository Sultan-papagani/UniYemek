from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Menu import Menu
from time import sleep

def getname():
    return "Istanbul"


def run():

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (often needed for headl
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://sks.istanbul.edu.tr/yemek-listesi")

    sleep(4)

    #kahvaltı /html/body/div[1]/main/div[2]/div/div/div[1]/ul/li[1]
    #öğlen    /html/body/div[1]/main/div[2]/div/div/div[1]/ul/li[2]
    #akşam    /html/body/div[1]/main/div[2]/div/div/div[1]/ul/li[3]
    #vegan    /html/body/div[1]/main/div[2]/div/div/div[1]/ul/li[4]
    ogle_buton = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/ul/li[2]")
    ogle_buton.click()

    sleep (2)

    tablo = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[2]/div/div/table"))
    )

    bolunmus_yazi = tablo.text.split("\n")
    menu_listesi = []

    index = 0
    for yazi in bolunmus_yazi:
        try:
            yazi = yazi.strip()
            if yazi.isdigit():
                # sayi ise bir sonraki menü yazısı olabilir (genelde öyle)
                if index + 1 >= len(bolunmus_yazi) - 1:
                    #sona gelmişiz.
                    break

                if not bolunmus_yazi[index + 1].isdigit():
                    # menü yazısı.
                    menu_listesi.append(Menu.gunile(gun=int(yazi), yemekler=bolunmus_yazi[index + 1].strip()))
            index += 1
        except Exception as e:
            print(e,end=" ")
            print("at: " + str(index))

    driver.quit()

    return menu_listesi