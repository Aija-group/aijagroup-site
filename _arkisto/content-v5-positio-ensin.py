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
    "description": "Äijä Group on positiointitoimisto. Rakennamme brändille position, tarjooman ja viestin, jotka resonoivat – ja viemme ne käytäntöön mainontaan, sivustolle ja myyntiin. Positio ensin, kaikki muu seuraa.",
}

NAV = [("Miksi", "#miksi"), ("Miten", "#miten"), ("Yhteistyö", "#yhteistyo"), ("Perustaja", "#perustaja")]

HERO = {
    "eyebrow": "Positiointitoimisto",
    "h1_a": "Positio ensin.",
    "h1_b": "Kaikki muu seuraa.",
    "lead": "Äijä Group on positiointiin erikoistunut markkinointitoimisto. Rakennamme brändille position, tarjooman ja viestin, jotka aidosti resonoivat kohderyhmälle – ja viemme ne käytäntöön mainontaan, sivustolle ja myyntiin. Useimmat tekevät sen väärässä järjestyksessä: ostavat kanavan ennen kuin on päätetty, mitä sanotaan ja kenelle.",
}

# 1. Miksi kasvu jumittaa – kolme syytä, jotka peilaavat osaamista
WHY = [
    ("Viesti ei resonoi",
     "Tuote tai palvelu on hyvä, mutta kenellekään ei ole kerrottu, miksi juuri se. Mainonta joutuu tekemään positioinnin työn – ja epäonnistuu siinä, koska se ei ole mainonnan tehtävä.",
     "Positiointi"),
    ("Osat eivät toimi yhteen",
     "Mainonta, sivusto, sähköposti ja some on rakennettu erillään, jokainen omalla logiikallaan ja usein eri tekijöiden käsissä. Kukaan ei vastaa siitä, että ne muodostavat yhden koneen.",
     "Kokonaisuuden suunnittelu"),
    ("Strategia ei ylitä toteutusta",
     "Suunnitelma on hyvä, mutta mainostilillä, verkkokaupassa ja mittauksessa näkyy jotain muuta. Strategian ja tekniikan välissä on aukko, johon tulokset putoavat.",
     "Tekninen jalkautus"),
]

# 2. Miten kasvu rakennetaan – menetelmä neljässä vaiheessa
METHOD = [
    ("Positio",
     "Kenelle brändi on ja miksi se valitaan kilpailijan sijaan.",
     "Positiointi, kohderyhmä, kilpailuasetelma ja se yksi asia, joka brändistä pitää muistaa.",
     ["Asiakas- ja myyntidata", "Kilpailijakartta", "Positiointilause"]),
    ("Tarjooma ja viesti",
     "Mitä tarjotaan, mihin hintaan ja millä sanoilla, jotta se aidosti resonoi kohderyhmälle.",
     "Offerit, hinnoittelun logiikka, myyntiviestit ja luovat kulmat – testattuina oikealla rahalla ennen isoja päätöksiä.",
     ["Offerit ja hinnoittelu", "Myyntiviestit", "Luovat kulmat"]),
    ("Järjestelmä",
     "Miten kanavat, sivusto, sähköposti ja mittaus toimivat yhtenä koneena kasvutavoitetta kohti.",
     "Kanavaroolit ja budjetti, verkkokauppa tai laskeutumissivut, elinkaarimarkkinointi ja mittausmalli, joka kertoo katteen eikä klikkejä.",
     ["Kanavaroolit ja budjetti", "Verkkokauppa ja sivut", "Sähköposti ja pito", "Mittausmalli"]),
    ("Toteutus ja optimointi",
     "Mitä testataan, mitä skaalataan ja mitä lopetetaan – kuukausi kerrallaan.",
     "Kampanjat, automaatiot ja sivuston parannukset rakennetaan itse. Tulokset raportoidaan liiketoiminnan luvuilla: uusasiakashinta, kate, kokonaistuotto.",
     ["Kampanjat ja luovat", "Automaatiot", "Kuukausiraportti"]),
]
TOOLS = "Työkalut, joilla tämä tehdään: Meta, Google Ads, ChatGPT Ads, TikTok, Klaviyo, Shopify, GA4. Ne valitaan tavoitteen mukaan – eivät toisinpäin."

