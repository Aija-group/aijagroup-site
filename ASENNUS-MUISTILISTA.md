# Sivuston myynti ja asennus – muistilista

**Äijä Group · päivitetty 22.9.2026 · ei vaadi koodausta**

Meidän tapamme: **sivu rakennetaan ensin, myydään sitten, asennetaan viimeiseksi.**
Siksi tässä on kaksi eri osaa. Osa A tehdään ennen kauppaa meidän omalla hostingilla. Osa B tehdään kaupan jälkeen asiakkaan omaan webhotelliin.

Netlify ja asiakkaan webhotelli eivät ole kilpailevia vaihtoehtoja, vaan peräkkäisiä vaiheita: Netlify on myyntityökalu, webhotelli on lopullinen koti.

---

# OSA A – Demo myyntiä varten

Tehdään ilman yhteyttä asiakkaaseen. Asiakkaan tunnuksia ei tarvita eikä kysytä.

## A1. Ennen rakennusta – tarkista alusta

Kerro minulle asiakkaan domain, niin katson:
- onko asiakkaalla webhotelli (Plesk/cPanel) vai suljettu palvelu (Wix, Squarespace, Kotisivukone)
- onko domainilla sähköposti

**Miksi tämä on tärkeää:** jos asiakkaalla ei ole webhotellia, sinne ei voi asentaa mitään. Silloin sivu jää Netlifyyn pysyvästi ja kaupan jälkeen vaihdetaan DNS-tietueita. Se on eri keskustelu asiakkaan kanssa, ja parempi tietää etukäteen kuin kaupan jälkeen.

## A2. Rakennus

Sivu tehdään asiakkaan julkisten tietojen pohjalta. Kerro minulle:
- mitä palveluita korostetaan
- onko käytettävissä omia kuvia (jos ei, teen AI-kuvat)

## A3. Demo verkkoon

Minä hoidan tämän. Sivu tulee osoitteeseen **`asiakas.aijagroup.fi`** – oman domainisi alle, ei `netlify.app`-osoitteeseen. Näyttää myyntitilanteessa paremmalta.

Jokaisessa demossa on automaattisesti:
- **hakukone-esto** – demo ei saa näkyä Googlessa eikä kilpailla asiakkaan oikean sivun kanssa
- **lomake ohjattu sinulle**, ei asiakkaalle – muuten asiakas saa yhteydenottoja sivustolta, jota hän ei tiedä olevan olemassa
- footerissa pieni merkintä "Sivustoehdotus – Äijä Group Oy"

## A4. Myynti

Lähetä asiakkaalle linkki. Sivu toimii puhelimella, joten sen voi näyttää myös kasvotusten.

---

# OSA B – Asennus kaupan jälkeen

Nyt saat asiakkaan tunnukset. Sähköpostit eivät ole vaarassa missään vaiheessa: vaihdamme vain yhden kansion sisällön. Sähköposti, webmail ja domain-asetukset jäävät koskematta.

## B1. Pyydä asiakkaalta

- Pleskin (tai vastaavan paneelin) tunnukset
- Mihin sähköpostiin yhteydenottolomakkeen viestit ohjataan?
- Omat valokuvat, logo, hinnasto – jos niitä on
- Onko vanhalla sivulla jotain, mikä pitää ehdottomasti säilyttää
- **Kuvakaappaus paneelin etusivusta** – siitä näen paneelin tyypin, palvelinohjelmiston ja PHP-version ja kerron, onko jotain poikkeavaa ennen kuin aloitat

Kerro nämä minulle. Vaihdan lomakkeen osoittamaan asiakkaalle, poistan demomerkinnän ja hakukone-eston, ja annan sinulle **yhden zip-tiedoston**.

## B2. Varmuuskopio – tärkein vaihe

Koontinäyttö → **Varmuuskopioi ja palauta** → **Varmuuskopioi**

