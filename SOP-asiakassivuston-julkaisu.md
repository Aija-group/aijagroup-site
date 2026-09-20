# SOP – Asiakassivuston toteutus ja julkaisu

**Äijä Group Oy · versio 1.0 · 20.9.2026**
Tämä on toistettava menettely staattisen asiakassivuston rakentamiseen, julkaisuun ja ylläpitoon. Sama putki, jolla aijagroup.fi julkaistiin. Arvioitu kokonaisaika julkaisuun (kun sisältö on valmis): **45–90 min**, josta odottelua noin puolet.

---

## 0. Periaatteet

| Asia | Käytäntö |
|---|---|
| **Domain** | Aina **asiakkaan** nimissä ja asiakkaan rekisteröijällä. Emme koskaan rekisteröi asiakkaan domainia omalle tilillemme. |
| **DNS** | Mieluiten Cloudflare (ilmainen, hyvä UI). Jos asiakas ei halua vaihtaa, käytetään asiakkaan nykyistä DNS-paneelia – riittää, että sinne saa lisättyä kaksi tietuetta. |
| **Lähdekoodi** | GitHub-organisaatio **Aija-group**, repo `<asiakas>-site`. Luovutetaan asiakkaalle pyydettäessä (zip tai siirto heidän GitHubiinsa). |
| **Hosting** | Netlify, tiimi **Äijä group oy**. Yksi projekti per asiakas. |
| **Sopimukseen** | Lause: "Sivuston lähdekoodi ja sisältö ovat asiakkaan omaisuutta ja luovutetaan pyydettäessä. Hosting- ja versionhallintatilit ovat Äijä Groupin hallinnassa ylläpidon ajan." |

**Tilit ja avaimet (Sulon Mac):**
- GitHub: käyttäjä `sulo-commits` (sulo@aijagroup.fi), organisaatio `Aija-group`. SSH-avain `~/.ssh/id_ed25519_aijagroup`, host-alias `github.com-aijagroup`.
- Netlify: sulo@aijagroup.fi (GitHub-kirjautuminen), tiimi "Äijä group oy".
- Cloudflare: sulo@aijagroup.fi. Asiakkaan domain lisätään **omalle Cloudflare-tilillemme** vain jos asiakkaalla ei ole omaa; muuten asiakas luo tilin ja antaa meille *DNS-muokkausoikeuden* (Manage Account → Members).

---

## 1. Aloitus – mitä asiakkaalta tarvitaan

Kerää nämä ennen kuin mitään rakennetaan. Puuttuva tieto tässä vaiheessa on yleisin viivästyksen syy.

- [ ] **Domain**: mikä domain, missä se on rekisteröity (NordicHost, Domainkeskus, Louhi, GoDaddy…) ja **kenellä on tunnukset**.
- [ ] **Sähköposti**: käyttääkö asiakas domainia sähköpostiin (Google Workspace, M365, webhotellin posti)? → MX-tietueet **eivät saa katketa** nimipalvelinvaihdossa.
- [ ] **Nykyinen sivusto**: onko, ja ohjataanko vanhat URL-osoitteet uusille (301-ohjaukset `_redirects`-tiedostoon).
- [ ] **Lomake**: mihin sähköpostiin yhteydenotot ohjataan.
- [ ] **Sisältö**: copy, kuvat, logo, värit (tai päätös, että teemme brändin).
- [ ] **Y-tunnus, osoite, puhelin** footeriin ja tietosuojaselosteeseen.
- [ ] **Analytiikka**: GA4 / Meta Pixel / muut tunnisteet, jos halutaan.

---

## 2. Rakennus (Claude Code + generaattori)

Vakiorakenne (kopioi aijagroup-site-reposta):

```
<asiakas>-site/
  content.py          # kaikki tekstit ja rakenne
  build.py            # generaattori → site/
  netlify.toml        # build-komento, publish-kansio, headerit
  requirements.txt    # Pillow (OG-kuva, favicon)
  src/img/            # kuvat
  src/fonts/          # fontit OG-kuvaan
  README.md           # projektin oma muistio + oletukset
  .gitignore          # site/, *.zip, _materiaali/, .DS_Store
```

Työjärjestys:
1. **Sisältö ensin** – `content.py` täyteen, tekstit asiakkaan hyväksyttäväksi mieluiten `COPYT.md`-muodossa (yksi tiedosto, kaikki tekstit).
2. **Ulkoasu** – `build.py`:n CSS-muuttujat (värit, fontit), rakenneosiot.
3. **Esikatselu paikallisesti** – `python3 build.py` → Browser-paneeli. Tarkista desktop ja mobiili (375 px), ei vaakavieritystä.
4. **Lomake** – `data-netlify="true"` + honeypot + `action="/kiitos/"`. Kiitossivu `noindex`.
5. **Tekninen tarkistus**: `<title>` ja meta description joka sivulle, OG-kuva, favicon, `sitemap.xml`, `robots.txt`, `404.html`, JSON-LD (Organization/LocalBusiness), canonical-linkit.
6. **Tietosuojaseloste** – lomake + evästeet (jos analytiikka) kuvattuna.

