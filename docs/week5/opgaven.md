# Opgave week 5: privacy threat modelling van een slimme spiegel

We gaan deze week bezig met het bepalen van privacyrisico’s van een voorbeeldcasus aan de hand van de LINDDUN-methode. 

## Casus

Een start-up heeft een nieuw platform ontwikkeld dat gebruikers in staat stelt om een slimme spiegel in hun woning te installeren. De slimme spiegel heeft een ingebouwde camera en sensoren om gebruikers te voorzien van gepersonaliseerde fitnessinstructies, weerberichten, kledingadviezen, en andere nuttige informatie tijdens het gebruik. De spiegel is verbonden met een mobiele app en een webinterface voor gebruikersbeheer.

De camera in de spiegel kan worden gebruikt voor gezichtsherkenning, zodat de spiegel automatisch de fitnessprogramma's kan aanpassen op basis van de gebruiker die ervoor staat. De informatie over het fitnessgedrag van de gebruiker, zoals trainingsduur en hartslag, wordt opgeslagen op de servers van het bedrijf en is toegankelijk via de mobiele app en de webinterface.

Naast de fitnessinformatie slaat het bedrijf ook gegevens op over het kijkgedrag van gebruikers voor advertentiedoeleinden. Deze gegevens worden gebruikt om gerichte advertenties aan te bieden via de mobiele app.

Om het platform verder te financieren, biedt het bedrijf een premium abonnement aan waarvoor gebruikers maandelijks betalen. Dit abonnement geeft toegang tot geavanceerde fitnessprogramma's, uitgebreide weer- en verkeersinformatie en exclusieve kledingadviezen.

Het platform heeft een functie waarmee gebruikers hun slimme spiegel kunnen delen op sociale media. Via deze functie, die standaard aan staat, kunnen vrienden en volgers live meekijken met hun fitness-sessies via de mobiele app.

Om het platform verder te verbeteren, overweegt het bedrijf samenwerkingen met zorgverzekeraars, waarbij gebruikers gezondheidsgegevens delen in ruil voor korting op hun premie.

## Opdrachten

1.\ Teken het Data Flow Diagram van de beschreven casus. 

2.\ Definieer welke privacyrisico’s er **per interface** (plekken waar data over een trust boundary gaat) én **per data store** in de DFD aanwezig zijn. Hierbij komt kijken:

* Wat voor privacygevoelige informatie er over de interface gaat of in de data store staat
* Wat voor probleem het is als deze informatie uitlekt, voor de verschillende stakeholders (bijv. patiënt, systeemverkoper, ziekenhuis)
* Waar mogelijk gebruik maken van de LINDDUN-afkorting om de types risico’s aan te geven in de DFD: 
    * <b>L</b>inkability: data aan elkaar koppelen
    * <b>I</b>dentifiability: subject identificeren op basis van data
    * <b>N</b>on-repudiation: opgeslagen data niet kunnen aanpassen of verwijderen
    * <b>D</b>etectability: kunnen vaststellen dát er data is over een subject
    * <b>D</b>isclosure of information: data openbaar maken
    * <b>U</b>nawareness: data wordt verwerkt zonder dat het subject het weet
    * <b>N</b>on-compliance: data wordt niet conform de wet- en regelgeving verwerkt

3.\ 

A. Bepaal wat de risicoscenario’s zijn.

B. Prioriteer deze risico’s en onderbouw deze prioritering ook.

C. Bedenk zo veel mogelijke maatregelen om deze risico’s te verminderen.

*Tip: je kunt 2, 3A, B en C in één keer maken door gebruik te maken één of meer tabellen met kolommen voor de interfaces / data stores, de LINDDUN-letters, de scenario's, de stakeholders, de prioriteiten en de tegenmaatregelen. Zie bijvoorbeeld de Excel-sheet die op Blackboard staat. Denk er wel om dat je de **onderbouwing** van je prioritering erbij vermeldt!*