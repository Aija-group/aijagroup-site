# -*- coding: utf-8 -*-
"""Äijä Group Oy – sivuston sisältö. Muokkaa tätä, aja build.py."""

SITE = {
    "name": "Äijä Group Oy",
    "short": "Äijä Group",
    "domain": "https://aijagroup.fi",          # OLETUS – vahvista domain
    "email": "sulo@aijagroup.fi",              # OLETUS – vahvista
    "phone": "",                               # ei julkaista ennen vahvistusta
    "founder": "Sulo Mäki",
    "founder_title": "Perustaja ja omistaja",
    "city": "Suomi",
    "ytunnus": "",                             # täydennä
    "tagline": "Markkinointistrategioihin erikoistunut toimisto kuluttajabrändeille",
    "description": "Äijä Group on markkinointistrategioihin erikoistunut toimisto kuluttajabrändeille. Strategia ja positiointi, liidienhankinta, brändimainonta, orgaaninen some ja verkkokauppaprojektit – yhdellä logiikalla, yhdestä paikasta.",
    "linkedin": "https://www.linkedin.com/company/aijagroup",  # OLETUS
}

NAV = [
    ("Mitä teemme", "/palvelut/"),
    ("Toimintamalli", "/toimintamalli/"),
    ("Kenelle", "/kenelle/"),
    ("Yritys", "/yritys/"),
    ("Yhteys", "/yhteys/"),
]

# Etusivun hero
HERO = {
    "eyebrow": "Markkinointistrategioihin erikoistunut toimisto",
    "h1_a": "Strategia ensin.",
    "h1_b": "Sitten toteutus, joka näkyy tuloksissa.",
    "lead": "Äijä Group on markkinointistrategioihin erikoistunut toimisto kuluttajabrändeille. Oli kyse liidienhankinnasta, brändimainonnasta, orgaanisesta somesta tai yksittäisestä verkkokauppaprojektista – aloitamme aina siitä, mitä yritetään saada aikaan ja kenelle. Sen jälkeen vastaamme myös toteutuksesta.",
    "cta": "Varaa kartoituskeskustelu",
    "cta2": "Mitä teemme",
}

# Kolme väitettä heron alla
CLAIMS = [
    ("Strategia, joka viedään käytäntöön", "Emme jätä suunnitelmaa kalvoiksi. Sama tiimi, joka päättää position ja suunnan, rakentaa kampanjat, sisällöt ja sivut – ja vastaa siitä, että ne tuottavat."),
    ("Kanava valitaan tavoitteen mukaan", "Meta, Google, ChatGPT, orgaaninen some tai sähköposti ovat työkaluja. Valitsemme ne sen perusteella, mitä pitää saada aikaan – emme sen mukaan, mitä osaamme myydä."),
    ("Perustaja tekee työn", "Et saa myyjää, joka luovuttaa asiakkuuden juniorille. Sulo Mäki vastaa strategiasta ja on mukana toteutuksessa alusta loppuun."),
]

# Kanavat ja työkalut, jotka mainitaan tukiroolissa (ei omina palveluina)
TOOLS = ["Meta Ads", "Google Ads", "ChatGPT Ads", "YouTube", "TikTok", "Instagram", "Sähköposti & Klaviyo", "Shopify", "GA4", "Laskeutumissivut"]

