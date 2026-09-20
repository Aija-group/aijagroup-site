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
    "description": "Äijä Group auttaa kasvuhaluisia yrityksiä rakentamaan position, myyntiviestin ja offerin, jotka tekevät niiden arvosta helpommin ymmärrettävän. Toteutamme myös verkkosivut, verkkokaupat ja käytännön markkinointia.",
}

NAV = [("Miksi", "#miksi"), ("Mitä teemme", "#mita"), ("Miten työskentelemme", "#miten"), ("Yhteistyö", "#yhteistyo"), ("Meistä", "#meista")]

TITLE = "Äijä Group – Positiointi, myyntiviestit ja verkkosivut"

HERO = {
    "eyebrow": "Positiointi · Myyntiviestit · Verkkosivut",
    "h1": "Älä osta lisää näkyvyyttä viestille, joka ei vielä myy.",
    "p1": [
        "Mainontaan voi käyttää loputtomasti lisää rahaa. Kampanjoita voi optimoida, kohderyhmiä vaihtaa ja uusia creativeja puskea ulos viikko toisensa jälkeen.",
        "Jossain kohtaa kannattaa kuitenkin kysyä yksi yksinkertainen kysymys:",
    ],
    "question": "Onko itse myyntiviesti oikeasti tarpeeksi houkutteleva?",
    "p2_lead": "Äijä Group auttaa kasvuhaluisia yrityksiä selvittämään, ",
    "p2_bold": "miksi asiakkaan pitäisi kiinnostua, miksi hänen pitäisi valita juuri teidät ja miten tämä arvo kannattaa sanoittaa.",
    "p3": [
        "Rakennamme position, myyntiviestin ja offerin sen ympärille, mikä asiakkaalle oikeasti merkitsee.",
        "Sen jälkeen viemme saman ajatuksen mainoksiin, verkkosivuille, verkkokauppaan, sähköposteihin ja myyntiin.",
    ],
    "cta": "Näytä meille nykyinen viestisi",
}

# Miksi
WHY = {
    "title": "Mainonta ei pysty korjaamaan viestiä, joka ei herätä kiinnostusta.",
    "p1": [
        "Monessa yrityksessä mainontaa kehitetään jatkuvasti.",
        "Kohderyhmiä rajataan tarkemmin. Budjettia nostetaan. Creativet vaihtuvat. Kampanjarakennetta ruuvataan. Toimisto raportoi CTR:ää, CPA:ta ja ROASia.",
        "Kaikki nämä ovat tärkeitä asioita.",
        "Silti kaikkein perustavanlaatuisin kysymys jää helposti liian vähälle huomiolle:",
    ],
    "question": "Mitä asiakkaalle oikeastaan sanotaan?",
    "p2": [
        "Jos oikea ihminen näkee mainoksen mutta ei koe siinä mitään itselleen merkityksellistä, ongelmaa on vaikea ratkaista pelkällä mediabudjetilla.",
        "Sama näkyy sivustolla. Liikennettä tulee, mutta kiinnostus ei muutu yhteydenotoiksi tai kaupaksi.",
        "Tai myynnissä. Tuote on hyvä, nykyiset asiakkaat ovat tyytyväisiä ja myyjä osaa selittää arvon puhelussa, mutta markkinointi ei saa samaa asiaa välitettyä ilman ihmistä väliin.",
        "Usein tällaisessa tilanteessa yrityksellä ei ole varsinaista tuoteongelmaa.",
    ],
    "closing": ["Arvo on olemassa.", "Sitä ei vain ole vielä sanoitettu tarpeeksi terävästi."],
}

RECOGNIZE = [
    "Mainontaan menee joka kuukausi rahaa, mutta tulokset tuntuvat junnaavan paikallaan.",
    "Sivustolla käy ihmisiä, mutta liian harva tekee mitään.",
    "Tuote toimii nykyisille asiakkaille erinomaisesti, mutta uusille sen hyötyä on yllättävän vaikea selittää.",
    "Markkinointi keskittyy ominaisuuksiin, vaikka asiakasta kiinnostaa lopulta se, mitä hyötyä niistä on hänen elämässään tai liiketoiminnassaan.",
    "Mainoksissa kokeillaan uusia kuvia ja videoita, mutta viestin perusajatus pysyy samana.",
    "Kilpailijoihin verrattuna erot tuntuvat pieniltä, vaikka tiedätte itse olevanne monessa asiassa parempia.",
    "Myyjä osaa kyllä perustella tuotteen arvon keskustelussa, mutta sama ajatus ei välity sivustolta tai mainonnasta.",
    "Brändillä on paljon sanottavaa, mutta kukaan ei oikein tiedä, mikä niistä asioista pitäisi sanoa ensimmäisenä.",
]
RECOGNIZE_CLOSING = "Jos nämä kuulostavat tutuilta, markkinointia kannattaa katsoa hetki ennen seuraavaa kampanjaa hieman syvemmältä."

