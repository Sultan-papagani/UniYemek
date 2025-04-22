from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Menu import Menu
from time import sleep

def getname():
    return "Odtu"


def run():

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (often needed for headl
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://portal.odtugvo.k12.tr/yemek/7")

    sleep(4)

    aylik_buton = driver.find_element(By.XPATH, "/html/body/app-root/app-food-front/div[3]/div[1]/div[1]/button[3]")
    aylik_buton.click()

    sleep(4)

    yeni_eleman = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-food-front/div[3]/div[3]"))
    )


    bolunmus_yazi = yeni_eleman.text.split("\n")
    tarih_indexler = []
    menu_listesi = []

    for i in range(len(bolunmus_yazi)):
        if bolunmus_yazi[i].strip() == "Öğle Yemeği":
            tarih_indexler.append(i-1)

    for i in range(len(tarih_indexler)):

        try:

            last_index = 0

            if i >= len(tarih_indexler) - 1:
                last_index = None
            else:
                last_index = tarih_indexler[i+1]

            tarih_yazisi = bolunmus_yazi[tarih_indexler[i]].strip()

            #bir sonraki tarih indexine kadar kopyala

            menu_yemek = ""

            for yazi in bolunmus_yazi[tarih_indexler[i]+1:last_index]:
                menu_yemek += yazi+"\n"

            menu_listesi.append(Menu.stringtarih(tarih_yazisi, menu_yemek))

        except Exception as e:
            print(e,end=" ")
            print("at: " + str(i))

    driver.quit()

    return menu_listesi