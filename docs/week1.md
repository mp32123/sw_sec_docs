# Opgaven week 1

## 1: Wachtwoord-fuzzing met Hydra

Kan op Linux, Mac en Windows (WSL)

Windows-gebruikers moeten eerst het Windows Subsystem for Linux installeren (wat sowieso een goed idee is); zie https://learn.microsoft.com/en-us/windows/wsl/install

Hydra-repo: https://github.com/vanhauser-thc/thc-hydra

Commando's om te installeren:
```
git clone https://github.com/vanhauser-thc/thc-hydra.git
cd thc-hydra
./configure
make
make install
```

### Hydra draaien op een webapp

Voorbeeld-commando op een lokale Flask-webapp (poort 5000, met CSRF-controle uitgezet). Hydra probeert hier alle wachtwoorden met 4 cijfers.
Bestudeer de documentatie van Hydra om te leren hoe de -x-optie en de andere parameters precies werken.

``hydra -l t.e.roos@pl.hanze.nl -x 4:4:1 127.0.0.1 http-post-form -s 5000 "/login:email=t.e.roos@pl.hanze.nl&password=^PASS^:Inlog niet correct"``

## 2: Fuzzing met Radamsa

Radamsa is beschikbaar voor Linux, Apple en Windows (via WSL). De broncode is te vinden op gitlab: https://gitlab.com/akihe/radamsa
Documentatie is daar ook te vinden: https://gitlab.com/akihe/radamsa/-/blob/develop/README.md
Download en installeer de software: 
De volgende commando’s kunnen hiervoor op Linux, Apple of WSL uitgevoerd worden via de terminal:
Mochten git, gcc en/of make nog niet geïnstalleerd zijn installeer deze dan eerst via je package manager (bijvoorbeeld: apt-get install git gcc make)

```
git clone https://gitlab.com/akihe/radamsa.git radamsa
cd radamsa
make
make install
```

kijk of radamsa goed werkt door te typen: ``radamsa --help``
of: ``echo "Dit is een teststring" | radamsa``

Voorbeeld 1
Hier een kort voorbeeld hoe een Radamsa-aanroep werkt.
Ga terug naar de folder die je hebt aangemaakt en waar je zojuist Radamsa hebt geinstalleerd.
Maak hier een nieuwe map: examples
Plaats in deze map een .txt bestand met een korte tekst.
Voer radamsa een aantal keren uit voor het bestand, bijvoorbeeld: ``radamsa examples/hello.txt``
Elke keer als radamsa wordt uitgevoerd wordt er een nieuwe fuzzer uitgevoerd en het resultaat getoond.

Voorbeeld 2
Met Radamsa kun je meerdere fuzz-cases achter elkaar laten maken en de uitvoer per case opslaan. Het volgende voorbeeld laat dit zien.
Maak een nieuwe folder fuzz-cases
Maak in examples een nieuw bestand aan, bijvoorbeeld een python bestand, html of xml.
Gebruik -n voor het aantal varianten dat je wilt genereren door Radamsa en geef daarnaast met -o het pad naar fuzz-cases op
Het commando ziet er dan zo uit:  radamsa -n 10 -o 'fuzz-cases/hello-%n.%s' examples/hello.txt
Ga naar de fuzz-cases folder en bekijk hier de gegenereerde fuzz-cases