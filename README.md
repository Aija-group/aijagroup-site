# Äijä Group Oy – verkkosivut (yksisivuinen)

Staattinen sivusto, generoidaan Pythonilla. Ei riippuvuuksia (Pillow valinnainen: favicon.ico, logo.png, og.png).

```
python3 build.py      # -> site/
```

Julkaisu: pudota `site/`-kansion sisältö (tai `aijagroup-netlify.zip`) Netlifyyn tai mihin tahansa staattiseen hostiin.

## Rakenne (3 sivua)

- `/` – kaikki yhdellä sivulla. Copy = Sulon oma teksti (`COPYT.md`, 20.9.2026), rakenne:
  hero ("Älä osta lisää näkyvyyttä viestille, joka ei vielä myy.") → Miksi → Tunnistatko tämän? (8) → Positiointi (5 kysymystä) → Myyntiviesti (9 kysymystä + sitaatti) → Mitä teemme (5) → Mitä jää käteen (7) → Näin työskentelemme (5) → Yhteistyö (Viestiaudit / Positiointi & myyntiviesti / Verkkosivu / Kumppanuus, mailto-CTA:t) → Mediaeuro → Meistä (Sulo, minä-muoto, kuva) → Yhteys
- `/tietosuoja/`, `/kiitos/` (lomakkeen kiitossivu, noindex), `404.html`
- Yhteydenottolomake = Netlify Forms (`data-netlify`, honeypot). **Netlifyssä: Site → Forms → Form notifications → Email → sulo@aijagroup.fi** – muuten viestit jäävät vain Netlifyn paneeliin.

## Brändi

- Paperi `#f4f1ea`, muste `#14130f`, signaalioranssi `#ff4d1a`; Bricolage Grotesque + Inter (Google Fonts)
- Logomerkki: musta pyöristetty neliö, kaksi oranssia pistettä (ä:n pisteet) + viiva. SVG `build.py`:n `MARK`-muuttujassa, PNG:t generoidaan.

## Kuva

Perustajan portretti `src/img/sulo-maki.jpg` (1200×1500, rajattu alkuperäisestä `sulo kuva (1).png`). Neliöversio some/Googleen: `logo/sulo-maki-nelio-1024.jpg`.

## Copyn muokkaus

Tekstit ovat `content.py`:ssä rakenteina; `COPYT.md` on Sulon alkuperäinen. Lihavointi `**näin**` toimii FOUNDER-kappaleissa.

## Vahvista ennen julkaisua (content.py)

- Domain `aijagroup.fi` ja sähköposti `sulo@aijagroup.fi` – OLETUKSIA
- `SITE["ytunnus"]`, `SITE["linkedin"]` – tyhjät, ei näytetä ennen täyttöä
- Perustajan tekstit (`FOUNDER`) – kirjoitettu Sulon oman kuvauksen pohjalta, tarkista sävy

## Arkisto

`_arkisto/` sisältää aiemmat versiot: v2 (palvelusivut), v3 (taitolista), v4 (D2C-ketju), v5 (positio ensin), v6 (viesti on).

## Julkaisu (Netlify + Cloudflare DNS)

1. app.netlify.com → Add new site → Deploy manually → pudota `aijagroup-netlify.zip` (tai `site/`-kansio).
2. Site configuration → Forms → Enable form detection; Form notifications → Email → sulo@aijagroup.fi. **Tee uusi deploy detectionin jälkeen** – Netlify rekisteröi lomakkeen vain build-hetkellä, muuten POST → 404.
3. Domain management → Add domain → aijagroup.fi (+ www). Netlify näyttää tarvittavat tietueet.
4. Cloudflare DNS (Proxy status **DNS only**, harmaa pilvi):
   - `A`     `@`    `75.2.60.5`
   - `CNAME` `www`  `<sitename>.netlify.app`
5. Netlify → HTTPS → Verify DNS → sertifikaatti tulee itsestään (Let's Encrypt).
6. Project configuration → General → Powered by Netlify badge → Off.
7. Uusi projekti on Private by default → Make public.

Päivitykset: `python3 build.py` → pudota uusi zip Netlifyn Deploys-välilehdelle.

## GA4 ja Meta Pixel

Tunnukset `content.py` → `TRACKING`. **Tyhjä arvo = työkalua ei ladata lainkaan**, jolloin sivu pysyy evästeettömänä eikä bannerivaadetta ole.

```python
TRACKING = {
    "ga4": "G-XXXXXXXXXX",
    "meta_pixel": "1234567890123456",
    "google_ads": "",   # valinnainen
}
```

Kun vähintään yksi tunnus on täytetty, build lisää automaattisesti:
- **Google Consent Mode v2** -oletukset (kaikki mainos- ja analytiikkasuostumukset `denied`) ennen gtag-latausta
- **GA4** latautuu heti, mutta ilman suostumusta evästeettömänä pinginä (advanced consent mode → mallinnus toimii)
- **Meta Pixel latautuu vasta hyväksynnän jälkeen** – Metalla ei ole consent mode -tukea, joten sitä ei saa ladata etukäteen
- Evästebanneri (Hyväksy kaikki / Vain välttämättömät), valinta `localStorage`-avaimessa `aija-consent`
- Footerin **Evästeasetukset**-painike, josta valinnan voi muuttaa
- Tietosuojaselosteen evästeosiot

**Tapahtumat:** mailto-klikki → GA4 `contact_click` + Meta `Contact`; lomakkeen lähetys → `form_submit` + `InitiateCheckout`; `/kiitos/` → `generate_lead` + `Lead`.

**Testaus julkaisun jälkeen:** GA4 → Raportit → Reaaliaikainen; Meta → Events Manager → Test Events. Chromen kehittäjätyökaluista Application → Local Storage näyttää suostumuksen tilan.
