import urllib.request
import os
from time import sleep
import pandas as pd
from Menu import Menu

def getname():
    return "Ankara"

def run():

    PATH = "download_folder/ankara_yemek_liste.xlsx"

    os.remove(PATH)
    urllib.request.urlretrieve("https://sksbasvuru.ankara.edu.tr/kayit/moduller/yemeklistesi/aylikmenu.php", PATH)

    document = pd.read_excel(PATH)

    menu_listesi = []

    for i in range(3, 7+1):
        satir = document.iloc[i]
        tarih = satir.iloc[0]
        if satir.iloc[1] == "ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR":
            menu_listesi.append(Menu(_datetime=tarih, yemekler="ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR"))
        else:
            print(satir.iloc[1], " ", satir.iloc[2],  " ",satir.iloc[3], " ", satir.iloc[4],  " ",satir.iloc[5])
            menu_listesi.append(Menu(_datetime=tarih, yemekler=satir.iloc[1]+satir.iloc[2]+satir.iloc[3]+satir.iloc[4]+satir.iloc[5]))

    for i in range(9, 13+1):
        satir = document.iloc[i]
        tarih= satir.iloc[0]
        if satir.iloc[1] == "ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR":
            menu_listesi.append(Menu(_datetime=tarih, yemekler="ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR"))
        else:
            menu_listesi.append(Menu(_datetime=tarih, yemekler=satir.iloc[1]+satir.iloc[2]+satir.iloc[3]+satir.iloc[4]+satir.iloc[5]))

    for i in range(15, 19+1):
        satir = document.iloc[i]
        tarih= satir.iloc[0]
        if satir.iloc[1] == "ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR":
            menu_listesi.append(Menu(_datetime=tarih, yemekler="ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR"))
        else:
            menu_listesi.append(Menu(_datetime=tarih, yemekler=satir.iloc[1]+satir.iloc[2]+satir.iloc[3]+satir.iloc[4]+satir.iloc[5]))

    for i in range(21, 25+1):
        satir = document.iloc[i]
        tarih= satir.iloc[0]
        if satir.iloc[1] == "ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR":
            menu_listesi.append(Menu(_datetime=tarih, yemekler="ÖĞRENCİ KONSEYİ ANKETİYLE BELİRLENECEKTİR"))
        else:
            menu_listesi.append(Menu(_datetime=tarih, yemekler=satir.iloc[1]+satir.iloc[2]+satir.iloc[3]+satir.iloc[4]+satir.iloc[5]))

    return menu_listesi