| Kohta | Valinta | Miksi |
|---|---|---|
| Määritys | harmaana, ei voi muuttaa | – |
| **Viestit** | **⬜ rasti pois** | Tämä on sähköpostilaatikoiden sisältö, usein 1–2 GB. Emme koske sähköpostiin, joten sitä ei tarvitse kopioida |
| Käyttäjän tiedostot | ✅ | Itse sivusto |
| Tietokannat | ✅ | WordPressistä puolet on täällä |
| Tallenna kohteeseen | Palvelimen säilytystila | – |
| **Tyyppi** | **Täysi** (ei Kasvava) | Kasvava toimii vain, jos sitä edeltävä täysi kopio on yhä olemassa. Oma kopio pitää toimia yksinään |
| Kommentit | `Ennen sivu-uudistusta – Äijä Group <pvm>` | Erottaa oman kopiosi hostingin "Scheduled Backup" -riveistä |
| Jätä pois lokitiedostot | ✅ | Pienempi tiedosto |
| Sähköposti-ilmoitus | ⬜ tyhjäksi | Kenttään on valmiiksi täytetty **asiakkaan** osoite – hän saisi turhan ilmoituksen |

→ **OK** → odota (ilman viestejä muutama minuutti) → uusi rivi ilmestyy listaan omalla kommentillasi → klikkaa rivin lopun **vihreää latausnuolta** → salasanasuojauksen voi ohittaa → tallenna asiakkaan kansioon `_materiaali/`.

**Avaa ladattu tiedosto koneella** ja tarkista että se aukeaa eikä ole tyhjä. Testaamaton varmuuskopio on arvaus.

Lopuksi **poista varmuuskopio palvelimelta** – se vie levytilaa, jota tileillä on usein niukasti.

**Jos vanha sivu on WordPress:** ota lisäksi tietokanta.
Vasemmalta **Tietokannat** → **Vie dump** → lataa tiedosto. Pelkkä tiedostojen varmuuskopio ei riitä WordPressille, koska puolet sivusta on tietokannassa.

**Kaksi kuvakaappausta varmuuden vuoksi:**
**Isännöinti ja DNS → DNS-asetukset** ja **Sähköposti → Sähköpostitilit**. Emme muuta niitä, mutta tieto on sitten tallessa.

> Tämä vaihe tekee kaikesta muusta turvallista. Jos jokin menee pieleen, vanha sivu palautuu tästä noin viidessä minuutissa.

### Jos palautat varmuuskopion joskus myöhemmin

**Palauta vain sivusto – ota rasti pois sähköposteista.** Palautusikkuna kysyy, mitä palautetaan. Jos palautat koko paketin, myös postilaatikot palautuvat siihen päivään ja välissä saapuneet viestit katoavat. Sivuston rikkoutuminen on pieni harmi, asiakkaan sähköpostien katoaminen ei ole.

### Hostingpalvelun omat aikataulutetut varmuuskopiot

Useimmilla hosteilla on lista valmiita varmuuskopioita ("Scheduled Backup"). Ne ovat hyvä nopea peruutus samana päivänä, mutta:
- ne **katoavat noin 7–14 päivässä** kierrossa
- ne kuuluvat hostingpalvelulle, joka voi muuttaa käytäntöä kertomatta
- ne sisältävät yleensä sähköpostit, mikä tekee palautuksesta vaarallisemman

Siksi oma ladattu kopio otetaan aina, vaikka lista näyttäisi täydeltä.

## B3. Siirrä vanha sivu syrjään (älä poista)

Turvallisempi kuin poistaminen: vanha sivu jää palvelimelle, muutaman klikkauksen päässä.

1. **Tiedostot** → avaa **httpdocs**
2. **Laita piilotiedostot näkyviin** (oikean yläkulman asetusvalikko). **Tämä on pakollinen WordPress-tapauksissa:** WP:n oma `.htaccess` on piilotiedosto, ja jos se jää paikalleen, uusi sivu ei toimi lainkaan tai jää ohjaussilmukkaan
3. **Luo** → *Hakemisto* → nimi `_vanha`
4. Valitse kaikki muu otsikkorivin valintaruudusta, ja **ota rasti pois** kohdista `_vanha` ja `.well-known` (jälkimmäinen liittyy SSL-varmenteeseen – sitä ei saa siirtää eikä poistaa)
5. **Siirrä** → kohteeksi `_vanha` → OK

**Peruutus jos jokin menee pieleen:** avaa `_vanha`, valitse kaikki, Siirrä → `httpdocs`. Vanha sivu on takaisin minuutissa – ei varmuuskopion latausta, ei odottelua.

Poista `_vanha` vasta noin viikon kuluttua, kun asiakas on hyväksynyt uuden sivun.

