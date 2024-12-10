# Opgave week 7 – netwerksecurity

Deze opgave is speciaal voor de Deeltijd-variant van het vak Security.

## Side-Channel Attack 

### Introductie 

Je probeert in te loggen op een website, waarna je als reactie krijgt dat het wachtwoord niet klopt. Kun je het antwoord van de server gebruiken om het wachtwoord te kraken? 

Ja. Tenminste, als er geen rekening is gehouden met het risico van een timing attack. Een Timing Attack is een vorm van Side-Channel Attack waarbij de responstijd van de server gebruikt wordt om letter voor letter een wachtwoord te kraken. 

Neem als voorbeeld de volgende functie:

```python
def check_password(actual_password, provided_password):
    if len(provided_password) == len(actual_password):
        for i in range(len(provided_password)):
            if provided_password[i] != actual_password[i]:
                return("Incorrect password. Access Denied.")
        return("Password correct. Access Granted.")
    else:
        return("Incorrect password. Access Denied.")
```

De functie gaat karakter voor karakter het gegeven wachtwoord bij langs en kijkt of het overeenkomt met het daadwerkelijke wachtwoord.
Zodra die een verkeerd karakter tegenkomt eindigt de functie en wordt de toegang geweigerd; pas als alle karakters zijn gecheckt wordt de toegang verleend. 

Dit betekent dus dat hoe meer karakters (op een rij, vanaf het eerste karakter) juist zijn, hoe vaker de loop wordt herhaald, en dus hoe langer het duurt voor de functie een antwoord teruggeeft!  

Met deze kennis zouden we kunnen proberen om het wachtwoord te kraken, en dat is ook precies wat we in deze opdracht gaan doen.  

### Opdracht 

Er zal binnen het netwerk een simpele server opgezet worden waar je kunt inloggen met je studentencode en een (voor jullie) onbekend wachtwoord.
De gegevens hiervoor volgen nog, zodra de server draait.
Voor testdoeleinden is het (eerst) ook mogelijk om [met een lokale server te werken](#lokale-server).

Je krijgt cadeau dat het wachtwoord alléén uit kleine letters en cijfers bestaat.
Deze server werkt aan de achterkant praktisch hetzelfde als de bovenstaande functie, en je kunt hem dus ook op dezelfde manier uitbuiten om het wachtwoord te kraken.
Hiervoor maak je gebruik van [het bestand client.py](https://github.com/hanze-hbo-ict/sw_sec_docs/tree/master/src/pract-wk7/client.py) dat al enkele functies bevat om de verbinding tot stand te laten komen: ``client_connect()`` is een backend-functie die de directe koppeling met de server regelt en eventuele errors afvangt. ``call_server()`` maakt daar weer gebruik van, en kun je direct aanroepen in je oplossing. 

NB: gebruik géén andere soorten aanvallen om het wachtwoord te proberen kraken! De server is niet bijzonder robuust en als je hem platgooit heb je zowel jezelf als alle andere studenten ermee. 
De functie ``call_server()`` mag naar wens worden aangepast, maar zorg dat je de regel met ``time.sleep(0.001)`` laat staan; dit zorgt ervoor dat jullie de server niet per ongeluk DDoS’en met zijn allen. Het verbindingsgedrag van de clients wordt overigens bijgehouden.  

Hierna staan de eisen van het lab journal en een stappenplan dat je kunt aanhouden om de opdracht te maken. 
 
#### Stappenplan 

1. Controleer of de functionaliteit van de verbinding: werkt de test-aanroep onderaan de code? 

1. Als de verbinding werkt zul je eerst een manier nodig hebben om te timen hoe lang de server erover doet om een antwoord te sturen. Pas de code aan zodat je voor elke inlogpoging ziet hoe veel tijd er tussen het versturen van de credentials en het ontvangen van het antwoord zit. 

1. Nu je kunt meten hoe lang de server doet over een antwoord kunnen we beginnen met kraken! Stap één is het bepalen van de lengte van het wachtwoord. Schrijf een functie die de responstijd van wachtwoorden van verschillende lengte meet, en deze gebruikt om de juiste lengte te bepalen.
Denk goed na over waar in de code je het tijdsverschil meet.<br>
_Hint: variabele vertraging in het netwerk voegt willekeur toe aan de responstijd._<br>
Wat kun je doen om je metingen betrouwbaarder te maken?<br>
Denk hierbij bv. aan statistische analyse. 

1. Nu je de juiste lengte hebt kun je beginnen met het kraken van het wachtwoord zelf.
Doe dit door eerst een ontwerp te maken met pseudo-code en er met zijn tweeën naar te kijken alvorens je het implementeert.
Doe dit vóórdat je het internet raadpleegt voor hulp!<br>
_Hint: je zult teken voor teken aan de slag moeten gaan!_<br>
NB: het wachtwoord bestaat uit alleen kleine letters en cijfers. Mocht je je aanval willen testen met een gebruiker waarvan het wachtwoord bekend is kun je studentnummer 000000 gebruiken, deze heeft het wachtwoord hunter2. 

#### Lab journal 

Zorg dat je in het “Discussie”-onderdeel de volgende vragen behandelt: 

* Hoe ben je omgegaan met de variabele vertraging van het netwerk? Welke oplossingen heb je geprobeerd die niet werkten, en waarom werkten ze niet? 
* Aansluitend op bovenstaande onderdeel: obstakels die je tijdens het maken van de opgave bent tegengekomen en hoe je ze overkwam.  

Noem in het “Resultaten”-onderdeel ook het “gestolen” wachtwoord van beide studenten (die van de opgave dus – je echte wachtwoorden mag je houden 😉).

* Als je het wachtwoord niet hebt kunnen vinden resulteert dat niet per se een onvoldoende, maar je zult dan wel een erg goede verslaglegging van je ontwerp- en troubleshooting-processen moeten vastleggen, en bij de demonstratie kunnen aantonen dat je goed over alle obstakels hebt nagedacht. 

#### Inleveren 

Voor deze weekopgave lever je de volgender onderdelen in: 

* Jullie versie van het client.py bestand met de code die je hebt gebruikt om de server te kraken, voorzien van eigen commentaar.
* Een .pdf met dezelfde code + commentaar. Dit voor het beoordelen middels Blackboard.
* Een .pdf van de eerste volledige versie van je pseudo-code (als je je pseudo-code schriftelijk hebt gemaakt is een .pdf met/van een foto ook goed).
* Een .pdf van het lab journal.

#### Lokale server 

Als je wil werken aan je code, maar geen toegang hebt tot de server kun je gebruik maken van een lokale versie middels Docker. Zorg dat je Docker geïnstalleerd hebt (en de map met docker.exe hebt toegevoegd aan je PATH), en voer de volgende commando’s uit: 

``docker pull jjmellens/timingattack:latest``

``docker run -d -p 3840:3840 --name timingattack jjmellens/timingattack``

Als het goed is draait er nu een Docker-container met daarop een versie van de server (je kunt het nog even controleren met ``docker ps``).
De server op de docker-container bevat overigens alleen de users 000000 met wachtwoord hunter2. 

NB: de Docker-server draait lokaal op je eigen machine en heeft dus geen last van netwerk-interferentie.
Dat betekent dat een aanval die alleen is getest op de Docker server hoogstwaarschijnlijk niet werkt op de echte server.
Houd hier dus rekening mee en zorg dat je je oplossing ook op locatie test, en host de docker-server bij voorkeur op een ander apparaat dan de machine vanwaar je de aanval uitvoert. 