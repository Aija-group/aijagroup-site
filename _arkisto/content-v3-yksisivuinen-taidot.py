# -*- coding: utf-8 -*-
"""Äijä Group Oy – yksisivuisen sivuston sisältö. Muokkaa tätä, aja build.py."""

SITE = {
    "name": "Äijä Group Oy",
    "short": "Äijä Group",
    "domain": "https://aijagroup.fi",          # OLETUS – vahvista
    "email": "sulo@aijagroup.fi",              # OLETUS – vahvista
    "linkedin": "",                            # esim. https://www.linkedin.com/in/... – tyhjä = ei näytetä
    "founder": "Sulo Mäki",
    "founder_title": "Perustaja",
    "ytunnus": "",                             # tyhjä = ei näytetä
    "description": "Äijä Group suunnittelee ja rakentaa verkkokauppojen ja D2C-brändien kasvun: positiointi, tarjooma ja myyntiviesti, jotka resonoivat – ja toteutus, joka viedään loppuun asti.",
}

NAV = [("Mitä teemme", "#mita"), ("Miten", "#miten"), ("Kenelle", "#kenelle"), ("Perustaja", "#perustaja")]

HERO = {
    "eyebrow": "Verkkokauppojen ja D2C-brändien markkinointi",
    "h1_a": "Suunnittelemme kasvun.",
    "h1_b": "Ja rakennamme sen.",
    "lead": "Äijä Group suunnittelee vaativia markkinoinnin ja myynnin kokonaisuuksia, jotka palvelevat yrityksen kasvutavoitteita – ja toteuttaa ne. Emme jätä strategiaa kalvoiksi.",
}

# Kolme pilaria – se, mitä Sulo oikeasti osaa
PILLARS = [
    ("Positiointi ja tarjooma",
     "Ensin päätetään, kenelle brändi on ja miksi se valitaan. Siitä johdetaan tarjous, hinnoittelu ja myyntiviesti, jotka aidosti resonoivat kohderyhmälle. Tämä on työn ydin – kaikki muu on sen toteutusta."),
    ("Kokonaisuuden suunnittelu",
     "Kanavat, budjetti, sisällöt, sivusto ja mittarit suunnitellaan yhtenä kokonaisuutena kasvutavoitteesta käsin. Ei erillisiä kampanjoita, vaan järjestelmä, jossa jokainen osa tietää tehtävänsä."),
    ("Toteutus loppuun asti",
     "Ymmärrämme myös tekniikan: mainostilit, mittaus, verkkokauppa-alustat, automaatiot. Siksi rakentamamme strategia myös jalkautuu – meidän käsissämme tai yhdessä tiimisi kanssa."),
]

# Mitä se käytännössä on – yksi tiivis lista, ei omia sivuja
WORK = [
    ("Markkinointistrategia ja positiointi", "Kohderyhmä, positio, tarjooma ja viestihierarkia. Kasvun lähteet ja budjetti."),
    ("Myynti- ja mainosviestit, offerit", "Tarjoukset, kulmat ja copy, jotka testataan oikealla rahalla."),
    ("Mainonta ja liidienhankinta", "Meta, Google, ChatGPT Ads, TikTok – kanava valitaan tavoitteen mukaan."),
    ("Brändimainonta", "Tunnettuus, joka laskee muiden kanavien hintaa. Mitataan brändihausta ja konversiosta."),
    ("Orgaaninen some ja sisältö", "Sisältöstrategia, konseptit ja tuotannon ohjaus, jotka kytkeytyvät myyntiin."),
    ("Sähköposti ja asiakkuuden pito", "Klaviyo-automaatiot, elinkaarimarkkinointi, uusintaostot."),
    ("Verkkokauppa- ja sivustoprojektit", "Shopify-verkkokaupat, laskeutumissivut ja sivustot, jotka myyvät."),
    ("Mittaus ja raportointi", "GA4, konversiomittaus, kate- ja LTV-pohjainen optimointi. Raportit liiketoiminnan luvuilla."),
]

# Miten – kolme tapaa työskennellä
MODELS = [
    ("Kartoitus", "Käymme läpi numerot, markkinoinnin ja sivuston ja sanomme suoraan, missä kasvu jumittaa ja mitä tekisimme. Kiinteä hinta."),
    ("Projekti", "Rajattu kokonaisuus: strategia ja positiointi, lanseeraus, kampanja tai verkkokauppa. Kiinteä laajuus ja hinta."),
    ("Kumppanuus", "Vastaamme markkinoinnin kokonaisuudesta kuukausipalkkiolla – strategiasta toteutukseen. Rajattu määrä asiakkaita kerrallaan."),
]

# Kenelle
FOR = [
    "Verkkokaupat ja D2C-brändit, joilla on toimiva tuote ja halu kasvaa kannattavasti.",
    "Kuluttajatuotebrändit, jotka myyvät myös jälleenmyyjien kautta ja tarvitsevat oman kanavan.",
    "Yritykset, joilla markkinointia tehdään paljon mutta kukaan ei vastaa kokonaisuudesta.",
]
NOT_FOR = "Emme ota mainostiliä tai somea hoitoon ilman oikeutta puhua tavoitteesta, positiosta ja tarjoomasta. Jos haluat vain toteuttajan valmiille suunnitelmalle, on parempia vaihtoehtoja."

FOUNDER = [
    "Sulo Mäki on Äijä Groupin perustaja ja tekee työn itse. Tausta on verkkokauppojen ja D2C-brändien markkinoinnissa: positioinnissa, myyntiviestinnän ja tarjoomien rakentamisessa sekä mitattavassa mainonnassa ja verkkokauppakehityksessä.",
    "Sulon vahvuus on yhdistelmä, joka on harvinainen: hän rakentaa position ja viestin, jotka resonoivat, ja osaa myös tekniikan, jolla ne viedään mainostileille, sivustolle ja mittaukseen. Strategia on hyvä vain, jos se näkyy toteutuksessa ja kassassa.",
]
QUOTE = "Strategia on hyvä vain, jos se näkyy toteutuksessa ja kassassa. Siksi teen molemmat."

PRIVACY = [
    ("Rekisterinpitäjä", "Äijä Group Oy. Yhteydenotot tietosuoja-asioissa: " + SITE["email"] + "."),
    ("Mitä tietoja käsittelemme", "Sivustolla ei ole lomakkeita eikä seurantaevästeitä. Kun otat yhteyttä sähköpostilla, käsittelemme lähettämiäsi tietoja (nimi, sähköposti, viestin sisältö) yhteydenottoon vastaamiseen ja mahdollisen yhteistyön valmisteluun."),
    ("Säilytysaika", "Yhteydenottoja säilytetään enintään 24 kuukautta viimeisestä yhteydenotosta, ellei niistä synny asiakassuhdetta. Asiakassuhteen tietoja säilytetään kirjanpitolain edellyttämän ajan."),
    ("Oikeutesi", "Sinulla on oikeus tarkastaa, oikaista ja pyytää poistamaan tietosi sekä vastustaa käsittelyä. Pyynnöt sähköpostilla rekisterinpitäjälle."),
]
