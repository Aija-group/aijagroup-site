# Asennus asiakkaan webhotelliin – työohje

**Äijä Group · 22.9.2026**
Kun asiakkaalla on Plesk, cPanel, DirectAdmin tai muu webhotelli ja sähköposti sen takana (webmail), uusi sivu asennetaan tänne eikä Netlifyyn. **Nimipalvelimiin, MX-tietueisiin tai sähköpostiin ei kosketa lainkaan.**

Kokonaisaika kun sivu on valmis: **30–45 min**, josta puolet varmuuskopiointia.

---

## Vaihe 0 – Kartoitus (ennen kuin mitään rakennetaan)

Kirjaa nämä asiakasprojektin `README.md`:hyn:

| Tieto | Mistä | Miksi |
|---|---|---|
| Paneelin osoite ja tunnukset | asiakkaalta | Plesk `:8443`, cPanel `:2083` |
| Juurikansio | Tiedostot | `httpdocs` (Plesk) / `public_html` (cPanel) |
| PHP-versio | Dev Tools → PHP | Lomake vaatii 7.4+ |
| Nykyinen alusta | Tiedostot | WordPress (`wp-config.php`), Joomla (`configuration.php`), muu |
| Onko tietokanta | Tietokannat | WP → kyllä, pitää varmuuskopioida |
| Sähköpostitilit | Sähköposti | **Ei kosketa** – kirjaa vain, mitä on |
| Lomakkeen vastaanottaja | asiakkaalta | Mieluiten domainin oma osoite |
| Vanhat URLit | Google `site:domain.fi` | 301-ohjaukset, ettei SEO katoa |

---

## Vaihe 1 – Varmuuskopiot (ÄLÄ ohita)

Kaikki tallennetaan asiakasprojektin kansioon `_materiaali/`.

**1a. Tiedostot**
- Plesk: Koontinäyttö → **Varmuuskopioi ja palauta → Varmuuskopioi** → valitse *Konfiguraatio ja sisältö*, **poista rasti sähköpostiviesteistä** (ne ovat usein gigatavuja eikä niitä olla koskemassa) → lataa valmis paketti koneelle.
- Tai pienemmillä sivuilla: Tiedostot → juurikansio → **Näytä piilotiedostot päälle** → valitse kaikki → Pakkaa → lataa zip → poista zip palvelimelta.
- cPanel: **Backup Wizard → Download a Home Directory Backup**.

**1b. Tietokanta (jos WordPress/Joomla/muu CMS)**
- Plesk: Tietokannat → tietokanta → **Vie dump** → lataa `.sql.gz`.
- cPanel: phpMyAdmin → Vie → Nopea → SQL.
- Ota talteen myös `wp-config.php`:n tietokantatunnukset – ilman niitä dumpin palautus on työlästä.

**1c. Kuvakaappaukset**
- **Isännöinti ja DNS → DNS-asetukset** – koko lista. Tätä ei muuteta, mutta se on henkivakuutus.
- **Sähköposti → Sähköpostitilit** – mitä osoitteita on olemassa.
- Vanhan sivun etusivu ja tärkeimmät alasivut (vertailukuvat asiakkaalle).

**1d. Sisältö talteen ennen poistoa**
Kuvat, PDF:t, hinnastot vanhasta `wp-content/uploads`-kansiosta – usein ainoa paikka, missä asiakkaan omat valokuvat ovat.

> **Tarkistus ennen jatkoa:** avaa ladattu zip koneella ja varmista, että se aukeaa ja sisältää `index.php`/`index.html`. Rikkinäinen varmuuskopio huomataan vasta kun sitä tarvitaan.

---

## Vaihe 2 – Generaattori webhotelli-tilaan

Kopioi tämän kansion `hosting.py` asiakasprojektin juureen. Lisää `build.py`:hyn:

```python
from hosting import HOSTING, form_attrs, hidden_fields, write_host_files
```

Lomake (`contact_form`-funktio) – korvaa Netlify-attribuutit:

```python
return f"""<form class="form" id="{id_}" name="yhteydenotto" method="POST" {form_attrs()}>
{hidden_fields()}
  ... kentät ennallaan ...
</form>"""
```