SERVICES = [
    {
        "slug": "strategia",
        "nav": "Strategia ja positiointi",
        "title": "Markkinointistrategia ja positiointi",
        "icon": "target",
        "wide": True,
        "short": "Kenelle brändi on, mitä se lupaa, mistä kasvu tulee ja mihin rahat laitetaan. Kaikki muu tekemisemme johdetaan tästä.",
        "lead": "Useimpien kuluttajabrändien ongelma ei ole huono mainonta vaan päättämättömyys: kenelle brändi on, miksi se valitaan ja mihin rajallinen budjetti kannattaa laittaa. Markkinointistrategia vastaa näihin kysymyksiin niin konkreettisesti, että toteutus voi alkaa heti.",
        "meta": "Markkinointistrategia ja positiointi kuluttajabrändeille: kohderyhmä, erottuva lupaus, kasvun lähteet, kanavaroolit, budjetti ja mittarit. Strategia, joka on kirjoitettu toteutettavaksi.",
        "intro": [
            "Strategiatyö alkaa numeroista ja asiakkaista, ei workshop-post-iteista. Käymme läpi myyntidatan, asiakaspalautteen, arvostelut ja kilpailijoiden viestit. Selvitämme, kuka oikeasti ostaa, miksi ja mitä vaihtoehtoja hän harkitsi.",
            "Lopputulos on tiivis dokumentti, jonka jokainen tiimin jäsen ja kumppani ymmärtää: kohderyhmä, positio ja lupaus, kasvun lähteet (uudet asiakkaat, ostotiheys, keskiostos), kanavaroolit, budjetin jako, mittarit ja seuraavan puolen vuoden tekemiset.",
            "Strategia ei ole kertaluonteinen dokumentti vaan päätös, jota testataan markkinassa. Siksi kirjoitamme sen niin, että se voidaan viedä suoraan mainontaan, sisältöihin ja sivuille – ja päivitämme sitä, kun tulokset opettavat jotain uutta.",
        ],
        "features": [
            ("Asiakas- ja dataperusteinen analyysi", "Myyntidata, arvostelut, asiakaspalaute ja haastattelut – ei oletuksia."),
            ("Positiointi ja viestihierarkia", "Yksi lupaus, perustelut ja äänensävy. Valmis käytettäväksi mainonnassa, somessa ja sivuilla."),
            ("Kasvun lähteet ja yksikkötalous", "Mistä kasvu tulee, mitä uusi asiakas saa maksaa ja paljonko kasvuun voi investoida."),
            ("Kanavaroolit, budjetti ja mittarit", "Mitä kukin kanava tekee, miten rahat jaetaan ja millä luvuilla onnistumista arvioidaan."),
        ],
        "faq": [
            ("Kuinka kauan strategiatyö kestää?", "Tyypillisesti 4–6 viikkoa aloituksesta valmiiseen strategiaan. Nopeus riippuu siitä, kuinka paljon dataa ja asiakaskontakteja on käytettävissä."),
            ("Voiko strategian ostaa ilman toteutusta?", "Kyllä. Osa asiakkaista teettää strategian meillä ja toteuttaa itse tai nykyisen kumppanin kanssa. Kirjoitamme sen niin, että toinen tekijä pystyy toteuttamaan sen."),
            ("Tarvitsemmeko uuden ilmeen tai logon?", "Ei välttämättä. Strategia on päätös siitä, mitä sanotaan, kenelle ja missä – visuaalinen ilme päivitetään vain, jos se on ristiriidassa uuden position kanssa."),
        ],
    },
    {
        "slug": "liidienhankinta",
        "nav": "Liidienhankinta ja myynti",
        "title": "Liidienhankinta ja myynnin kasvattaminen",
        "icon": "chart",
        "short": "Mitattavaa kysyntää: yhteydenottoja, tarjouspyyntöjä ja verkkokauppatilauksia. Kanavat valitaan tavoitteen mukaan, tulokset raportoidaan liiketoiminnan luvuilla.",
        "lead": "Kun tavoite on saada lisää liidejä tai tilauksia, kysymys ei ole siitä, mikä kanava on muodikas, vaan siitä, missä kohderyhmäsi on ostohetkellä ja mikä viesti saa hänet toimimaan. Rakennamme kokonaisuuden – viestin, kanavat, laskeutumissivut ja mittauksen – ja optimoimme sitä kuukausittain.",
        "meta": "Liidienhankinta ja myynnin kasvattaminen kuluttajabrändeille: viesti, kanavavalinta (Meta, Google, ChatGPT Ads), laskeutumissivut, mittaus ja kuukausittainen optimointi. Tulokset liiketoiminnan luvuilla.",
        "intro": [
            "Aloitamme yksikkötaloudesta: mitä liidi tai tilaus saa maksaa, jotta se on kannattava. Siitä johdetaan budjetti, kanavat ja tavoiteluvut. Näin tiedät ennen ensimmäistäkään kampanjaa, mitä hyvä tulos tarkoittaa.",
            "Kanavat valitaan roolinsa mukaan. Meta ja TikTok rakentavat kysyntää ja skaalaavat, Google ja ChatGPT Ads keräävät jo olemassa olevan ostoaikomuksen, sähköposti hoitaa jatkon. Viesti johdetaan positiosta ja testataan järjestelmällisesti – luova on tärkein kohdennus.",
            "Mittaus rakennetaan todellisten liidien ja tilausten varaan, ei klikkausten. Raportoimme kuukausittain sillä kielellä, jolla yrityksen johto puhuu: paljonko uusia asiakkaita, mihin hintaan, mikä on kokonaismainonnan tuotto ja mitä opittiin.",
        ],
        "features": [
            ("Viesti ja tarjous", "Positiosta johdetut viestikulmat ja tarjoukset, joita testataan oikealla rahalla."),
            ("Kanavat ja toteutus", "Meta, Google, ChatGPT Ads, TikTok ja sähköposti – tilirakenne, luovat ja jatkuva testaus."),
            ("Laskeutumissivut", "Sivu, joka jatkaa mainoksen viestiä ja kääntää liikenteen liideiksi tai tilauksiksi."),
            ("Mittaus ja kuukausiraportti", "Liidin/tilauksen hinta, kate ja kokonaistuotto. Seuraavan kuun testit yhdellä sivulla."),
        ],
        "faq": [
            ("Mitä kanavia käytätte?", "Useimmiten Meta-mainontaa, Google Adsia, sähköpostia ja yhä useammin ChatGPT Adsia. Kanava valitaan tavoitteen, kohderyhmän ja budjetin mukaan – ei toisinpäin."),
            ("Kuinka nopeasti tulokset näkyvät?", "Ensimmäiset testitulokset 2–4 viikossa. Kannattava skaalaus vaatii tyypillisesti 2–3 kuukauden testaussyklin, riippuen budjetista ja lähtötilanteesta."),
            ("Kenen nimissä mainostilit ovat?", "Aina asiakkaan. Työskentelemme kumppanina asiakkaan tileillä, ja data ja historia jäävät asiakkaalle."),
        ],
    },
    {
        "slug": "brandimainonta",
        "nav": "Brändimainonta",
        "title": "Brändimainonta",
        "icon": "megaphone",
        "short": "Tunnettuutta, joka laskee kaikkien muiden kanavien hintaa. Yksi muistettava viesti, oikeat kanavat ja vaikutus, joka mitataan muualta kuin kampanjan omasta raportista.",
        "lead": "Pelkällä suoralla vastemainonnalla kasvu pysähtyy, kun ostovalmiit yleisöt on käyty läpi. Brändimainonta rakentaa kysyntää etukäteen – ja kun se tehdään strategiasta käsin, se ei ole kulu vaan investointi, jonka tuotto näkyy halvempina hakuina, parempana konversiona ja hintajoustona.",
        "meta": "Brändimainonta kuluttajabrändeille: kampanjakonsepti positiosta, video, some ja yhteistyöt, kanavasuunnittelu sekä vaikutuksen mittaus brändihaun, suoran liikenteen ja konversion kautta.",
        "intro": [
            "Brändimainonnan tehtävä on saada oikea kohderyhmä tunnistamaan brändi ja muistamaan yhden asian siitä. Se yksi asia tulee positioinnista – siksi emme tee brändikampanjaa ilman strategiaa.",
            "Suunnittelemme kampanjan formaatit ja kanavat kohderyhmän mediankäytön mukaan: video Metassa, YouTubessa ja TikTokissa, yhteistyöt sisällöntuottajien kanssa, tarvittaessa ulko- tai radiomainonta kumppaneiden kautta.",
            "Mittaamme vaikutusta muualla kuin kampanjan omassa raportissa: brändihaun kasvu, suora liikenne, muun mainonnan konversioasteen muutos ja tarvittaessa brand lift -tutkimus.",
        ],
        "features": [
            ("Kampanjakonsepti strategiasta", "Yksi muistettava viesti, joka kestää useita toteutuksia ja kanavia."),
            ("Video ja sisältöyhteistyöt", "Käsikirjoitus, tuotannon ohjaus ja sisällöntuottajayhteistyöt."),
            ("Kanavasuunnittelu", "Meta, YouTube, TikTok, sisällöntuottajat ja tarvittaessa perinteinen media kumppaniverkoston kautta."),
            ("Vaikutuksen mittaus", "Brändihaku, suora liikenne, konversioasteen muutos ja brand lift."),
        ],
        "faq": [
            ("Milloin brändimainonta on ajankohtaista?", "Kun suora vastemainonta on kannattavaa mutta ei enää skaalaudu, tai kun kategoria on kilpailtu ja hinta on ainoa ero. Ei silloin, kun tuote tai positio on vielä testaamatta."),
            ("Kuinka paljon budjetista pitäisi mennä brändiin?", "Ei ole yhtä oikeaa lukua. Tyypillinen lähtökohta on 20–40 % mediabudjetista, ja jakoa säädetään sen mukaan, miten brändihaku ja suora liikenne kehittyvät."),
        ],
    },
    {
        "slug": "orgaaninen-some",
        "nav": "Orgaaninen some",
        "title": "Orgaaninen some ja sisältöstrategia",
        "icon": "chat",
        "short": "Sisältöä, jolla on tehtävä: mitä julkaistaan, kenelle, missä kanavissa ja miten se tukee myyntiä. Strategia, konseptit ja tuotannon ohjaus.",
        "lead": "Orgaaninen some ei ole ilmaista, se maksaa aikaa. Siksi sillä pitää olla strategia: mitä brändin halutaan olevan tunnettu, mille yleisölle sisältöä tehdään ja miten some kytkeytyy mainontaan ja myyntiin. Ilman sitä julkaistaan ahkerasti eikä mitään tapahdu.",
        "meta": "Orgaaninen some ja sisältöstrategia kuluttajabrändeille: kanavavalinta, sisältöpilarit ja konseptit, julkaisurytmi, tuotannon ohjaus ja mittaus. Some, joka tukee myyntiä ja mainontaa.",
        "intro": [
            "Sisältöstrategia johdetaan positiosta: mistä aiheista brändi puhuu, millä äänellä ja mitä se ei tee. Valitsemme kanavat kohderyhmän mukaan – yleensä on parempi tehdä yksi tai kaksi kanavaa hyvin kuin viisi puolihuolimattomasti.",
            "Rakennamme sisältöpilarit ja toistettavat konseptit, joita voi tuottaa viikosta toiseen ilman, että joka julkaisu keksitään tyhjästä. Ohjaamme tuotantoa tai tuotamme sisällöt yhdessä brändin omien tekijöiden ja sisällöntuottajien kanssa.",
            "Some ja mainonta suunnitellaan yhdessä: parhaat orgaaniset sisällöt skaalataan mainonnalla, ja mainonnan testitulokset kertovat, mikä viesti kannattaa viedä orgaaniseen sisältöön. Mittaamme kasvun ja sitoutumisen lisäksi sitä, mitä some tuo sivustolle ja myyntiin.",
        ],
        "features": [
            ("Sisältöstrategia ja kanavavalinta", "Aiheet, äänensävy, kanavat ja julkaisurytmi johdettuna positiosta."),
            ("Konseptit ja sisältöpilarit", "Toistettavat formaatit, jotka helpottavat tuotantoa ja rakentavat tunnistettavuutta."),
            ("Tuotannon ohjaus", "Sisältökalenteri, briiffit ja yhteistyö brändin tekijöiden ja sisällöntuottajien kanssa."),
            ("Kytkentä mainontaan ja mittaus", "Parhaat sisällöt skaalataan mainonnalla; vaikutus mitataan liikenteessä ja myynnissä."),
        ],
        "faq": [
            ("Hoidatteko julkaisemisen ja yhteisönhallinnan?", "Vastaamme strategiasta, konsepteista ja tuotannon ohjauksesta. Päivittäinen julkaiseminen ja kommentteihin vastaaminen sopii useimmiten parhaiten brändin omalle tiimille – autamme rakentamaan siihen prosessin."),
            ("Mitkä kanavat kannattaa valita?", "Se riippuu kohderyhmästä ja tuotteesta. Useimmille kuluttajabrändeille Instagram ja TikTok ovat tärkeimmät, mutta päätös tehdään strategiatyössä, ei oletuksena."),
        ],
    },
    {
        "slug": "verkkokauppa",
        "nav": "Verkkokauppa ja sivustot",
        "title": "Verkkokauppa- ja verkkosivuprojektit",
        "icon": "browser",
        "short": "Rajattu projekti, kun tarvitaan uusi verkkokauppa, sivusto tai laskeutumissivu – suunniteltuna myymään, ei vain näyttämään hyvältä.",
        "lead": "Joskus tarve on selkeä ja rajattu: uusi verkkokauppa, yrityssivusto tai kampanjan laskeutumissivu. Teemme sen projektina – mutta samalla ajattelulla kuin muun työmme: sivun pitää jatkaa brändin viestiä ja kääntää kävijät asiakkaiksi.",
        "meta": "Verkkokauppa- ja verkkosivuprojektit kuluttajabrändeille: Shopify-verkkokaupat, yrityssivustot ja laskeutumissivut. Konversio-optimoitu rakenne, nopea toteutus, hakukoneystävällisyys ja mittaus.",
        "intro": [
            "Aloitamme siitä, mitä sivun pitää saada aikaan: mistä liikenne tulee, mitä kävijä tietää ja epäilee ja mikä saa hänet jatkamaan. Rakenne, tekstit ja kuvat suunnitellaan tässä järjestyksessä – ulkoasu palvelee viestiä.",
            "Toteutamme sivut nopeina ja kevyinä: Shopify-verkkokaupat ja -mukautukset, laskeutumissivut kampanjoihin sekä yrityssivustot, jotka latautuvat nopeasti myös mobiilissa. Tekninen hakukoneoptimointi, rakenteinen data ja mittaus (GA4, Meta, Google) kuuluvat toteutukseen.",
            "Projekti päättyy julkaisuun, mutta sivusto ei ole silloin valmis. Annamme selkeän suunnitelman siitä, mitä seurata ja parantaa – ja jatkamme kumppanina, jos niin sovitaan.",
        ],
        "features": [
            ("Konversiorakenne ja tekstit", "Sivun logiikka ja copy johdetaan positiosta ja kävijän ostopolusta."),
            ("Toteutus", "Shopify-verkkokaupat, laskeutumissivut ja yrityssivustot. Nopeat, kevyet ja mobiili ensin."),
            ("Tekninen SEO ja mittaus", "Rakenteinen data, sivunopeus, GA4, Meta CAPI ja Google-konversiot kunnossa julkaisusta lähtien."),
            ("Selkeä projekti", "Kiinteä laajuus, aikataulu ja hinta. Tiedät, mitä saat ja milloin."),
        ],
        "faq": [
            ("Millä alustalla sivut tehdään?", "Verkkokaupoissa useimmiten Shopify. Laskeutumissivut ja yrityssivustot toteutetaan kevyinä staattisina sivuina tai asiakkaan nykyiselle alustalle, jos se on järkevä."),
            ("Voiko projektin ostaa ilman muuta yhteistyötä?", "Kyllä. Verkkokauppa- ja sivustoprojektit tehdään myös yksittäisinä, kiinteähintaisina projekteina. Moni jatkaa sen jälkeen kumppanuuteen, mutta se ei ole ehto."),
        ],
    },
]