Minä lisään ohjaustiedostoon rivin, joka estää pääsyn `_vanha`-kansioon selaimesta – muuten vanha sivu näkyisi osoitteessa `domain.fi/_vanha/` ja voisi päätyä Googleen.

## B4. Lataa uusi sivu

Samassa näkymässä:
- **Lataa** → valitse minulta saamasi zip
- Klikkaa zip-tiedostoa → **Pura arkisto**
- Poista zip, kun purku on valmis

## B5. SSL päälle

**SSL/TLS-varmenteet** → **Asenna ilmainen perusvarmenne** → rastita sekä `domain.fi` että `www.domain.fi`.

Sitten **Isännöinti ja DNS → Isännöinnin asetukset** → päälle
*"Pysyvä SEO-turvallinen 301-uudelleenohjaus HTTP:stä HTTPS:ään"*.

## B6. Tarkista

- [ ] `https://domain.fi` ja `https://www.domain.fi` aukeavat ilman varoituskolmiota
- [ ] Valikon kaikki sivut läpi
- [ ] Sivu puhelimella
- [ ] **Täytä lomake ja lähetä** → tuliko sähköposti asiakkaan osoitteeseen? Katso myös roskaposti
- [ ] **Lähetä testiviesti asiakkaan sähköpostiin ja avaa webmail** → toimii kuten ennen
- [ ] Google-haku vanhalla sivulla (`site:domain.fi`) → klikkaa pari vanhaa osoitetta, ohjautuvatko uusille

Jos jokin ei toimi, kerro minulle mikä. Älä säädä Pleskin asetuksia itse.

## B7. Luovutus

- Kerro asiakkaalle, mihin sähköpostiin lomakeviestit tulevat
- Kerro, miten muutoksia pyydetään (sinulta, ei paneelista)
- Vanha tietokanta jätetään palvelimelle vähintään kuukaudeksi – toinen turvaverkko
- WP-lisäosien maksulliset tilaukset voi irtisanoa → asiakkaalle säästöä, kerro se

---

# Jos jokin menee pieleen

**Nopein peruutus:** siirrä `_vanha`-kansion sisältö takaisin httpdocsiin (vaihe B3). Minuutti.

**Jos se ei riitä:** Varmuuskopioi ja palauta → valitse varmuuskopio → **Palauta** → **vain sivusto, ei sähköposteja**.

| Oire | Tee tämä |
|---|---|
| Sivu ei näy ollenkaan | Odota 5 min, lataa uudelleen Cmd+Shift+R |
| Alasivut antavat virheen | Laita piilotiedostot näkyviin httpdocsissa, katso onko `.htaccess` siellä – jos ei, kerro minulle |
| Lomake ei lähetä | Kerro minulle. Älä poista mitään |
| Varmuuskopio: "ei tarpeeksi levytilaa" | Kerro minulle – otetaan pelkkä httpdocs zipinä, se on paljon pienempi |
| Varmuuskopio jumissa "käynnissä" | Normaalia isolla tilillä. Anna olla, älä käynnistä uutta |

---

# Muut paneelit kuin Plesk

Logiikka on identtinen, vain nimet vaihtuvat.

| Asia | Plesk | cPanel | DirectAdmin |
|---|---|---|---|
| Tiedostonhallinta | Tiedostot | File Manager | File Manager |
| Sivuston kansio | `httpdocs` | `public_html` | `public_html` |
| Piilotiedostot | asetusvalikko → Näytä piilotiedostot | Settings → Show Hidden Files | asetuksissa |
| Siirto | Siirrä | Move | Move |
| Varmuuskopio | Varmuuskopioi ja palauta | Backup Wizard / JetBackup | Create Backup |
| Tietokanta ulos | Tietokannat → Vie dump | phpMyAdmin → Export | phpMyAdmin → Export |
| SSL | Asenna Let's Encrypt | AutoSSL (usein automaattinen) | Let's Encrypt |
| HTTPS-pakotus | Isännöinnin asetukset | Domains → Force HTTPS Redirect | vastaava valinta |

**Kolme asiaa, jotka voivat poiketa:**

**Palautus.** Pleskissä palautat itse. Monissa cPanel-hotelleissa täyden palautuksen tekee vain tuki, ja se voi kestää vuorokauden. Siksi `_vanha`-kansio on cPanelissa vielä tärkeämpi – se on peruutus, joka ei vaadi keneltäkään mitään.