`build()`-funktion loppuun, ennen zipin luontia:

```python
write_host_files(OUT,
    vastaanottaja="info@asiakas.fi",
    domain="asiakas.fi",
    sivusto="Asiakas Oy",
    redirects={"/vanha-sivu.html": "/palvelut/uusi/"})   # 301-ohjaukset vanhoilta URLeilta
```

Ajo:
```bash
python3 build.py                  # webhotelli: .htaccess + lahetys.php mukaan
HOSTING=netlify python3 build.py  # sama koodi Netlifylle, jos asiakas vaihtaa myöhemmin
```

Sama koodipohja toimii molempiin – asiakasta ei tarvitse lukita kumpaankaan.

---

## Vaihe 3 – Lomake ja toiminnallisuudet

| Netlifyllä | Webhotellissa |
|---|---|
| `data-netlify="true"` | `lahetys.php` (tässä kansiossa) |
| Netlify Forms -arkisto | `.lomake-loki.txt` palvelimella + sähköposti |
| Netlify Functions | PHP-tiedosto samassa kansiossa |
| `_redirects` | `.htaccess` → `Redirect 301` |
| `_headers` | `.htaccess` → `<IfModule mod_headers.c>` |

**`lahetys.php` sisältää:** honeypot, 3 sekunnin aikatarkistus, pakolliset kentät, sähköpostiosoitteen validointi, otsakeinjektion esto, `Reply-To` lähettäjään, ja varmuuskopiolokin levylle (sähköposti voi kadota, loki ei).

**Tärkeää `From`-osoitteesta:** sen pitää olla asiakkaan **oman domainin** osoite (`no-reply@asiakas.fi`), ei lähettäjän Gmail. Muuten SPF hylkää viestin ja lomake näyttää toimivan vaikka posti katoaa. Osoitteen ei tarvitse olla oikea postilaatikko.

**Muut toiminnallisuudet staattisella sivulla:**
- Kartta → Google Maps -upotus tai staattinen kuva + linkki
- Ajanvaraus → linkki asiakkaan omaan järjestelmään (Vello, Timma), ei upotusta
- Verkkokauppa → ei staattisella; silloin WooCommerce jää tai siirrytään Shopifyyn
- Uutiset/blogi → `content.py`:hyn; jos asiakas haluaa itse kirjoittaa, harkitse erikseen

---

## Vaihe 4 – Asennus (~15 min)

1. `python3 build.py` → tarkista paikallisesti selaimessa, myös mobiilileveys.
2. Pakkaa **`site/`-kansion sisältö**, ei kansiota:
   ```bash
   cd site && zip -r ../asiakas-site.zip . -x '.DS_Store' && cd ..
   ```
   (`-r . ` ottaa myös `.htaccess`:n mukaan – tarkista `unzip -l asiakas-site.zip | grep htaccess`)
3. Paneeli → Tiedostot → juurikansio → **Näytä piilotiedostot** → valitse kaikki vanhat → **Poista**.
   Jätä rauhaan: `.well-known` (sertifikaatit), `cgi-bin`, mahdolliset paneelin omat tiedostot.
4. **Lataa** zip → klikkaa sitä → **Pura arkisto** → poista zip.
5. **Oikeudet** (jos lomake antaa 500): `lahetys.php` → 644, kansiot 755.

---

## Vaihe 5 – SSL ja tarkistukset

1. **SSL/TLS-varmenteet → Asenna ilmainen Let's Encrypt** → rastita domain **ja** www. cPanelissa AutoSSL hoitaa itse.
2. HTTP→HTTPS-ohjaus: joko paneelista (Plesk: Isännöinnin asetukset → *SEO-turvallinen 301*) **tai** `.htaccess`:sta – **ei molempia**, muuten tulee ohjaussilmukka. Suositus: paneelista, ja kommentoi `.htaccess`:n HTTPS-lohko pois.
3. Läpikäynti:
   - [ ] `https://domain.fi` ja `https://www.domain.fi` aukeavat ilman varoitusta
   - [ ] Jokainen alasivu, valikko ja footer-linkki
   - [ ] Olematon osoite → oma 404-sivu
   - [ ] Mobiili 375 px, ei vaakavieritystä
   - [ ] **Lomake: lähetä testiviesti → tuliko sähköposti?** Tarkista myös roskaposti.
   - [ ] Vanha URL (esim. `/yhteystiedot.html`) → ohjautuu uudelle
   - [ ] **Sähköposti: lähetä ja vastaanota viesti asiakkaan osoitteeseen, avaa webmail.** Pitää toimia kuten ennen, koska mitään ei muutettu.
