# Opgaven week 1: fuzzing

## Opgave 1: Wachtwoord-fuzzing met Hydra

Deze opdracht kan op Linux, Mac en Windows (WSL) worden uitgevoerd.

[Hydra](https://github.com/vanhauser-thc/thc-hydra) is een tool om wachtwoorden mee te brute-forcen, wat ook een vorm van fuzzing is.

### Hydra installeren (1 - voor Windows)

Windows-gebruikers moeten eerst het [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL) installeren. De standaard-distributie, Ubuntu, is prima. Na installatie beschik je over een Linux-prompt en kun je onderstaande opdrachten uitvoeren (en nog veel meer - zo heb je WSL nodig om Docker, waar we volgende week mee bezig gaan, te kunnen draaien). [Wargames van Over the Wire](https://overthewire.org/wargames/) is een web-app waar je interactief veel over het gebruiken van verschillende Linuxtools kunt leren. Een must voor ICT'ers. Advies is om te beginnen met de Bandit-wargame. Lees [hier](https://www.howtogeek.com/426749/how-to-access-your-linux-wsl-files-in-windows-10/) hoe je bestanden van en naar je Linux-omgeving kunt kopiëren.

### Hydra installeren (2)

We beginnen nu met de installatie van Hydra. Ga naar een geschikte map (maak bijv. een map "software-security" aan in je homedir) en voer één voor één de volgende commmando's uit:
```
git clone https://github.com/vanhauser-thc/thc-hydra.git hydra
cd hydra
./configure
sudo make
sudo make install
```

### Mogelijke problemen en oplossingen bij de Hydra-installatie
Mochten git, gcc en/of make nog niet geïnstalleerd zijn, installeer deze dan eerst via je package manager (bijvoorbeeld Ubuntu Linux of WSL: ``sudo apt-get install git gcc make``).

Het kan soms helpen om allereerst de package-manager zelf te updaten: ``sudo apt-get update``

Mocht je tijdens het draaien van Hydra de melding krijgen dat bepaalde opties niet beschikbaar zijn, dan kan het helpen om vóór de installatie een aantal extra pakketten te installeren: ``sudo apt-get install libssl-dev libssh-dev libidn11-dev libpcre3-dev libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev``

Mocht je tijdens het clonen van de Github-repository de foutmelding "Unable to resolve github.com in WSL" krijgen, dan de volgende stappen doorlopen om de default nameserver aan te passen:

* ``sudo nano /etc/resolv.conf``
* comment originele nameserver uit (met #)
* Toevoegen:
```
nameserver 8.8.8.8
nameserver 8.8.4.4
```
* Opnieuw proberen, of bijv. eerst 'ping google.com'

### Hydra draaien op een webapp

Voorbeeld-commando op het login-formulier van een lokale Flask-webapp, draaiend op poort 5000. Hydra probeert hier voor gebruiker (email) "henk@hanze.nl" alle wachtwoorden met 4 cijfers. Bestudeer de [documentatie van Hydra](https://github.com/vanhauser-thc/thc-hydra) om te leren hoe de -x-optie en de andere parameters precies werken.

``hydra -l henk@hanze.nl -x 4:4:1 127.0.0.1 -s 5000 http-post-form "/login:email=^USER^&password=^PASS^:Inlog niet correct"``

Let op: ondanks dat het misschien op meerdere regels wordt weergegeven, is bovenstaande één commmando dat op één regel dient te worden uitgevoerd!

Om dit werkend te krijgen, zijn er enkele aandachtspunten:

* Zet de [CSRF-controle](https://www.geeksforgeeks.org/csrf-protection-in-flask/) uit door ``app.config['WTF_CSRF_ENABLED'] = False`` in je code op te nemen, op de plek waar je ook de andere configuratie, zoals de ``SECRET_KEY``, instelt.
* Zorg dat bij een incorrecte inlog de tekst "Inlog niet correct" (of anders - maar pas dan je Hydra-aanroep aan) in beeld komt, zodat Hydra weet wanneer een login-poging mislukt is.
* Windows-gebruikers moeten de webapp draaien vanuit hun WSL/Linux-console, dus **niet** vanuit de Windows-omgeving, anders kan Hydra er niet bij. Zo'n aanroep ziet er dan bijvoorbeeld zo uit: ``user@LAPTOP:/mnt/c/Users/user/swsec/wc-wk1$ python3 app.py``

### De opdracht

Je gaat je eigen Webtech- of IOT-applicatie uit de vorige periode<sup>*</sup> brute-forcen! Maak een gebruiker aan met een simpel wachtwoord, bijvoorbeeld bestaande uit 3 cijfers, en kijk hoelang Hydra erover doet om het te kraken. Maak nu het wachtwoord stapsgewijs complexer door meer cijfers en eventueel letters en leestekens (pas dan wel je -x-parameter aan) toe te voegen, en noteer steeds hoelang Hydra erover doet. Welke wachtwoord-complexiteit vind jij veilig genoeg? Schaalt dit naar een echte productie-applicatie of gelden er dan toch nog strengere eisen, en waarom?

Benoem daarnaast drie mogelijkheden om dit soort brute-force-aanvallen tegen te gaan.

Lever een kort verslagje in over deze "penetration test" (pentest), inclusief screenshots van je Hydra-aanroeptijden, metingen, conclusies en tegenmaatregelen. (50%)

<sup>*</sup> Geen webapp (meer) paraat? [Hier](https://github.com/hanze-hbo-ict/sw_sec_docs/tree/master/src/wc-wk1) kun je er eentje vinden die je ook mag gebruiken.

## Opgave 2: Fuzzing met Radamsa

Radamsa is beschikbaar voor Linux, Apple en Windows (via WSL). De broncode is te vinden op [Gitlab](https://gitlab.com/akihe/radamsa). De [documentatie](https://gitlab.com/akihe/radamsa/-/blob/develop/README.md) is daar ook te vinden.

Download en installeer de software. De volgende commando’s kunnen hiervoor op Linux, Apple of WSL één voor één uitgevoerd worden via de terminal. Mochten git, gcc en/of make nog niet geïnstalleerd zijn, installeer deze dan eerst via je package manager (bijvoorbeeld Ubuntu Linux of WSL: ``sudo apt-get install git gcc make``).

```
git clone https://gitlab.com/akihe/radamsa.git radamsa
cd radamsa
sudo make
sudo make install
```

Kijk of radamsa goed werkt door te typen: ``radamsa --help`` of: ``echo "Dit is een teststring" | radamsa``

### Voorbeeld 1
Hier een kort voorbeeld hoe een radamsa-aanroep werkt.

Blijf in de map waar je zojuist radamsa hebt geinstalleerd en maak hier een nieuwe map: examples. Plaats in deze map een .txt-bestand met een korte tekst. Voer radamsa een aantal keren uit voor het bestand, bijvoorbeeld: ``radamsa examples/hello.txt``

Elke keer als radamsa wordt uitgevoerd wordt er een nieuwe fuzz-actie gedaan en wordt het resultaat in de terminal getoond.

### Voorbeeld 2
Met Radamsa kun je meerdere fuzz-cases achter elkaar laten maken en de uitvoer per case opslaan. Het volgende voorbeeld laat dit zien.

Maak eerst een nieuwe submap aan in de radamsa-map: fuzz-cases. Ga dan terug naar de map examples en maak een nieuw bestand aan, bijvoorbeeld een python-bestand, html of xml.

Gebruik -n voor het aantal varianten dat je wilt genereren door radamsa en geef daarnaast met -o het pad naar fuzz-cases op. Het commando ziet er dan zo uit: ``radamsa -n 10 -o 'fuzz-cases/hello-%n.%s' examples/hello.txt``
Ga naar de map fuzz-cases en bekijk hier de gefuzzde bestanden.

### De opdracht
a. Leer radamsa kennen. Ga er mee aan de slag en kijk wat het doet. Raadpleeg hiervoor ook aanvullende informatie op internet en ga in overleg met klasgenoten.

b. Kies een aantal bronnen om de fuzzer op toe te passen (minimaal 3). Radamsa kun je toepassen op tekstbestanden, afbeeldingen, codefragmenten etc.  

c. Pas radamsa toe en analyseer het resultaat. Wat gebeurt er als je gefuzzde bestanden probeert uit te voeren of te laten openen door de applicatie waarmee je ze normaal opent? Kan dit kwaad en/of kan hier misbruik van gemaakt worden?

Lever een kort verslagje in over deze "fuzz test". Welke bronnen heb je gekozen en waarom? Beschrijf en laat d.m.v. screenshots zien wat je opvalt: wat voor data wordt er gegenereerd en wat is het effect van deze data? (50%)

De beide verslagjes mogen worden samengevoegd in één document en als doc(x) of pdf worden ingeleverd via het Inleverpunt.