**Palvelinohjelmisto.** Ohjaustiedosto toimii Apachella, joka on käytössä lähes kaikkialla. Erikoistuneissa WordPress-hotelleissa (Seravo, WP-palvelu.fi) pyörii pelkkä nginx, jolloin se ei tee mitään ja ohjaukset hoidetaan paneelin asetuksista. Näen tämän etukäteen paneelin kuvakaappauksesta.

**Lomakkeen lähetys.** Joillakin halvoilla hosteilla PHP:n postitus on estetty roskapostin takia. Selviää testiviestistä (vaihe B6) – kerro minulle, jos viesti ei tule, niin vaihdan lähetystavan.

**Ei paneelia lainkaan, vain FTP-tunnukset?** Onnistuu sekin. Cyberduckilla: luot `_vanha`-kansion, raahaat vanhat sinne, raahaat uudet tilalle. Sama idea, eri työkalu.

---

# Kun vanha sivu on WordPress

Nämä koskevat vain WP-tapauksia ja aiheuttavat useimmat ongelmat.

- **Piilotiedostot näkyviin ennen siirtoa.** WP:n `.htaccess` jää muuten paikalleen ja rikkoo uuden sivun. Tämä on se yksi asia, joka sinun pitää muistaa WP-tapauksissa
- **Tietokanta talteen erikseen.** Pelkkä tiedostojen varmuuskopio ei riitä – puolet WordPressistä on tietokannassa
- **Jätä `wp-content/uploads` paikalleen.** Siellä ovat asiakkaan valokuvat, ja niihin voi olla linkkejä Facebookissa, Google-yrityskortissa tai vanhoissa sähköposteissa. Ei häiritse uutta sivua mitenkään. Käytännössä: siirrä se `_vanha`-kansion sijaan takaisin juureen, tai kerro minulle niin hoidan ohjauksen
- **Tietokanta poistetaan vasta kuukauden päästä**, kun asiakas on hyväksynyt uuden sivun
- **wp-admin-kirjanmerkki lakkaa toimimasta.** Asiakkaalla on selaimessa kirjanmerkki WordPressin hallintaan – kerro etukäteen, muuten tulee puhelu
- **Tarkista vanhan lomakkeen vastaanottaja.** Jos WP:ssä oli Contact Form 7 tms., uuden lomakkeen pitää mennä samaan osoitteeseen, muuten asiakas ihmettelee miksi yhteydenotot loppuivat
- **Evästebanneri ja analytiikka olivat lisäosia** eivätkä siirry mukana. Kerro minulle, jos asiakas haluaa ne

**Hyvä puoli:** WordPress-sivusta saan sisällön ja vanhat osoitteet koneellisesti rajapinnasta. Kerro vain domain – 301-ohjaukset vanhoilta osoitteilta tulevat zippiin valmiina, eikä hakusijoituksia menetetä.

---

# Päivitykset myöhemmin

Kerro mitä muutetaan → saat uuden zipin → toistat vaiheet B3 ja B4.

Jos jonkun asiakkaan sivua päivitetään usein, voin kytkeä automaattisen päivityksen, jolloin sinun ei tarvitse käydä Pleskissä lainkaan. Puhutaan siitä, kun se on ajankohtaista.

---

# Erikoistapaukset

**Asiakkaalla ei ole webhotellia** (Wix, Squarespace, Kotisivukone, tai pelkkä domain)
Sivu jää Netlifyyn. Asiakkaan domainin asetuksiin vaihdetaan kaksi riviä. Jos domainilla on sähköposti, tarkistan ensin ettei se katkea. Tämä on minun työtäni – kerro vain, että näin on.

**Asiakas haluaa muokata tekstejä itse**
Staattinen sivu ei taivu siihen. Vaihtoehdot: muutokset meidän kautta (nopeaa, sisältyy ylläpitoon) tai sivu tehdään WordPressiin. Jälkimmäinen on eri projekti ja eri hinta.

**Asiakkaalla on verkkokauppa**
Staattinen sivu ei korvaa verkkokauppaa. Joko vanha kauppa jää rinnalle omaan osoitteeseen tai tehdään erillinen suunnitelma.
