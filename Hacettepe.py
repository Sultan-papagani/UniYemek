from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Menu import Menu
from time import sleep

def getname():
    return "Hacettepe"


def run():

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (often needed for headl
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://sksdb.hacettepe.edu.tr/bidbnew/grid.php?parameters=qbapuL6kmaScnHaup8DEm1B8maqturW8haidnI%2Bsq8F%2FgY1fiZWdnKShq8bTlaOZXq%2BmwWjLzJyPlpmcpbm1kNORopmYXI22tLzHXKmVnZykwafFhImVnZWipbq0f8qRnJ%2BioF6go7%2FOoplWqKSltLa805yVj5agnsGmkNORopmYXam2qbi%2Bo5mqlXRrinJdf1BQUFBXWXVMc39QUA%3D%3D")

    sleep(3)

    element = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]")

    bolunmus_yazi = element.text.split("\n")
    tarih_indexler = []

    menu_listesi = []

    for i in range(len(bolunmus_yazi)):
        if bolunmus_yazi[i] == "* Alerjen Listesi (A-N)":
            tarih_indexler.append(i-1)

    for i in range(len(tarih_indexler)):

        try:

            last_index = 0

            if i == len(tarih_indexler) - 1:
                last_index = None
            else:
                last_index = tarih_indexler[i+1]


            menu_yemek = ""

            for x in bolunmus_yazi[tarih_indexler[i]+2:last_index]:
                menu_yemek += x+"\n"

            bugun = bolunmus_yazi[tarih_indexler[i]][:10]

            if len(bugun[:bugun.find(".")]) <= 1:
                # tarihteki günün başına 0 ekle
                bugun = "0"+bugun

            menu_listesi.append(Menu.stringtarih(bugun.strip(), menu_yemek))
        except Exception as e:
            # son gün

            bugun = bolunmus_yazi[tarih_indexler[i]][:10]

            if len(bugun[:bugun.find(".")]) <= 1:
                # tarihteki günün başına 0 ekle
                bugun = "0"+bugun

            print("Hata at: " + str(i))
            print("Hata Mesaji: ",end="")
            print(e)
            print("parslanan tarih: " + bugun.strip())

            pass

    driver.quit()

    return menu_listesi