POSITIONING = {
    "title": "Positiointi antaa asiakkaalle syyn valita juuri teidät.",
    "intro": [
        "Hyvä positiointi tekee arvosta helpommin hahmotettavan.",
        "Sen avulla asiakas ymmärtää nopeasti, kenelle tuote on tarkoitettu, minkä ongelman se ratkaisee, missä se on vaihtoehtoja parempi ja miksi tällä erolla on merkitystä.",
        "Käytännössä selvitämme esimerkiksi:",
    ],
    "qa": [
        ("Mihin asiakas vertaa teitä?", "Se ei aina ole suora kilpailija. Vaihtoehto voi olla nykyinen toimintatapa, halvempi ratkaisu, oman tiimin tekeminen tai koko asian lykkääminen myöhemmäksi."),
        ("Missä olette aidosti vahvoja?", "Erottautuminen toimii parhaiten silloin, kun se perustuu johonkin todelliseen eikä mainostoimiston keksimään adjektiiviin."),
        ("Mitä hyötyä tästä erosta syntyy asiakkaalle?", "Ominaisuus muuttuu kiinnostavaksi vasta silloin, kun asiakas ymmärtää sen vaikutuksen omaan tilanteeseensa."),
        ("Kenelle tämä hyöty merkitsee eniten?", "Kaikille suunnattu viesti jää helposti niin yleiseksi, ettei kukaan koe sitä erityisen relevantiksi."),
        ("Miten tämä kaikki sanotaan ymmärrettävästi?", "Position pitää lopulta muuttua sanoiksi, jotka toimivat mainoksessa, sivustolla ja myyntikeskustelussa."),
    ],
    "closing": [
        "Kun nämä asiat ovat kirkkaat, markkinoinnin tekeminen helpottuu huomattavasti.",
        "Tiedetään mistä puhua, mitä nostaa esiin ja millä argumenteilla asiakas kannattaa vakuuttaa.",
    ],
}

MESSAGE = {
    "title": "Hyvä myyntiviesti kuulostaa asiakkaasta tutulta.",
    "intro": [
        "Yritykset tuntevat yleensä oman tuotteensa erittäin hyvin.",
        "Asiakkaan ajattelu tunnetaan usein huomattavasti heikommin.",
        "Siksi lähdemme liikkeelle tutkimalla sitä maailmaa, jossa ostopäätös tapahtuu.",
        "Käymme läpi esimerkiksi myyntikeskusteluja, asiakaspalautteita, arvosteluja, mainonnan dataa, hakukäyttäytymistä ja kilpailijoiden viestejä. Tarvittaessa haastattelemme asiakkaita, myyntiä ja muita ihmisiä, jotka keskustelevat kohderyhmän kanssa päivittäin.",
    ],
    "list_title": "Haluamme ymmärtää muun muassa:",
    "questions": [
        "Mitä asiakas yrittää saada aikaan?",
        "Mikä nykyisessä tilanteessa ärsyttää tai hidastaa?",
        "Mikä saa hänet ylipäätään lähtemään etsimään ratkaisua?",
        "Mitä vaihtoehtoja hän harkitsee?",
        "Mitä hän on jo kokeillut?",
        "Mikä aikaisemmissa ratkaisuissa on jäänyt vajaaksi?",
        "Mitä hän epäilee ennen ostamista?",
        "Mitkä asiat lopulta ratkaisevat valinnan?",
        "Millä sanoilla hän itse puhuu ongelmastaan?",
    ],
    "closing": [
        "Hyvä copy tuntuu usein yksinkertaiselta juuri siksi, että sen taustalla on tehty riittävästi ajatustyötä.",
        "Asiakas lukee sen ja ajattelee:",
    ],
    "quote": "Tämähän puhuu juuri siitä ongelmasta, jonka kanssa painin.",
    "after": "Siitä alkaa kiinnostus.",
}