> Kaikki oletukset (domain, sähköposti, aikataulut, hinnat), joita ei ole vahvistettu, listataan README:n "Vahvista ennen julkaisua" -kohtaan.

---

## 3. GitHub

1. github.com/Aija-group → **New repository** → nimi `<asiakas>-site`, **Public** (Netlify free ei julkaise organisaation privaatteja repoja; jos asiakas vaatii privaattia → Netlify Pro 20 $/kk tai Cloudflare Pages).
   Ei README:tä, .gitignorea eikä lisenssiä (repo tyhjäksi).
2. Paikallisesti:
   ```bash
   cd <asiakas>-site
   git init -b main
   git add -A && git commit -m "Ensimmäinen versio"
   git remote add origin git@github.com-aijagroup:Aija-group/<asiakas>-site.git
   git push -u origin main
   ```
3. Tarkista, että repo näkyy GitHubissa ja `site/` **ei** ole mukana (.gitignore).

---

## 4. Netlify

1. app.netlify.com → **Add new project → Import an existing project → GitHub** → organisaatio **Aija-group** → valitse repo.
   *Jos repo ei näy:* "Configure the Netlify app on GitHub" → anna Netlifylle pääsy Aija-group-organisaatioon.
2. **Project name**: `<asiakas>` → esikatselu `https://<asiakas>.netlify.app`. Build-asetukset tulevat `netlify.toml`:sta (command `python3 build.py`, publish `site`). Jos kentät ovat tyhjiä, täytä ne. → **Deploy**.
3. Odota build vihreäksi (~1 min). Avaa `<asiakas>.netlify.app` ja tarkista sivu.
4. **Project overview → Make public** (uudet projektit ovat "Private by default" → muuten 401 kaikille).
5. **Forms → Enable form detection**, sitten **Add notification → Email notification** → *New form submission*, sähköposti = asiakkaan osoite, Form = *Any form*.
6. **Tee uusi deploy** (pieni commit + push tai *Deploys → Trigger deploy*). Netlify rekisteröi lomakkeen vain build-hetkellä – ilman tätä lomakkeen lähetys päätyy 404:ään.
7. **Project configuration → General → Powered by Netlify badge → Off**.
8. Lähetä yksi testiviesti lomakkeella → tarkista, että sähköposti tulee.

**Esikatselu asiakkaalle:** `<asiakas>.netlify.app` kelpaa hyväksyntäkierrokseen ennen domainin kytkemistä.

---

## 5. DNS ja domain

### 5A. Jos DNS siirretään Cloudflareen (suositus)

1. **Ennen nimipalvelinvaihtoa:** kirjaa asiakkaan nykyiset DNS-tietueet (etenkin **MX**, SPF-TXT, DKIM, mahdolliset alidomainit). Ota kuvakaappaus.
2. Cloudflare → **Add a domain** → asiakkaan domain → Free. Cloudflare skannaa tietueet – **vertaa kohtaan 1** ja lisää puuttuvat käsin. Sähköposti ei saa katketa.
3. Cloudflare antaa 2 nimipalvelinta (`xxx.ns.cloudflare.com`).
4. Asiakkaan rekisteröijällä (tai asiakas itse): **Nimipalvelimet → omat nimipalvelimet** → syötä Cloudflaren kaksi → tallenna. Tyhjennä muut kentät.
5. Odota, kunnes Cloudflare sanoo "Active" (yleensä 5 min – 2 h, max 24 h). Tarkistus: `dig NS <domain>`.

### 5B. Jos DNS jää asiakkaan nykyiseen paneeliin

Riittää, että sinne lisätään kohdan 6 kaksi tietuetta. Jos paneelia ei ole (kuten NordicHostilla ilman webhotellia), on pakko tehdä 5A.

---

## 6. Domain Netlifyyn + tietueet

1. Netlify → **Domain management → Add a domain** → `<domain>` (tarkista kirjoitusvirheet kirjain kirjaimelta). Netlify lisää `www` automaattisesti. **Älä** valitse Netlify DNS:ää.
2. Cloudflareen (tai asiakkaan DNS-paneeliin) kaksi tietuetta, molemmat **DNS only / ei proxya** (Cloudflaressa harmaa pilvi):

   | Type | Name | Content |
   |---|---|---|
   | `A` | `@` | `75.2.60.5` |
   | `CNAME` | `www` | `<asiakas>.netlify.app` |

3. Tarkista terminaalista:
   ```bash
   dig +short A <domain> @1.1.1.1        # → 75.2.60.5
   dig +short CNAME www.<domain> @1.1.1.1 # → <asiakas>.netlify.app.
   ```
