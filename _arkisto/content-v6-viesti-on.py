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
    "description": "Äijä Group on positiointitoimisto. Selvitämme, mikä kohderyhmääsi oikeasti vaivaa, kirjoitamme viestin, joka osuu siihen, ja viemme sen mainoksiin, sivustolle ja myyntiin. Kun viesti osuu, kanavalla ei ole väliä.",
}

NAV = [("Tunnistatko", "#tunnistatko"), ("Miksi", "#miksi"), ("Mitä saat", "#mita"), ("Näin etenee", "#miten"), ("Perustaja", "#perustaja")]

HERO = {
    "eyebrow": "Positiointitoimisto",
    "h1_a": "Mainonta ei ole rikki.",
    "h1_b": "Viesti on.",
    "lead": "Äijä Group on positiointitoimisto – markkinointi- ja myyntiviestinnän ammattilaisia. Selvitämme, mikä kohderyhmääsi oikeasti vaivaa, kirjoitamme viestin, joka osuu siihen, ja viemme sen mainoksiin, sivustolle ja myyntiin. Sama viesti joka kohtaamisessa.",
}

# 1. Tunnistatko tilanteen? – asiakas tunnistaa itsensä
RECOGNIZE = [
    "Mainontaan ja sivustoon menee joka kuukausi paljon rahaa, mutta kukaan ei osaa sanoa, mikä viesti oikeasti tuo kauppaa.",
    "Toimisto optimoi kampanjoita ja yleisöjä, mutta itse viestiin ei kukaan koske – se on ollut sama kaksi vuotta.",
    "Liikennettä tulee, mutta harva ostaa. Sivusto kertoo, mitä tuote on – ei sitä, miksi sen pitäisi kiinnostaa.",
    "Mainos sanoo yhtä, sivusto toista ja myyjä kolmatta. Asiakas ei tunnista samaa yritystä.",
    "Kilpailu käydään hinnalla ja alennuskoodeilla, koska eroa kilpailijaan ei ole sanoitettu.",
    "Tuote on hyvä ja nykyiset asiakkaat tyytyväisiä – mutta uusia ei saada vakuuttuneiksi.",
]

# 2. Väite – miksi ongelma on viestissä eikä kanavassa
THESIS = {
    "title": "Kun viesti osuu, kanavalla ei ole väliä",
    "paragraphs": [
        "Mainostyökalut lupaavat näyttää mainoksen oikealle ihmiselle oikeaan aikaan. Se on hyvä lupaus, mutta se ei myy mitään. Ihminen ei osta siksi, että mainos tuli sopivalla hetkellä – hän ostaa siksi, että se sanoi jotain, mikä osui.",
        "Osuva viesti syntyy siitä, että tiedetään, mikä kohderyhmää oikeasti vaivaa. Ei pintapuolisesti – vaan eri syvyyksillä: se, mikä ärsyttää arjessa, se, mitä pelätään, ja se, mitä ei sanota ääneen. Kun viesti puhuu näistä ja tarjoaa niihin uskottavan ratkaisun, se toimii Metassa, Googlessa, sähköpostissa ja myyjän suussa.",
        "Kanava tuo ihmiset paikalle. Viesti tekee kaupan. Siksi aloitamme aina viestistä – ja vasta sitten päätämme, missä se näytetään.",
    ],
}

# 3. Mitä saat – konkreettiset tuotokset
DELIVERABLES = [
    ("Positio",
     "Yhdellä sivulla: kenelle brändi on, mihin sitä verrataan ja miksi se valitaan. Päätös, jonka jokainen tiimissä ja jokainen kumppani ymmärtää samalla tavalla."),
    ("Kohderyhmän kipukartta",
     "Mitä asiakas yrittää saada aikaan, mikä siinä on vaikeaa ja mitä hän on jo kokeillut. Kivut ja halut eri syvyyksillä, asiakkaiden omilla sanoilla – haastatteluista, arvosteluista ja myyntikeskusteluista."),
    ("Viesti ja tarjous",
     "Ydinviesti ja sen muunnelmat eri tilanteisiin: sille, joka ei vielä tiedä tarvitsevansa mitään, ja sille, joka vertailee vaihtoehtoja. Tarjous paketoituna niin, että siihen on helppo sanoa kyllä."),
    ("Vienti käytäntöön",
     "Sama viesti mainoksiin, sivustolle, sähköpostiin ja myyntipuheeseen. Toteutamme itse tai briiffaamme nykyiset tekijäsi – ja mittaamme, mikä muunnelma tuo kauppaa."),
]