SERVICES = [
    ("Positiointi", [
        "Rakennamme yritykselle selkeän kaupallisen position, jonka ympärille markkinointi ja myynti voidaan rakentaa.",
        "Työssä tarkennetaan kohderyhmä, asiakkaan tärkeimmät vaihtoehdot, yrityksen erottavat vahvuudet ja se arvo, jonka nämä vahvuudet asiakkaalle tuottavat.",
        "Samalla päätämme, mikä näkökulma nostetaan markkinoinnin kärjeksi ja millä perusteilla se voidaan uskottavasti omistaa.",
        "Lopputuloksena yrityksellä on selkeä vastaus kysymykseen:",
    ], "Miksi asiakkaan kannattaa valita juuri meidät?"),
    ("Myyntiviesti & offeri", [
        "Kun positio on kirkas, se muutetaan käytännön myyntiviestiksi.",
        "Rakennamme ydinviestin, arvolupauksen, viestihierarkian, tärkeimmät myyntikulmat ja argumentit, joiden ympärille mainonta ja sivusto voidaan rakentaa.",
        "Samalla käymme läpi offerin. Hyvä tuote voi jäädä vaikeaksi ostaa, jos paketti on epäselvä, lupaus liian laimea tai asiakkaan saama arvo jää abstraktiksi.",
        "Ruuvataan siis kokonaisuus siihen kuntoon, että asiakas ymmärtää nopeasti:",
    ], "Mitä hän saa, miksi se on hänelle arvokasta ja miksi juuri tämä vaihtoehto kannattaa ottaa vakavasti."),
    ("Mainonnan viestit & testaus", [
        "Mainonta antaa meille nopean tavan nähdä, mihin markkina reagoi.",
        "Rakennamme position pohjalta useita viestikulmia ja testaamme esimerkiksi eri ongelmia, lupauksia, hyötyjä, offereita ja tapoja kehystää sama tuote.",
        "Tuloksista nähdään, mikä saa kohderyhmän pysähtymään, klikkaamaan ja etenemään kohti ostoa. Samalla opimme lisää asiakkaasta.",
        "Toimiva viesti voidaan tämän jälkeen viedä laajemmin mainontaan, sivustolle ja muuhun myyntiviestintään.",
    ], None),
    ("Verkkosivut & verkkokaupat", [
        "Verkkosivu on yksi yrityksen tärkeimmistä myyjistä.",
        "Sen pitää auttaa asiakasta ymmärtämään nopeasti, mitä tarjoatte, kenelle se on tarkoitettu, miksi sillä on merkitystä ja miksi teihin kannattaa luottaa.",
        "Rakennamme sivurakenteen, viestihierarkian, copyn ja käyttökokemuksen tämän ostopolun ympärille. Toteutamme yrityssivustoja, landing pageja ja Shopify-verkkokauppoja kokonaisuutena aina strategiasta valmiiseen sivuun.",
        "Mainoksesta alkanut ajatus jatkuu samalla logiikalla sivustolle asti. Asiakkaan ei tarvitse aloittaa ymmärtämistä uudelleen jokaisessa vaiheessa.",
    ], None),
    ("Strateginen markkinointikumppani", [
        "Markkinointi harvoin kehittyy yhden projektin aikana valmiiksi. Asiakkaat muuttuvat, kilpailijat muuttuvat, offerit kehittyvät ja uusia kanavia tulee mukaan.",
        "Toimimme yrityksille myös jatkuvana kaupallisen markkinoinnin kumppanina.",
        "Työ voi sisältää esimerkiksi positioinnin kehittämistä, uusien offerien rakentamista, mainonnan suunnittelua, copywritingia, landing pageja, verkkosivun kehittämistä ja markkinoinnin kokonaisuuden sparrausta.",
        "Strategia ja käytännön tekeminen kulkevat samassa pöydässä.",
    ], None),
]

DELIVERABLES_INTRO = ["Tavoitteena on rakentaa työkaluja, joita yritys pystyy oikeasti käyttämään markkinoinnissa ja myynnissä.", "Tyypillinen kokonaisuus sisältää esimerkiksi:"]
DELIVERABLES = [
    ("Positio", "Selkeä määritelmä siitä, kenelle yritys on erityisen relevantti, mihin vaihtoehtoihin sitä verrataan ja miksi se kannattaa valita."),
    ("Asiakasymmärrys", "Kohderyhmän tärkeimmät ongelmat, tavoitteet, ostotriggerit, epäilykset ja päätökseen vaikuttavat tekijät."),
    ("Viestihierarkia", "Päätös siitä, mikä asia asiakkaalle kerrotaan ensimmäisenä ja millä argumenteilla tarinaa rakennetaan siitä eteenpäin."),
    ("Arvolupaus", "Ytimekäs tapa sanoittaa se arvo, jonka yritys asiakkaalle tuottaa."),
    ("Offeri", "Palvelun tai tuotteen kaupallinen paketointi niin, että asiakkaan on helppo ymmärtää mitä hän saa ja miksi siihen kannattaa tarttua."),
    ("Myyntikulmat", "Eri kohderyhmille, ongelmille ja tietoisuustasoille soveltuvat näkökulmat, joiden avulla samaa tuotetta voidaan markkinoida useasta suunnasta."),
    ("Valmiit copyt", "Tarpeen mukaan mainokset, verkkosivut, landing paget, sähköpostit ja myynnin materiaalit."),
]

