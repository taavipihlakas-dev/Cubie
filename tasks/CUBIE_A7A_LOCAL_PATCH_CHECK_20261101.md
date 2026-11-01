# Cubie A7A — ebaõnnestunud kohaliku paranduse kontroll, 2026-11-01

**Staatus: töö ei ole valmis ega ülevaatuseks sobiv kandidaat. Uut HTML-i ei avaldatud.**

## Kinnitatud lähtealus
Ainus geomeetriline allikas oli main/Kohutavalt kaua ver.1.html.
SHA-256 kontrolliti nii GitHubist loetud sisul kui kohalikul failil:
661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91
Faili suurus: 5 527 796 baiti. Baasfaili ei muudetud.
Teiste Cubie HTML-, SCAD- ega STL-versioonide geomeetriat ei kasutatud.
Kolm kasutaja märgistatud kuvatõmmist olid kättesaadavad.

## Tegelikult kontrollitud
- Konstruktsiooni baasvõrk: 71 880 kolmnurka, 35 932 erinevat tippu.
- Kõik 107 820 topoloogilist serva kuuluvad täpselt kahele tahule; servade orientatsioonid on kooskõlas.
- Üks kolmnurk on täpselt nullpindalaga; kokku üheksa kolmnurga kahekordne pindala on alla 1e-10 mm². See ei tõesta iseenesest kogu baasi vigasust.
- Märgiga võrgumaht: 215 955,7356433328 mm³.
- Vaaturi Waveshare'i teisendus: Rx 16°, pivot [87.5,89.5,0], Z-nihe +3.5 mm. Kohaliku ringi keskpunkt XY=[87.5,54].
- Konstruktsiooni ringpinna tipud vastavad kohalikele raadiustele 33.5 ja 35.5 mm, lähtematerjali float32 arvulise täpsuse piires.
- Lähima XLR-i vaaturi algasend: [125.6,24.9,5], pööre Z=180°. Teise XLR-i asend: [150.8,24.9,5].
- Esimese ava ja rõnga pinna lõikumist toetavad ühised baasvõrgu piiripunktid. Näiteks globaalne punkt [114.92721558,30.16323471,-0.12788415] on kohalikul rõngaraadiusel umbes 35.4995762 mm ning XLR-i teljest XY-kaugusel 11.89999861 mm. See on geomeetriline lõikepiir, mitte „Lähtesta” vaate optiline mulje.
- Vaaturi olemasolev reset muudab kaamerat, kuid ei peida eraldi osi; olemasolevas koodis initiallyVisible=true.
- OpenCascade'i teisendatud kest läbis kesta kontrolli, kuid sellest tehtud tahke keha isValid() tagastas false. See kontroll puudutab teisendatud keha ega tõesta kõiki baasvõrgu võimalikke vigu.

## Ebaõnnestunud katsed
1. Baas-HTML-i võrk eksporditi muutmata koordinaatidega ajutisse STL-i.
2. OpenSCAD 2021.01 / CGAL: prooviti Ø73 ülemise poolkaare vabastuslõiget ringi kaitsemahuga. CGAL katkestas assertion violation veaga:
   e_below != SHalfedge_handle()
   /usr/include/CGAL/Nef_3/SNC_FM_decorator.h:418.
   Väljund oli tühi; seda ei kasutatud kandidaadina.
3. Blender 4.3.2 EXACT boolean andis lõiketulemuse. Kontroll leidis lisaks kahe tahuga servadele 154 serva, millega oli ühendatud 4–22 tahku; 48 orientatsioonikonflikti ja 168 täpselt nullpindalaga kolmnurka. Tulemus lükati tagasi.
4. Uus katse samas Blenderi töövoos pärast 0.00001 mm lävega tippude ühendamist ning degenereerunud geomeetria puhastamist:
   83 452 kolmnurka; 191 ühe tahuga serva; üks kolme tahuga serv; 12 nelja tahuga serva; 192 orientatsioonikonflikti; kolm nullpindalaga kolmnurka.
   Ka see tulemus lükati tagasi. Numbriline puhastamine ei lahendanud topoloogiat.
5. Chromiumi käivitamine Playwrightiga ebaõnnestus keskkonna süsteemipiirangute tõttu: setsockopt / shutdown Operation not permitted. Brauserikontrolli ei loetud läbituks.
6. GitHubi CLI-võrguühendus ei töötanud vaikimisi sandboxis. Lisavõrguõigust nõudnud paigalduspäringud jäid kasutaja jaoks pikalt ootele ja katkestati; sõltuvuste paigaldamist ei väideta õnnestunuks.
7. Töökeskkond muutus lõpuks unavailable-olekusse.

## Lõpetamata ja kontrollimata
- Ringipõhja lõpliku tasapinna ning lõike täissügavuse kinnitamine. Katses kasutatud kohalik Z15 oli tööparameeter, mitte väljastuseks kinnitatud mõõt.
- Ø73 vabastuslõike nõuetekohane, suletud ja orienteeritud lõppvõrk.
- XLR-ava minimaalne nihutus koos vana ava korrektse taastamise ja pesa samatelgsuse kontrolliga.
- Kõigi nõutud C0.5 faaside tegemine ja servakaupa konfliktide dokumenteerimine.
- Täielik iselõikumiste, pindade pidevuse, normaalide ja lubatud muutmismahust väljapoole jääva geomeetria kontroll.
- Läbipaistvuse, peidetavate osade ja reset-käitumise töötav brauserikontroll.
- Uus iseseisev HTML, selle GitHubi üleslaadimine ja Pagesi avaldamine ning värske veebiversiooni kontroll.

## Väljastusotsus
Ühtegi ebaõnnestunud võrgutulemust ei esitata parandatud mudelina. Varasemad versioonid ja kinnitatud baas säilitati. Pagesi uut versiooni ei avaldatud, sest nõutud geomeetria- ja vaaturikontrollid ei läbinud.
See raport on diagnostika, mitte valminud mudel ega kasutaja heakskiidu taotlus.
