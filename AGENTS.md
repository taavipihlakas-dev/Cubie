# Cubie A7A tööreeglid

Need on kasutaja püsivad projektijuhised. Rakenda neid iga Cubie A7A muudatuse ja väljundi puhul.

1. Salvesta iga HTML-i muudatus uude eraldi terviklikku HTML-faili kasvava versiooninumbriga. Kontrolli olemasolevaid versioone ja vali seni kasutamata nimi.
2. Säilita kõik eelmised versioonid ja kasutaja kinnitatud baas muutmata. Praegu kinnitatud baas on `Cubie_v48_32_3D.html`; v48.33 on kinnitamata ülevaatuskandidaat. Uut kandidaati ei tohi vaikimisi baasiks võtta.
3. Salvesta uus HTML-versioon GitHubi hoidlasse `taavipihlakas-dev/Cubie`: tee vastava faili commit ja push. Ainult ajutisse töökausta salvestamine ei lõpeta väljastamist. Säilita kasutaja muud failid ja muudatused; ära lisa commit'i ülesandega mitteseotud muudatusi.
4. Anna pärast iga muudatust vastuses kohe uus klikitav GitHubi faililink, mille kaudu kasutaja saab HTML-faili alla laadida. Lisa lühike tegelike muudatuste kokkuvõte ja kontrollide tulemus. Faililingi kuju on `https://github.com/taavipihlakas-dev/Cubie/blob/<tegelik-kaugharu>/<failinimi>`; soovi korral lisa samale failile ka GitHubi otsene allalaadimislink. Erista allalaadimist interaktiivsest brauserieelvaatest.
5. Ära paku ega kasuta väljundi edastamiseks veebimajutust, veebiserverit või täiendavaid teenuseid. Ära loo avaldamisharusid ega Pagesi saiti. GitHubi hoidla on failide salvestamise ja allalaadimise koht.
6. Ära muuda HTML-i sisu allalaadimise võimaldamiseks. Vaatur peab jääma terviklikuks iseseisvaks interaktiivseks WebGL-vaaturiks; kõik vajalikud andmed peavad olema HTML-is. Sihtbrauserid on Windowsi brauserid ja Samsung Internet. Erista tegelikult testitud platvorme platvormidest, mille testimiseks ligipääs puudub.
7. Enne lingi esitamist kontrolli, et push õnnestus, tegeliku GitHubi kaugharu viide sisaldab loodud commit'i ning selles commit'is on oodatud HTML-fail õige sisuga. Pelk kohalik commit ei tõenda GitHubi salvestamist. Kui salvestamine ebaõnnestub, teata konkreetsest takistusest ja ära väida, et uus versioon on GitHubis olemas.
8. Kasuta lingis tegelikku GitHubi kaugharu nime, kuhu fail salvestati. Kui fail asub tööharus, viita sellele tööharule, mitte automaatselt `main`-harule. Kontrolli kasutatud kaugharu viidet; ära tuleta kaugharu nime üksnes kohaliku haru nimest.

Kontrolli iga muudatuse puhul kinnitatud baasi vastu, et muud osad, teiste detailide geomeetria ja vaaturi funktsioonid on säilinud. Fikseeri enne ja pärast baasi SHA-256. Erista kontrollitud omadusi, ebaõnnestunud kontrolle ja kontrollimata omadusi; ära esita vigast kandidaati kinnitatud lõppversioonina.

Olemasoleva faili muutmata väljastamise katse ei vaja uut versiooninumbrit. Kontrolli selle katse puhul sisu ja SHA-256 muutumatust.

Üksnes tööjuhiste või dokumentatsiooni muutmine ei nõua uue HTML-versiooni loomist. Püsivad projektijuhised salvesta samuti Cubie GitHubi hoidlasse ja kontrolli nende salvestumist.