PROCESS = [
    ("Selvitetään nykytilanne", [
        "Ensimmäisessä vaiheessa käymme läpi yrityksen nykyisen markkinoinnin, position, offerin, asiakkaat, kilpailijat ja myynnistä saatavan datan.",
        "Tavoitteena on ymmärtää, missä kohtaa kaupallinen viesti tällä hetkellä toimii ja missä kohtaa se menettää tehoa.",
        "Samalla katsotaan kokonaisuutta riittävän avoimesti. Kaikki markkinoinnin ongelmat eivät johdu viestistä, eikä niitä kannata sellaisina käsitellä.",
    ]),
    ("Rakennetaan positio", [
        "Seuraavaksi päätämme, minkä ajatuksen haluamme asiakkaan yhdistävän yritykseen.",
        "Määrittelemme tärkeimmän kohderyhmän, kilpailukentän, erottavat vahvuudet ja niistä syntyvän asiakasarvon. Tässä vaiheessa syntyy markkinoinnin strateginen pohja.",
    ]),
    ("Muutetaan positio sanoiksi", [
        "Position ympärille rakennetaan ydinviesti, arvolupaus, offeri ja tärkeimmät myyntikulmat.",
        "Samalla muodostetaan viestihierarkia, jonka avulla asiakkaalle kerrotaan oikeat asiat oikeassa järjestyksessä. Tämän jälkeen strategia alkaa jo näyttää käytännön markkinoinnilta.",
    ]),
    ("Viedään viesti käytäntöön", [
        "Rakennamme tarvittavat mainokset, landing paget, verkkosivut, verkkokaupan, sähköpostit tai muut materiaalit.",
        "Kanavat valitaan liiketoiminnan, kohderyhmän ja tavoitteen perusteella. Sama kaupallinen ajatus säilyy läpi asiakkaan polun.",
    ]),
    ("Testataan ja kehitetään", [
        "Markkina antaa lopulta parhaimman palautteen.",
        "Seuraamme, mihin viesteihin asiakkaat reagoivat, mitkä kulmat tuovat laadukasta liikennettä ja missä kohtaa ostopolku vielä tökkii. Tulosten pohjalta viestiä, offeria ja toteutusta kehitetään eteenpäin.",
    ]),
]

MODELS_TITLE = "Aloitetaan siitä kohdasta, missä apua eniten tarvitaan."
MODELS = [
    ("Viestiaudit", "Sopii tilanteeseen, jossa markkinointia tehdään jo aktiivisesti mutta tuloksissa tuntuu olevan enemmän potentiaalia. Käymme läpi nykyisen position, offerin, mainokset ja sivuston. Saat näkemyksen siitä, mitkä asiat ovat jo kunnossa, missä viesti menettää tehoa ja mitä lähtisimme kehittämään ensimmäisenä.", "Pyydä viestiaudit", "Viestiaudit"),
    ("Positiointi & myyntiviesti", "Kokonaisuus yritykselle, jonka kaupallinen viesti kaipaa perusteellisempaa remonttia. Tutkimme asiakkaat ja kilpailukentän, rakennamme position ja muutamme sen valmiiksi myyntiviestiksi. Projektin jälkeen yrityksellä on yhteinen kaupallinen punainen lanka, jota voidaan käyttää mainonnassa, verkkosivulla ja myynnissä.", "Keskustellaan projektista", "Positiointiprojekti"),
    ("Verkkosivu / verkkokauppa", "Rakennamme yrityssivustoja, landing pageja ja Shopify-verkkokauppoja strategiasta toteutukseen. Työhön voidaan sisällyttää positiointi, sivuston rakenne, UX, copy, visuaalinen suunnittelu ja tekninen toteutus. Lopputuloksena syntyy sivusto, jonka tehtävä on auttaa asiakasta etenemään kohti ostoa.", "Keskustellaan sivustosta", "Verkkosivuprojekti"),
    ("Jatkuva kumppanuus", "Jatkuva yhteistyö sopii yritykselle, joka haluaa kehittää kaupallista markkinointiaan systemaattisesti. Työpöydällä voivat olla esimerkiksi uudet kampanjat, offerit, mainoskulmat, sivuston kehittäminen, copywriting ja markkinoinnin strategiset kysymykset. Toimimme käytännössä yrityksen markkinoinnin strategisena lisäresurssina.", "Kysy kumppanuudesta", "Kumppanuus"),
]