# 4. Näin työ etenee
PROCESS = [
    ("Kuuntelu",
     "Haastattelemme asiakkaitasi ja myyjiäsi, luemme arvostelut ja tukipyynnöt, käymme läpi myyntidatan ja kilpailijoiden viestit. Emme arvaa, mitä kohderyhmä ajattelee – kysymme.",
     "1–2 viikkoa"),
    ("Positio ja viesti",
     "Kirjoitamme position, kipukartan ja viestin. Ehdotamme yleensä 2–3 vaihtoehtoista suuntaa, joista valitaan yksi – perustellusti, ei maun mukaan.",
     "2–3 viikkoa"),
    ("Testi oikealla rahalla",
     "Viestin muunnelmat testataan mainonnassa pienellä budjetilla ennen kuin mitään lyödään lukkoon. Kohderyhmä äänestää klikkauksilla ja ostoilla.",
     "2–4 viikkoa"),
    ("Vienti käytäntöön",
     "Voittanut viesti viedään kaikkiin kohtaamisiin: mainokset, sivusto, sähköposti, myyntimateriaalit. Sen jälkeen mittaamme ja hiomme kuukausi kerrallaan.",
     "jatkuva"),
]
TOOLS = "Toteutuksessa käytämme sitä, mitä tavoite vaatii: Meta, Google, TikTok, sähköposti, Shopify, laskeutumissivut. Kanava on väline – ei lähtökohta."

# 5. Tavat työskennellä
MODELS = [
    ("Kartoitus", "Käymme läpi nykyisen viestisi, mainonnan ja sivuston ja sanomme suoraan, missä se ei osu ja miksi. Saat kirjallisen arvion ja ehdotuksen. Kiinteä hinta, pari viikkoa.", "Aloita tästä"),
    ("Positiointiprojekti", "Kuuntelu, positio, kipukartta, viesti ja tarjous – testattuna ja valmiina vietäväksi käytäntöön. Voit toteuttaa itse, nykyisen kumppanin kanssa tai meidän kanssamme.", "6–10 viikkoa"),
    ("Kumppanuus", "Vastaamme viestistä ja sen viennistä käytäntöön jatkuvasti: mainonta, sivusto, sähköposti, myynnin tuki. Kuukausipalkkio, rajattu määrä asiakkaita.", "Jatkuva"),
]

NOT_FOR = "Emme ota mainostiliä tai somea hoitoon, jos viestiin ei saa koskea. Silloin optimoimme vain sitä, kuinka tehokkaasti väärä viesti näytetään – ja siihen on halvempia tekijöitä."

FOUNDER = [
    "Sulo Mäki on Äijä Groupin perustaja ja tekee työn itse. Hänen erikoisalansa on selvittää, mikä kohderyhmää oikeasti vaivaa, ja kirjoittaa siihen viesti ja tarjous, joihin on helppo sanoa kyllä.",
    "Sulo osaa myös viedä viestin käytäntöön: mainostilit, sivustot, sähköpostiautomaatiot ja mittaus ovat hänelle tuttuja työkaluja. Siksi viesti ei jää suunnitelmaksi, vaan päätyy sinne, missä asiakas sen näkee.",
]
QUOTE = "Kanava tuo ihmiset paikalle. Viesti tekee kaupan."

PRIVACY = [
    ("Rekisterinpitäjä", "Äijä Group Oy. Yhteydenotot tietosuoja-asioissa: " + SITE["email"] + "."),
    ("Mitä tietoja käsittelemme", "Sivustolla ei ole lomakkeita eikä seurantaevästeitä. Kun otat yhteyttä sähköpostilla, käsittelemme lähettämiäsi tietoja (nimi, sähköposti, viestin sisältö) yhteydenottoon vastaamiseen ja mahdollisen yhteistyön valmisteluun."),
    ("Säilytysaika", "Yhteydenottoja säilytetään enintään 24 kuukautta viimeisestä yhteydenotosta, ellei niistä synny asiakassuhdetta. Asiakassuhteen tietoja säilytetään kirjanpitolain edellyttämän ajan."),
    ("Oikeutesi", "Sinulla on oikeus tarkastaa, oikaista ja pyytää poistamaan tietosi sekä vastustaa käsittelyä. Pyynnöt sähköpostilla rekisterinpitäjälle."),
]
