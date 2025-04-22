
document.getElementsByName("universite-secim")[0].addEventListener('change', function() {
    UniversiteDegistir(this.value);
});

document.getElementsByName("ogun-secim")[0].addEventListener('change', function() {
    OgunDegistir(this.value);
});

document.getElementsByName("tarih-secim")[0].addEventListener('change', function() {
    TarihDegistir(this.value);
});


function fetchTableData(universiteIndex){
    const uniAdlari = ["Hacettepe","Odtu","Istanbul", "Ankara", "Gazi"];
    let ad = uniAdlari[universiteIndex];
    return fetch("./download_folder/"+ad+".json").then(response => response.json());
}

function UniversiteDegistir(index)
{

    document.getElementById("sonuc_alani").innerHTML = "";

    fetchTableData(index).then(jsonData => {
        for (let key in jsonData)
        {
            let yemek_yazi = jsonData[key]["yemekler"].replace("\n\r", "<br>");
            document.getElementById("sonuc_alani").innerHTML += "<div class='menu_item'>\
                            <p class='acik_yazi' style='font-size: 1.2em;'>"+jsonData[key]["tarih"]+"</p>\
                            <p class='acik_yazi' style='padding-left: 2rem; padding-top: 1rem; white-space: pre-wrap;'>"+yemek_yazi+"</p></div>";
        }
    });

}

function OgunDegistir(index)
{
    alert(1);
}

function TarihDegistir(index)
{
    alert("not implemented");
}

UniversiteDegistir(0); // default

/*
document.getElementById("sonuc_alani").innerHTML += "<div class='menu_item'>\
                            <p class='acik_yazi' style='font-size: 1.2em;'>"+jsonData[key]["tarih"]+"</p>\
                            <ul style='list-style-type:disc; padding-left: 2rem; padding-top: 1rem;'>\
                            <li class='acik_yazi'>"+jsonData[key]["yemekler"]+"</li></ul></div>"
 */