# Toimintamalli – strategisen kumppanuuden vaiheet
PROCESS = [
    ("Diagnoosi", "Käymme läpi numerot, asiakkaat, kilpailijat ja nykyisen markkinoinnin. Selvitämme, missä kasvu oikeasti jumittaa: positiossa, tarjoomassa, kanavissa vai sivustossa.", "1–2 vk"),
    ("Strategia ja positiointi", "Päätämme kenelle brändi on, mitä se lupaa, mistä kasvu tulee ja mihin rahat laitetaan. Kirjoitamme suunnitelman, josta toteutus johdetaan.", "4–6 vk"),
    ("Toteutussuunnitelma", "Kanavaroolit, budjetin jako, sisältökonseptit, tavoiteluvut ja testaussuunnitelma. Suunnitelma, jota vastaan tuloksia arvioidaan.", "1–2 vk"),
    ("Toteutus", "Rakennamme sivut, sisällöt ja kampanjat ja käynnistämme mainonnan valituissa kanavissa. Ensimmäiset testit 2–4 viikossa.", "jatkuva"),
    ("Mittaus ja optimointi", "Kuukausittainen raportti liiketoiminnan luvuilla, seuraavan kuun testit ja päätökset. Strategiaa päivitetään, kun markkina opettaa jotain uutta.", "kuukausittain"),
]

