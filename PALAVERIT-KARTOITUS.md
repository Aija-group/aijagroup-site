# Palaverikartoitus – 11 asiakasta

**Tarkistettu 22.9.2026 · DNS, sähköposti, alusta ja asennustapa**

Jokainen rivi on tarkistettu suoraan verkosta (nimipalvelimet, MX-tietueet, palvelinohjelmisto, sivun alusta). Tiedot ovat julkisia – asiakkaalta ei ole kysytty mitään.

---

## Yhteenveto

| Asiakas | Alusta | Missä posti | Asennustapa | Riski |
|---|---|---|---|---|
| hapetor.fi | WordPress + Woo | Domainhotelli (sama hosting) | Tapa 1 | pieni |
| tkwiring.fi | **Webnode** | **Webnode** (sama palvelu) | erikoistapaus | **suuri** |
| ppkiinteistopalvelut.fi | WordPress | Hostingpalvelu (sama hosting) | Tapa 1 | pieni |
| mmautopalvelut.fi | suljettu julkaisujärjestelmä | Rackspace (erillinen) | Netlify + DNS | keskisuuri |
| rakennusalaoja.fi | WordPress | **Google Workspace** | Tapa 1 tai Netlify | pieni |
| mittamatti.com | suljettu julkaisujärjestelmä | Rackspace (erillinen) | Netlify + DNS | keskisuuri |
| kotikantaja.fi | WordPress | Hostingpalvelu (sama hosting) | Tapa 1 | pieni |
| nhv.fi | **domainia ei ole olemassa** | – | – | – |
| iv-team.fi | WordPress **5.8.16** | **samalla palvelimella kuin sivu** | **vain Tapa 1** | **suuri jos DNS:ään kosketaan** |
| timapuu.fi | WordPress | Kotisivut.com (sama hosting) | Tapa 1 | pieni |
| omia.fi | WordPress | **Microsoft 365** | Tapa 1 tai Netlify | pieni |

**Tapa 1** = uusi sivu ladataan asiakkaan nykyiseen webhotelliin, DNS:ään ei kosketa. Turvallisin.

---

## Kolme, jotka vaativat erityishuomiota

### iv-team.fi – älä koske DNS:ään

MX-tietue osoittaa suoraan domainiin, eli **sähköposti tulee samalle palvelimelle kuin verkkosivu**. Jos sivuston osoitetietue vaihdetaan Netlifyyn, sähköposti lakkaa toimimasta samalla sekunnilla.

→ Tälle asiakkaalle **vain Tapa 1**. Ei Netlifyä, ei DNS-muutoksia, ei poikkeuksia.

Myyntikulma on tässä poikkeuksellisen vahva: WordPress-versio on **5.8.16**, eli sivua ei ole päivitetty vuosiin. Se on tietoturvariski, jonka voi näyttää asiakkaalle ruudulta.

### tkwiring.fi – Webnode hostaa myös sähköpostin

Sivu on Webnodella, suljetulla julkaisualustalla. Ei tiedostokansiota, johon asentaa. Mutta pahempi juttu: **myös sähköposti on Webnodella**.

Eli jos Webnoden tilaus irtisanotaan, sähköpostit katoavat. Vaihtoehdot:
1. Sähköposti siirretään ensin muualle (Google Workspace ~6 €/kk/käyttäjä tai M365), sitten Webnode pois
2. Webnoden tilaus pidetään pelkän sähköpostin takia – toimii, mutta asiakas maksaa turhasta

**Tätä ei myydä ennen kuin sähköpostiratkaisu on päätetty.** Ota asia esiin palaverissa: "Missä teidän sähköpostinne on?" Jos vastaus on "sivujen mukana", tiedät tilanteen.

Toni Kangas on sama yrittäjä kuin MM Autopalveluissa – voitte käsitellä molemmat samassa palaverissa.

### nhv.fi – domainia ei ole

Tarkistin rekisteristä: `nhv.fi` ei ole rekisteröity kenellekään. Tarkista kirjoitusasu asiakkaalta. Jos yrityksellä ei vielä ole domainia, se on itse asiassa hyvä lähtökohta – ei vanhaa sivua purettavaksi, ei sähköpostia vaarassa, ja voit rekisteröidä domainin asiakkaan nimiin osana toimitusta.

---

## Kaksi samalla alustalla

**mmautopalvelut.fi ja mittamatti.com** ovat samalla suljetulla julkaisualustalla: sama palvelin, sama nimipalvelinratkaisu (Amazonin Route 53), sama sähköpostipalvelu (Rackspace). Sama toimittaja hoitaa siis molempia.

Seuraukset:
- Ei tiedostokansiota → uusi sivu jää Netlifyyn, DNS-tietueet vaihdetaan
- Sähköposti on eri palvelussa kuin sivu → **DNS-muutos ei riko sähköpostia**, mikä on hyvä uutinen
- **Mutta nykyinen toimittaja hallitsee nimipalvelimia.** Vaihto vaatii joko heidän myötävaikutuksensa tai nimipalvelinten siirron. Toimittaja, joka on menettämässä asiakkaan, ei välttämättä kiirehdi

→ Selvitä palaverissa: kuka hoitaa nykyisiä sivuja, mitä se maksaa kuussa, ja onko asiakkaalla itsellään domain-tunnukset.

---

## Neljä helppoa

**ppkiinteistopalvelut.fi ja kotikantaja.fi** ovat molemmat Hostingpalvelu.fi:llä, sama WordPress-versio, sama sähköpostijärjestely. Täsmälleen sama asennus molemmille – tee ensimmäinen, toinen menee rutiinilla.

**hapetor.fi** on Domainhotellilla, posti samassa. Tapa 1.

Huomio Hapetorista: sivulla on WooCommerce, ja päätimme aiemmin, että asiakas päivittää tuotteita WordPressin puolella piilo-osoitteessa. Eli **WordPressiä ei saa poistaa** – se siirretään sivuun (esim. alidomainiin), ei roskiin. Tämä on ainoa asiakas, jossa vanha järjestelmä jää pyörimään.

**timapuu.fi** on Kotisivut.com-palvelussa, posti samassa. Tapa 1, mutta paneeli on kotisivut.com:n oma eikä Plesk – pyydä kuvakaappaus paneelin etusivusta, niin katson ennen asennusta.

---

## Kaksi, joissa sähköposti ei ole vaarassa

**rakennusalaoja.fi** – posti on Google Workspacessa. **omia.fi** – posti on Microsoft 365:ssä.

Näissä molemmat tavat toimivat. Tapa 1 on silti yksinkertaisempi, koska DNS:ään ei tarvitse koskea lainkaan ja sivu on jo valmis.

---

## Kysymykset, jotka kannattaa kysyä joka palaverissa

1. **Missä teidän sähköpostinne on?** Tärkein kysymys. Jos vastaus on epävarma, älä lupaa aikataulua
2. **Kuka hoitaa nykyisiä sivuja ja mitä se maksaa kuukaudessa?** Tästä saat säästölaskelman ja tiedät, kilpailetko jotakuta vastaan
3. **Kenellä on hostingin ja domainin tunnukset?** Jos kukaan ei tiedä, se on oma projektinsa
4. **Kuka päättää?** Erityisesti jos paikalla on useampi osakas

---

## Muistutus itselle

Tiedot on tarkistettu 22.9.2026. Nimipalvelimet ja sähköpostijärjestelyt voivat muuttua – tarkista uudelleen ennen asennusta, älä luota kuukauden vanhaan kartoitukseen.
