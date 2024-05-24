# Opgave week 5: privacy threat modelling van een slimme spiegel

We gaan deze week bezig met het bepalen van privacyrisico’s van een voorbeeldcasus aan de hand van de LINDDUN-methode. 

## Casus

Een start-up heeft een nieuw platform ontwikkeld dat gebruikers in staat stelt om een slimme spiegel in hun woning te installeren. De slimme spiegel heeft een ingebouwde camera, inclusief motion-detection en eye-tracking. De spiegel fungeert ook als een scherm dat gebruikers kan voorzien van gepersonaliseerde fitnessinstructies, weerberichten, kledingadviezen en andere nuttige informatie tijdens het gebruik. In het scherm is tevens een touchscreen ingebouwd, zodat een gebruiker bij het eerste gebruik zijn naam kan opgeven en fitnessoefeningen kan uitkiezen. De spiegel staat in verbinding met de cloudomgeving van de leverancier.

De camera in de spiegel kan worden gebruikt voor gezichtsherkenning, zodat de spiegel automatisch de fitnessprogramma's kan aanpassen op basis van de gebruiker die ervoor staat. De informatie over de lichaamsbouw en het fitnessgedrag van de gebruiker, zoals trainingsduur en intensiteit, wordt opgeslagen op de servers van het bedrijf.

Naast de fitnessinformatie slaat het bedrijf ook gegevens op over het kijkgedrag van de gebruikers voor advertentiedoeleinden (via eye-tracking door de camera). Deze gegevens worden gebruikt om gerichte advertenties aan te bieden.

Om het platform verder te financieren, biedt het bedrijf een premium abonnement aan waarvoor gebruikers maandelijks betalen. Dit abonnement geeft toegang tot geavanceerde fitnessprogramma's, uitgebreide weer- en verkeersinformatie en exclusieve kledingadviezen; dit alles zonder reclame.

Het platform heeft een functie waarmee gebruikers hun slimme spiegel kunnen delen op sociale media. Via deze functie, die standaard aan staat, kunnen vrienden en volgers live meekijken met hun fitness-sessies.

Om het platform verder te verbeteren, overweegt het bedrijf samenwerkingen met zorgverzekeraars, waarbij gebruikers gezondheidsgegevens delen in ruil voor korting op hun premie. Het idee hierachter is om met Machine Learning eventuele achteruitgang in gezondheid eerder te kunnen detecteren, om zo door preventie kosten te kunnen besparen.

## Opdrachten

1.\ Teken het Data Flow Diagram van de beschreven casus. Tip: nummer de interfaces en data stores, zodat je er bij 2 en 3 gemakkelijk naar kunt verwijzen.

2.\ Definieer welke privacyrisico’s er **per interface** (plekken waar data over een trust boundary gaat) én **per data store** in de DFD aanwezig zijn. Maak hierbij gebruik van de LINDDUN-afkorting om de types risico’s aan te geven in de DFD: 
    * <b>L</b>inkability: data aan elkaar koppelen.
    * <b>I</b>dentifiability: subject identificeren op basis van data.
    * <b>N</b>on-repudiation: opgeslagen data niet kunnen aanpassen of verwijderen.
    * <b>D</b>etectability: kunnen vaststellen dát er data is over een subject.
    * <b>D</b>isclosure of information: data wordt ongevraagd openbaar.
    * <b>U</b>nawareness: data wordt verwerkt zonder dat het subject het weet.
    * <b>N</b>on-compliance: data wordt niet conform de wet- en regelgeving verwerkt.

3.\ Geef per interface en data store minstens één concreet aanvalsscenario waarin één of meer van de door jou gekozen LINDDUN-letters terugkomen. Hierbij komt kijken:

* Wat voor privacygevoelige informatie er over de interface gaat of in de data store staat.
* Wat voor probleem het is als deze informatie uitlekt, voor de verschillende stakeholders (denk aan de gebruiker, de leverancier, eventuele huisgenoten van de gebruiker, zorgverzekeraars).

4.\ Maak nu een lijst van de interfaces, gesorteerd op prioriteit, dus de in jouw optiek meest kwetsbare bovenaan. Onderbouw je keuze!

5.\ Bedenk voor de top 3 van kwetsbare interfaces zo veel mogelijk maatregelen om de gevonden risico’s te verminderen.

*Tip: je kunt 2 t/m 5 grotendeels in één keer maken door gebruik te maken een tabel met kolommen voor de interfaces en data stores, de LINDDUN-letters, de scenario's (incl. type data en stakeholders), de prioriteiten en de tegenmaatregelen, en deze te sorteren op prioriteit. Zie bijvoorbeeld de Excel-sheet die op Blackboard staat. Denk er wel om dat je de **onderbouwing** van je prioritering erbij vermeldt!*