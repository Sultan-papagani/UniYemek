import json
import Ankara
import Gazi
import Hacettepe
import Istanbul
import Odtu


universiteler = [Ankara, Gazi,Hacettepe,Istanbul,Odtu] 


for name in universiteler:
    menu = name.run()
    uni_adi = name.getname()

    if menu[0].foto != None:
        #bu bir foto.
        veri = {}

        veri[uni_adi] = menu[0].foto

        json_data = json.dumps(veri, indent=4 , ensure_ascii=False)
        with open(f"download_folder/{uni_adi}.json", "w+", encoding='utf-8') as outfile:
            outfile.write(json_data)

    else:

        veri_dis = {}

        index = 0
        for yemek_listesi in menu:

            veri = {}

            veri["tarih"] = yemek_listesi.tarih.strftime('%d/%m/%Y')
            veri["yemekler"] = yemek_listesi.yemekler

            veri_dis["menu"+str(index)] = veri
            index += 1

        json_data = json.dumps(veri_dis, indent=4 , ensure_ascii=False)
        with open(f"download_folder/{uni_adi}.json", "w+", encoding='utf-8') as outfile:
            outfile.write(json_data)

    print(uni_adi +" biti")