# Kumppanuusmallit (ei hintoja ennen vahvistusta)
MODELS = [
    ("Kartoitus", "Yksi kiinteähintainen jakso, jossa käymme läpi numerot, markkinoinnin ja sivuston ja annamme selkeän arvion: mistä kasvu jumittaa ja mitä kannattaa tehdä seuraavaksi. Sopii ensimmäiseksi askeleeksi.", "Kertaprojekti"),
    ("Projekti", "Rajattu kokonaisuus kiinteällä hinnalla: markkinointistrategia, lanseeraus, brändikampanja tai verkkokauppaprojekti. Voit toteuttaa jatkon itse, nykyisen kumppanin kanssa tai meidän kanssamme.", "4–10 viikkoa"),
    ("Strateginen kumppanuus", "Jatkuva malli: vastaamme strategiasta, mainonnasta, sisällöistä ja sivuston kehityksestä kuukausittaisella palkkiolla. Toimimme brändin ulkoistettuna markkinointijohtona ja tekevänä tiiminä.", "Kuukausisopimus"),
]

# Kenelle – kohderyhmät
AUDIENCES = [
    ("D2C-verkkokaupat", "Myyt omaa tuotetta suoraan kuluttajille verkossa. Markkinointi on tärkein kasvumoottori, ja jokainen euro pitää perustella katteella.", "cart"),
    ("Kuluttajatuotebrändit", "Tuotteesi myydään myös jälleenmyyjien kautta. Tarvitset brändin, joka vetää hyllystä ja verkkokaupasta, ja oman kanavan, joka ei syö jälleenmyyjien myyntiä.", "box"),
    ("Kuluttajapalvelut", "Myyt palvelua kuluttajille ja kasvu tulee liideistä: yhteydenotoista, tarjouspyynnöistä ja varauksista. Tarvitset viestin, joka erottaa, ja kanavat, jotka tuottavat mitattavasti.", "users"),
]

