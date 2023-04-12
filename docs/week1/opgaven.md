# Opgaven week 1: fuzzing

## Opgave 1: Wachtwoord-fuzzing met Hydra

Deze opdracht kan op Linux, Mac en Windows (WSL) worden uitgevoerd.

### Hydra installeren

**Windows-gebruikers** moeten eerst het [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL) installeren. De standaard-distributie, Ubuntu, is prima. Na installatie beschik je over een Linux-prompt en kun je onderstaande opdrachten uitvoeren (en nog veel meer). Bovendien heb je een WSL-installatie nodig om Docker, waar we volgende week mee bezig gaan, te kunnen draaien.

Lees [hier](https://www.howtogeek.com/426749/how-to-access-your-linux-wsl-files-in-windows-10/) hoe je bestanden van en naar je Linux-omgeving kunt kopiëren.

[Hydra](https://github.com/vanhauser-thc/thc-hydra) is een tool om wachtwoorden mee te brute-forcen, wat ook een vorm van fuzzing is.

We beginnen met de installatie van Hydra. Ga naar een geschikte map (maak bijv. een map "software-security" aan in je homedir) en voer één voor één de volgende commmando's uit:
```
git clone https://github.com/vanhauser-thc/thc-hydra.git hydra
cd hydra
./configure
make
make install
```

### Hydra draaien op een webapp

Voorbeeld-commando op een lokale Flask-webapp (poort 5000, met [CSRF-controle](https://www.geeksforgeeks.org/csrf-protection-in-flask/) uitgezet door ``app.config['WTF_CSRF_CHECK_DEFAULT'] = False`` in de code op te nemen). Hydra probeert hier voor gebruiker "henk" alle wachtwoorden met 4 cijfers. Bestudeer de [documentatie van Hydra](https://github.com/vanhauser-thc/thc-hydra) om te leren hoe de -x-optie en de andere parameters precies werken.

``hydra -l henk -x 4:4:1 127.0.0.1 http-post-form -s 5000 "/login:username=henk&password=^PASS^:Inlog niet correct"``

Let op: ondanks dat het misschien op meerdere regels wordt weergegeven, is bovenstaande één commmando dat op één regel dient te worden uitgevoerd!

### De opdracht

Je gaat je eigen Webtech- of IOT-applicatie uit de vorige periode brute-forcen! Maak een gebruiker aan met een simpel wachtwoord, bijvoorbeeld bestaande uit 3 cijfers, en kijk hoelang Hydra erover doet om het te kraken. Maak nu het wachtwoord stapsgewijs complexer door meer cijfers en eventueel letters en leestekens (pas dan wel je -x-parameter aan) toe te voegen, en noteer steeds hoelang Hydra erover doet. Welke wachtwoord-complexiteit vind jij veilig genoeg? Schaalt dit naar een echte productie-applicatie of gelden er dan toch nog strengere eisen, en waarom?

Lever een kort verslagje in over deze "penetration test" (pentest), inclusief tijdmetingen en conclusies. (50%)

## Opgave 2: Fuzzing met Radamsa

Radamsa is beschikbaar voor Linux, Apple en Windows (via WSL). De broncode is te vinden op [Gitlab](https://gitlab.com/akihe/radamsa). De [documentatie](https://gitlab.com/akihe/radamsa/-/blob/develop/README.md) is daar ook te vinden.

Download en installeer de software. De volgende commando’s kunnen hiervoor op Linux, Apple of WSL één voor één uitgevoerd worden via de terminal. Mochten git, gcc en/of make nog niet geïnstalleerd zijn installeer deze dan eerst via je package manager (bijvoorbeeld Ubuntu Linux of WSL: ``sudo apt-get install git gcc make``).

```
git clone https://gitlab.com/akihe/radamsa.git radamsa
cd radamsa
make
make install
```

Kijk of radamsa goed werkt door te typen: ``radamsa --help``
of: ``echo "Dit is een teststring" | radamsa``

### Voorbeeld 1
Hier een kort voorbeeld hoe een radamsa-aanroep werkt.

Blijf in de map waar je zojuist radamsa hebt geinstalleerd en maak hier een nieuwe map: examples. Plaats in deze map een .txt-bestand met een korte tekst.Voer radamsa een aantal keren uit voor het bestand, bijvoorbeeld: ``radamsa examples/hello.txt``

Elke keer als radamsa wordt uitgevoerd wordt er een nieuwe fuzz-actie gedaan en het resultaat getoond.

### Voorbeeld 2
Met Radamsa kun je meerdere fuzz-cases achter elkaar laten maken en de uitvoer per case opslaan. Het volgende voorbeeld laat dit zien.

Maak eerst een nieuwe submap aan in de radamsa-map: fuzz-cases.

Ga terug naar de map examples en maak een nieuw bestand aan, bijvoorbeeld een python-bestand, html of xml.

Gebruik -n voor het aantal varianten dat je wilt genereren door radamsa en geef daarnaast met -o het pad naar fuzz-cases op. Het commando ziet er dan zo uit: ``radamsa -n 10 -o 'fuzz-cases/hello-%n.%s' examples/hello.txt``
Ga naar de map fuzz-cases en bekijk hier de gefuzzde bestanden.

### De opdracht
a. Leer radamsa kennen. Ga er mee aan de slag en kijk wat het doet. Raadpleeg hiervoor ook aanvullende informatie op internet en ga in overleg met klasgenoten.

b. Kies een aantal bronnen om de fuzzer op toe te passen (minimaal 3). Radamsa kun je toepassen op tekstbestanden, afbeeldingen, codefragmenten etc.  

c. Pas radamsa toe en analyseer het resultaat. Wat gebeurt er als je gefuzzde bestanden probeert uit te voeren of te laten openen door de applicatie waarmee je ze normaal opent?

Lever een kort verslagje in over deze "fuzz test". Welke bronnen heb je gekozen en waarom? Beschrijf wat je opvalt: wat voor data wordt er gegenereerd en wat is het effect van deze data? (50%)