4. Netlify → **HTTPS → Verify DNS configuration**. Näyttää usein "Waiting on DNS propagation" 10–20 min, vaikka dig on oikein – **odota, älä säädä**. Kun "DNS verification was successful", sertifikaatti tulee itsestään muutamassa minuutissa.
5. Tarkista: `https://<domain>` avautuu ilman varoitusta, `http://` ohjaa `https://`, `www` ohjaa päädomainille.

---

## 7. Sähköpostin suojaus (jos domainilla on sähköposti)

Kun DNS on hallinnassamme, varmista nämä TXT-tietueet – muuten asiakkaan sähköpostit ja lomakevastaukset päätyvät roskapostiin:

- **SPF**: `@` → `v=spf1 include:_spf.google.com ~all` (Google) tai `v=spf1 include:spf.protection.outlook.com -all` (M365)
- **DMARC**: `_dmarc` → `v=DMARC1; p=none; rua=mailto:<asiakkaan osoite>`
- **DKIM**: Google Admin → Gmail → Authenticate email → Generate → TXT nimellä `google._domainkey`. M365: admin-keskus → DKIM → kaksi CNAME:a.

---

## 8. Luovutus asiakkaalle

- [ ] Sivusto tarkistettu desktop + mobiili live-osoitteessa.
- [ ] Lomake testattu, viesti tuli asiakkaan sähköpostiin.
- [ ] Google Search Console: lisää domain (DNS TXT -vahvistus), lähetä `sitemap.xml`.
- [ ] Vanhan sivuston 301-ohjaukset toimivat (jos oli).
- [ ] Analytiikka toimii (jos asennettu).
- [ ] Asiakkaalle lyhyt sähköposti: live-osoite, mihin lomakeviestit tulevat, miten muutoksia pyydetään, ja että lähdekoodi luovutetaan pyydettäessä.
- [ ] README:n "Vahvista ennen julkaisua" -lista tyhjennetty tai avoimet kohdat kirjattu asiakkaalle.

---

## 9. Ylläpito ja muutokset

```bash
# muokkaa content.py (tai build.py)
python3 build.py          # tarkista paikallisesti
git add -A && git commit -m "Mitä muutettiin"
git push                  # Netlify julkaisee ~1 min
```

- Jokainen push = uusi julkaisu. Virheellinen julkaisu perutaan Netlifyssä *Deploys → aiempi deploy → Publish deploy* (sekunneissa).
- Lomakeviestit myös Netlify → Forms → `<lomake>`, vaikka sähköposti hukkuisi.
- Ilmaistason rajat: 100 GB liikennettä/kk, 300 build-minuuttia/kk, 100 lomakelähetystä/kk per projekti. Ylitys → Netlify Pro tai lomake Web3Forms/Formspree.

---

## 10. Vianetsintä – tänään opittua

| Oire | Syy | Korjaus |
|---|---|---|
| Rekisteröijän paneelissa ei DNS-asetuksia (esim. NordicHost) | Ei webhotellia → ei DNS-vyöhykettä | Siirrä DNS Cloudflareen (5A) |
| Registry näyttää nimipalvelimet "[Technical Error]" | Nimipalvelin ei vastaa domainille | Sama kuin yllä |
| Google/Netlify ei löydä TXT/A-tietuetta vaikka dig löytää | Tarkistajan välimuisti | Odota 10–20 min, yritä uudelleen |
| `Upgrade to Pro` Netlifyssä repoa valittaessa | Org-privaatti repo free-tasolla | Repo → Settings → Change visibility → Public |
| Sivu antaa 401 "Login Redirect" | Netlify-projekti Private by default | Project overview → Make public |
| Lomake → 404 | Form detection kytketty buildin jälkeen | Uusi deploy |
| Sertifikaattivirhe `*.netlify.app` omalla domainilla | Let's Encrypt ei vielä myönnetty | Odota; tarkista ettei domainissa ole kirjoitusvirhettä |
| "Powered by Netlify" -badge | Uusien free-projektien oletus | Project configuration → General → badge Off |
| GitHub "Too many requests" rekisteröinnissä | IP-/selainrajoitus | Yksityinen ikkuna tai puhelimen verkko, odota 15 min |
| Cloudflaren proxy (oranssi pilvi) päällä | Let's Encrypt -validointi epäonnistuu | Vaihda DNS only |

---

## Liite: Kustannukset per asiakassivusto

| Erä | Hinta |
|---|---|
| Hosting (Netlify free) | 0 €/kk |
| DNS (Cloudflare free) | 0 €/kk |
| Domain | asiakas maksaa rekisteröijälleen (~10–20 €/v) |
| GitHub (org free) | 0 € |
| Lomakkeet yli 100/kk | Netlify Pro 19 $/kk tai ulkoinen lomakepalvelu |

Käytännössä sivuston juoksevat kulut ovat nolla; hinnoittelu perustuu työhön ja ylläpitosopimukseen, ei läpilaskutettuun hostingiin.