MEDIA = {
    "title": "Jokainen mediaeuro suurentaa viestin vaikutusta.",
    "p1": ["Hyvä viesti hyötyy näkyvyydestä.", "Heikko viesti saa näkyvyyden mukana vain enemmän ihmisiä ohittamaan sen.", "Siksi mainonnan skaalaaminen kannattaa tehdä siinä vaiheessa, kun perusasiat ovat kunnossa:"],
    "list": ["Tuote ratkaisee oikean ongelman.", "Offeri on kilpailukykyinen.", "Kohderyhmä on riittävän tarkasti ymmärretty.", "Asiakas saa muutamassa sekunnissa kiinni siitä, miksi hänen pitäisi kiinnostua."],
    "p2": ["Kun nämä asiat osuvat kohdalleen, mainonnan tehtävä muuttuu paljon yksinkertaisemmaksi.", "Sen tarvitsee enää viedä hyvä viesti mahdollisimman monen oikean ihmisen eteen."],
}

FOUNDER = [
    "Olen tehnyt markkinointia ja myyntiä vuosia sekä omille yrityksilleni että asiakkailleni.",
    "Myynnissä mua on aina kiinnostanut erityisesti yksi kysymys: **mikä saa ihmisen oikeasti ostamaan?**",
    "Miksi joku tuote tuntuu heti kiinnostavalta, kun taas toinen jää täysin yhdentekeväksi, vaikka itse tuotteessa ei välttämättä olisi mitään vikaa?",
    "Aika nopeasti tajusin, että käytännössä lähes kaikki markkinoinnissa ja myynnissä palautuu lopulta samaan asiaan:",
    "**Miten tuotteen arvo saadaan välitettyä toiselle ihmiselle niin hyvin, että hän haluaa toimia?**",
    "Siitä mun kiinnostus positiointiin ja myyntiviestintään oikeastaan lähti.",
    "Haluan ensin ymmärtää, mikä tuotteessa on asiakkaalle oikeasti arvokasta, miksi hän ostaisi sen ja miksi juuri tämän vaihtoehdon jonkun muun sijaan. Sen jälkeen sama ajatus pitää saada näkymään kaikkialla, missä asiakas kohtaa yrityksen.",
    "Mainoksen pitää saada pysähtymään. Verkkosivun pitää saada muutamassa sekunnissa ymmärtämään, mistä tässä on kyse ja miksi tämän pitäisi kiinnostaa. Myyntikeskustelun pitää antaa tarpeeksi hyvä syy jatkaa keskustelua.",
    "Ja parhaassa tapauksessa positiointi on niin selkeä, että asiakas osaa itsekin kertoa toiselle ihmiselle, miksi valitsi juuri tämän tuotteen tai yrityksen.",
    "Siinä kohtaa positiointi alkaa oikeasti tehdä töitä.",
]

CONTACT = {
    "title": "Näytä meille, mitä asiakkaillesi tällä hetkellä sanot.",
    "text": ["Lähetä linkki sivustoosi ja halutessasi pari nykyistä mainosta.", "Käyn ne läpi ja kerron, mitkä asiat herättävät ensimmäisenä huomion ja missä näkisin suurimman kehityspotentiaalin.", "Pari linkkiä riittää alkuun."],
}
FOOTER_LINE = "Positiointi · Myyntiviestit · Verkkosivut · Verkkokaupat · Strateginen markkinointi"

PRIVACY = [
    ("Rekisterinpitäjä", "Äijä Group Oy. Yhteydenotot tietosuoja-asioissa: " + SITE["email"] + "."),
    ("Mitä tietoja käsittelemme", "Yhteydenottolomakkeella kerätään nimi, sähköposti, yritys, verkkosivun osoite ja viestin sisältö. Lomakkeen tekninen käsittelijä on Netlify (Netlify Forms), josta viesti välitetään sähköpostiimme. Sivusto ei käytä seurantaevästeitä. Tietoja käytetään yhteydenottoon vastaamiseen ja mahdollisen yhteistyön valmisteluun."),
    ("Säilytysaika", "Yhteydenottoja säilytetään enintään 24 kuukautta viimeisestä yhteydenotosta, ellei niistä synny asiakassuhdetta. Asiakassuhteen tietoja säilytetään kirjanpitolain edellyttämän ajan."),
    ("Oikeutesi", "Sinulla on oikeus tarkastaa, oikaista ja pyytää poistamaan tietosi sekä vastustaa käsittelyä. Pyynnöt sähköpostilla rekisterinpitäjälle."),
]