4. Google Search Console → lisää sivusto → lähetä `sitemap.xml`.

**Rollback:** pura `_materiaali/`-varmuuskopio takaisin juurikansioon. Kesto ~5 min. Kerro asiakkaalle, että tämä on olemassa – se poistaa jännityksen.

---

## Vaihe 6 – Päivitykset jatkossa

**Tapa A – zip (yksinkertaisin, sopii harvoin muuttuviin sivuihin)**
`python3 build.py` → zip → Tiedostot → Pura. Vanhoja tiedostoja ei tarvitse poistaa, purku korvaa ne.

**Tapa B – Plesk Git -webhook (kun päivityksiä tulee usein)**
1. Repo `Aija-group/<asiakas>-site`, jossa **`site/`-kansio on commitoitu** (poista se `.gitignore`sta – Plesk ei aja buildia).
2. Plesk → **Git → Lisää repositorio** → repon URL → haara `main` → julkaisutila **Automaattinen** → julkaisukansio `httpdocs`, lähdekansio `/site`.
3. Plesk antaa webhook-URLin → GitHub → repo → Settings → Webhooks → Add.
4. Jatkossa: `python3 build.py && git add -A && git commit -m "..." && git push` → sivu päivittyy.
   Ei DNS-muutoksia, ei paneeliin kirjautumista.

**Tapa C – SFTP** (Cyberduck/Transmit) yksittäisen tiedoston pikakorjaukseen.

> Muista: jos asiakas päivittää itse jotain paneelista, se katoaa seuraavassa julkaisussa. Sano tämä ääneen luovutuksessa.

---

## Yleisimmät ongelmat

| Oire | Syy | Korjaus |
|---|---|---|
| Alasivut 404 | `.htaccess` ei purkautunut (piilotiedosto) | Näytä piilotiedostot, tarkista että se on juuressa |
| Loputon ohjaussilmukka | HTTPS-ohjaus sekä paneelista että `.htaccess`:sta | Poista toinen |
| Lomake → 500 | PHP-versio tai tiedoston oikeudet | PHP 7.4+, `lahetys.php` 644 |
| Lomake näyttää onnistuvan, posti ei tule | `From` väärällä domainilla → SPF hylkää | `no-reply@<asiakkaan domain>` |
| Posti roskapostiin | Hostin IP:n maine | Lisää `Reply-To`, testaa mail-tester.com |
| Zipin purku loi `site/`-kansion | Pakattiin kansio eikä sisältöä | `cd site && zip -r ../x.zip .` |
| Vanha sivu näkyy yhä | Selaimen tai paneelin välimuisti | Kovalataus, Plesk: tyhjennä nginx-välimuisti |
| Let's Encrypt epäonnistuu | Domain ei osoita tähän palvelimeen tai `.well-known` poistettu | Tarkista A-tietue ja kansio |
| WP jätti `.htaccess`:n | Vanha tiedosto jäi juureen | Poista ja pura uusi |

---

## Mitä vanhalle WordPressille tehdään

1. Varmuuskopioi tiedostot **ja tietokanta** (vaihe 1).
2. Poista tiedostot juurikansiosta.
3. **Tietokanta jätetään toistaiseksi paikalleen** – se ei häiritse eikä vie tilaa mainittavasti. Poista vasta kun asiakas on hyväksynyt uuden sivun ja varmuuskopio on tallessa, aikaisintaan kuukauden päästä.
4. WP-lisäosien tilaukset (esim. maksullinen teema, Elementor Pro, varmuuskopiolisäosa) voi irtisanoa – kerro asiakkaalle, se on hänelle säästö.
5. Jos asiakkaalla oli WP:n kautta lähtevä posti (esim. Contact Form 7), varmista että uusi `lahetys.php` osoittaa samaan osoitteeseen.
