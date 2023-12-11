# Opgave week 5: privacy threat modelling van een ruggenmergstimulator

We gaan deze week bezig met het bepalen van privacyrisico’s van een voorbeeldcasus aan de hand van de LINDDUN-methode. 

## Casus

Een patiënt met chronische rugpijn ondergaat een operatie waarbij een implantaat wordt geplaatst bij het ruggenmerg. Het stimulatorapparaat is ontworpen om elektrische impulsen naar het ruggenmerg te sturen, wat verlichting van pijn biedt aan de patiënt.

Na een periode in het ziekenhuis krijgt de patiënt een ontvanger mee naar huis, die naast het bed geïnstalleerd wordt om verdere monitoring vanuit het ziekenhuis mogelijk te maken. De stimulator stuurt draadloos zijn activiteitsgegevens naar deze ontvanger via RF / MICS (Medical Implant Communication Service) technologie. De ontvanger slaat deze gegevens op in zijn interne geheugen en stuurt deze elk uur door naar een server in het ziekenhuis via het WiFi-netwerk en het HTTP-protocol.

De server slaat deze gegevens op in een standaard MySQL-database, die toegankelijk is voor de behandelend arts van de patiënt via een desktopcomputer in het ziekenhuis. De arts gebruikt deze gegevens om de voortgang van de patiënt te bewaken.

Tijdens follow-up afspraken in het ziekenhuis kan de arts de ruggenmergstimulator opnieuw programmeren met behulp van een RF-module die aan de computer van de arts verbonden is. Het herprogrammeringsproces stelt de arts in staat om de instellingen van het apparaat aan te passen, zoals de frequentie en intensiteit van de elektrische impulsen, om de pijnverlichting van de patiënt te optimaliseren.

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

*Tip: je kunt 2, 3A, B en C in één keer maken door gebruik te maken een tabel met kolommen voor de interfaces / data stores, de LINDDUN-letters, de scenario's, de stakeholders, de prioriteiten en de tegenmaatregelen. Zie bijvoorbeeld de Excel-sheet die op Blackboard staat. Denk er wel om dat je de **onderbouwing** van je prioritering erbij vermeldt!*