# Cubie v48.33 — visuaalne ülevaatuskandidaat

**Pole kinnitatud lõppversioon ega tootmisfail.** Kohalikud geomeetriakontrollid ja brauserikontroll läbisid; kogu võrgu topoloogiline kontroll ei läbinud.

## Tehtud muudatus

`Cubie_v48_33_3D.html` sisaldab Douki kohalikku lõiget. Säilib 16° kalle; uus põhi on 1 mm paksune, mõõdetuna risti kaldpinnaga. Viies kontrollpunktis mõõdeti paksuseks 0,999998–1,000002 mm.

Kopsiku ja ringava kaitsepiirkondade ning kogu muu lõikevälise konstruktsiooni pinnad taastati kinnitatud HTML-ist. Tervikparanduse katse, mis tekitas kopsikul kuni 4,894 mm hälbe, lükati tagasi; neid muudetud lõikeväliseid pindu selles failis ei kasutata.

Kinnitatud HTML ja algne STL jäid puutumata. Vaaturi kood, kaamera, CSS, juhtimine, liugurid, värvid ning kaheksa muud detailirühma jäid bait-baidilt samaks. Ka algsed v48.32 tekstisildid on säilitatud.

## Koordinaadid ja täpne piirkond

`U = cos(16°)·Y + sin(16°)·Z`; `W = −sin(16°)·Y + cos(16°)·Z`. Kõik pikkused millimeetrites.

| Suurus | Väärtus |
|---|---|
| Kopsiku valitud tagumine tasand | W ≈ 15,704873; Z ≈ 0,28674539·Y + 16,337770 |
| Douki senine põhipind | W ≈ 16,694873; Z ≈ 0,28674535·Y + 17,367668 |
| Vajalik Z-nihe | −1,029896 mm |
| Uus 1 mm põhi | 14,704873 ≤ W ≤ 15,704873 |
| Eemaldus | W < 14,704873 või W > 15,704873, ainult kontuuri sees ning kaitseprismadest väljas |

Kontuur `(X,U)`:

```text
160.2328932160, 86.9408793528
 53.6471067840, 86.9408793528
 53.4400000000, 86.7337725688
 53.4400000000, 54.1479861368
 53.6471067840, 53.9408793528
160.2328932160, 53.9408793528
160.4400000000, 54.1479861368
160.4400000000, 86.7337725688
```

Kopsiku kaitseprisma keskpunkt on `(87,5; 51,4976)`, ringava oma `(139,01; 71,75854943)`. Vastavad raadiused on 35,5001 ja 4,5011 mm. Kasutati 2048-külgseid välispidi lähendeid ja 0,0001 mm kaitsevaru. Ringava torusein taastati baasist.

## Kontrollid ja piirangud

- Taastatud tippude suurim kaugus algsest kolmnurgatasandist: 4.30370869e-06 mm. Uute pindade väljumine kontuurist: 5.82788222e-06 mm. Mõlemad jäid 0,00002 mm float32 pikkustolerantsi sisse; see ei asenda täielikku mahukontrolli.
- Brauseris ei olnud JavaScripti vigu. Töötasid tagantvaade, Wave otsevaade, mõõdud, läbipaistvus, ruudustik ja mobiilipaneelid.
- **Võrk pole veetihe ega ühtlase orientatsiooniga:** 29491 lahtist serva ja 9892 enam kui kahe tahuga serva. Alles on lähtevõrgu vead ja korrastamata lõikeliidesed. Range suletud keha ja lubatud mahu erinevuse kontroll ei ole läbitud; 0,000001 mm³ mahutolerantsi ei suurendatud. Vajalik on edasine topoloogiline parandus.
- Douk T4 Pro paigutus jäi lahendamata: täpne mudel ja kontrollitud gabariitmõõtmed puuduvad; asendusgeomeetriat ei lisatud.

Baas SHA-256: `95e0bd3cc898ec9fad22f41e743da377c7c63b0fca5758989225975b9694373b`

Ülevaatusfail SHA-256: `e5bd600d5724609a1ec1d099714b84b02ac5132dc83ec92b6322b3f94c467bb5`

Arvuline raport: `/workspace/cubie-analysis/review/final_local_check.json`.