# Tilanteet, joissa meihin otetaan yhteyttä
SITUATIONS = [
    "Markkinointia tehdään paljon, mutta kukaan ei osaa sanoa, mikä siitä tuottaa.",
    "Mainonta toi tuloksia, mutta ei enää skaalaudu – liidin tai tilauksen hinta nousee joka kuukausi.",
    "Brändi ei erotu kategoriassa; kilpailu käydään hinnalla ja alennuskoodeilla.",
    "Somea julkaistaan ahkerasti, mutta se ei näy sivustolla eikä myynnissä.",
    "Kanavat ovat eri toimijoilla, eikä kukaan vastaa kokonaisuudesta.",
    "Edessä on uusi tuote, markkina tai verkkokauppa – tarvitaan suunnitelma ennen kuin rahaa käytetään.",
]

# Periaatteet
PRINCIPLES = [
    ("Numerot ennen mielipiteitä", "Jokainen suositus perustellaan datalla: myynnillä, katteella, testituloksilla. Jos dataa ei ole, hankimme sen testaamalla."),
    ("Yksi logiikka kaikessa", "Strategia, mainonta, sisällöt ja sivusto noudattavat samaa viestiä. Asiakas kohtaa saman brändin mainoksessa, somessa, hakutuloksessa ja kassalla."),
    ("Selkeä puhe", "Ei toimistojargonia eikä raportteja, joita pitää tulkita. Sanomme, mikä toimii, mikä ei ja mitä teemme seuraavaksi."),
    ("Asiakkaan omistus", "Mainostilit, data, sisällöt ja sivusto ovat aina asiakkaan nimissä. Kumppanuus perustuu tuloksiin, ei lukkoihin."),
]