# 3. Miten työskennellään – kytkettynä ketjuun
MODELS = [
    ("Kartoitus", "Diagnoosi siitä, missä vaiheessa ketju katkeaa: positiossa, viestissä, järjestelmässä vai toteutuksessa. Käymme läpi numerot, markkinoinnin ja sivuston ja sanomme suoraan, mitä tekisimme. Kiinteä hinta, lyhyt aika.", "Aloita tästä"),
    ("Projekti", "Yksi tai kaksi vaihetta rajattuna kokonaisuutena: positiointi ja tarjooma, lanseeraus, kampanja tai verkkokauppa. Kiinteä laajuus, aikataulu ja hinta.", "Rajattu tarve"),
    ("Kumppanuus", "Koko ketju jatkuvana. Vastaamme markkinoinnin ja myynnin kokonaisuudesta kuukausipalkkiolla – strategiasta toteutukseen ja optimointiin. Rajattu määrä asiakkaita kerrallaan.", "Koko ketju"),
]

# Kenelle
FOR = [
    "Brändit, joilla on toimiva tuote tai palvelu mutta epäselvä positio: kilpailu käydään hinnalla, koska eroa ei ole sanoitettu.",
    "Yritykset, joiden mainonta toi tuloksia mutta ei enää skaalaudu – viesti on kulunut, ei kanava.",
    "Yritykset, joilla markkinointia tehdään paljon, mutta kukaan ei vastaa siitä, mitä sanotaan ja missä järjestyksessä.",
]
NOT_FOR = "Emme ota mainostiliä tai somea hoitoon ilman oikeutta puhua positiosta, tarjoomasta ja järjestelmästä. Jos haluat vain toteuttajan valmiille suunnitelmalle, on parempia vaihtoehtoja."

FOUNDER = [
    "Sulo Mäki on Äijä Groupin perustaja ja tekee työn itse. Erikoisala on positiointi: kenelle brändi on, miksi se valitaan ja miten se sanotaan niin, että kohderyhmä tunnistaa itsensä. Sen ympärille hän rakentaa tarjooman, myyntiviestit ja markkinoinnin kokonaisuuden.",
    "Harva rakentaa position ja osaa myös viedä sen mainostilille, sivustolle ja sähköpostiautomaatioon. Sulo tekee molemmat – ja siksi ketju ei katkea strategian ja toteutuksen väliin.",
]
QUOTE = "Strategia on hyvä vain, jos se näkyy toteutuksessa ja kassassa. Siksi teen molemmat."

PRIVACY = [
    ("Rekisterinpitäjä", "Äijä Group Oy. Yhteydenotot tietosuoja-asioissa: " + SITE["email"] + "."),
    ("Mitä tietoja käsittelemme", "Sivustolla ei ole lomakkeita eikä seurantaevästeitä. Kun otat yhteyttä sähköpostilla, käsittelemme lähettämiäsi tietoja (nimi, sähköposti, viestin sisältö) yhteydenottoon vastaamiseen ja mahdollisen yhteistyön valmisteluun."),
    ("Säilytysaika", "Yhteydenottoja säilytetään enintään 24 kuukautta viimeisestä yhteydenotosta, ellei niistä synny asiakassuhdetta. Asiakassuhteen tietoja säilytetään kirjanpitolain edellyttämän ajan."),
    ("Oikeutesi", "Sinulla on oikeus tarkastaa, oikaista ja pyytää poistamaan tietosi sekä vastustaa käsittelyä. Pyynnöt sähköpostilla rekisterinpitäjälle."),
]