ABOUT = {
    "title": "Äijä Group Oy",
    "lead": "Äijä Group on Sulo Mäen perustama, markkinointistrategioihin erikoistunut toimisto kuluttajabrändeille. Autamme, kun tavoite on liidejä, tunnettuutta, toimivaa somea tai uusi verkkokauppa – ja aloitamme aina strategiasta.",
    "paragraphs": [
        "Toimisto syntyi yhdestä havainnosta: kuluttajabrändien markkinointi on pilkottu liian pieniin paloihin. Yksi toimisto tekee strategian, toinen mainontaa, kolmas somea, neljäs sivuston – eikä kukaan vastaa siitä, että kokonaisuus tuottaa. Äijä Group on rakennettu tämän aukon täyttämiseksi.",
        "Työskentelemme rajatun määrän brändien kanssa kerrallaan. Se on tietoinen valinta: strateginen kumppanuus tarkoittaa, että perustaja tuntee liiketoimintasi luvut, tuotteet ja asiakkaat – ei vain mainostilin.",
        "Nimi on rehellinen. Äijä tekee, mitä lupaa, puhuu suoraan ja pitää sanansa. Samaa odotamme brändeiltä, joiden kanssa työskentelemme.",
    ],
    "founder_paragraphs": [
        "Sulo Mäki on Äijä Groupin perustaja ja omistaja. Hän vastaa jokaisen asiakkuuden strategiasta ja on mukana toteutuksessa – kampanjoiden rakenteesta laskeutumissivujen teksteihin.",
        "Sulon tausta on kuluttajabrändien markkinoinnissa ja verkkokaupassa: positioinnissa, mitattavassa mainonnassa ja verkkosivukehityksessä. Työtapa on käytännönläheinen – strategia on hyvä vain, jos se näkyy toteutuksessa ja kassassa.",
    ],
}

FAQ_GENERAL = [
    ("Mitä Äijä Group tekee?", "Olemme markkinointistrategioihin erikoistunut toimisto kuluttajabrändeille. Teemme strategian ja positioinnin ja vastaamme myös toteutuksesta: liidienhankinnasta ja mainonnasta, brändikampanjoista, orgaanisesta somesta sekä verkkokauppa- ja sivustoprojekteista."),
    ("Miten yhteistyö alkaa?", "Kartoituskeskustelulla. Käymme läpi tilanteesi, tavoitteesi ja nykyisen markkinoinnin noin tunnissa. Sen jälkeen ehdotamme, kannattaako aloittaa kartoituksella, rajatulla projektilla vai suoraan kumppanuudella – tai ei mitään, jos emme ole oikea kumppani."),
    ("Kenelle palvelu sopii?", "Kuluttajabrändeille, joilla on toimiva tuote tai palvelu ja halu kasvaa kannattavasti: D2C-verkkokaupoille, jälleenmyyjien kautta myyville tuotebrändeille ja kuluttajapalveluille, joiden kasvu tulee liideistä."),
    ("Pitääkö aina aloittaa strategiasta?", "Rajatun projektin, kuten verkkokaupan tai yksittäisen kampanjan, voi tehdä ilman laajaa strategiatyötä. Silloinkin käymme tavoitteen, kohderyhmän ja viestin läpi ennen toteutusta – se on lyhyt vaihe, mutta se ratkaisee lopputuloksen."),
    ("Mitä yhteistyö maksaa?", "Kartoitus ja projektit ovat kiinteähintaisia, jatkuva kumppanuus kuukausipalkkiolla. Hinta riippuu laajuudesta ja mediabudjetista – kerromme sen kartoituskeskustelun jälkeen ilman arvailua."),
    ("Kenen nimissä mainostilit ja sivusto ovat?", "Aina asiakkaan. Työskentelemme kumppanina asiakkaan tileillä, ja kaikki data, historia ja sivusto jäävät asiakkaalle yhteistyön päättyessäkin."),
    ("Teettekö töitä myös B2B-yrityksille?", "Ydinosaamisemme on kuluttajabrändeissä. Autamme B2B-yrityksiä tapauskohtaisesti, jos ostopäätös muistuttaa kuluttajakauppaa – muuten ohjaamme mielellämme sopivamman kumppanin puoleen."),
]

PRIVACY = [
    ("Rekisterinpitäjä", "Äijä Group Oy. Yhteydenotot tietosuoja-asioissa: " + SITE["email"] + "."),
    ("Mitä tietoja keräämme", "Yhteydenottolomakkeella kerätään nimi, sähköposti, yritys, verkkosivun osoite, mahdollinen puhelinnumero sekä viestin sisältö. Sivusto ei käytä seurantaevästeitä ilman suostumusta."),
    ("Mihin tietoja käytetään", "Tietoja käytetään yhteydenottoon vastaamiseen, kartoituskeskustelun sopimiseen ja tarjouksen laatimiseen. Tietoja ei käytetä markkinointiin ilman erillistä lupaa eikä luovuteta kolmansille osapuolille."),
    ("Säilytysaika", "Yhteydenottotietoja säilytetään enintään 24 kuukautta viimeisestä yhteydenotosta, ellei niistä synny asiakassuhdetta. Asiakassuhteen tietoja säilytetään kirjanpitolain edellyttämän ajan."),
    ("Oikeutesi", "Sinulla on oikeus tarkastaa, oikaista ja pyytää poistamaan tietosi sekä vastustaa käsittelyä. Pyynnöt sähköpostilla rekisterinpitäjälle."),
]
