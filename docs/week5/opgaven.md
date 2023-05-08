# Opgave week 5: privacy threat modelling van een ruggenmergstimulator

We gaan deze week bezig met het bepalen van privacyrisico’s van een voorbeeldcasus aan de hand van de LINDUNN-methode. 

## Casus

Een patiënt met chronische pijn ondergaat een operatie waarbij een implantaat wordt geplaatst bij de ruggenmerg. Het stimulatorapparaat is ontworpen om elektrische impulsen naar het ruggenmerg te sturen, wat verlichting van pijn biedt aan de patiënt.

Als onderdeel van de post-implantatie monitoring stuurt het apparaat draadloos zijn activiteitsgegevens naar een ontvanger bij het bed via RF / MICS (Medical Implant Communication Service) technologie. De ontvanger slaat deze gegevens op in zijn interne geheugen en stuurt deze elk uur door naar een server in het ziekenhuis via het WiFi-netwerk en het HTTP-protocol.

De server slaat deze gegevens op in een standaard MySQL-database, die toegankelijk is voor de behandelend arts van de patiënt via een desktopcomputer in het ziekenhuis. De arts gebruikt deze gegevens om de voortgang van de patiënt te bewaken.

Na een periode in het ziekenhuis krijgt de patiënt de ontvanger mee naar huis en wordt het daar naast het bed geïnstalleerd om verdere monitoring vanuit het ziekenhuis mogelijk te maken.

Tijdens follow-up afspraken in het ziekenhuis kan de arts de ruggenmergstimulator opnieuw programmeren met behulp van een laptop die is aangesloten op een USB RF-module. Het herprogrammeringsproces stelt de arts in staat om de instellingen van het apparaat aan te passen, zoals het aanpassen van de frequentie en intensiteit van de elektrische impulsen, om de pijnverlichting van de patiënt te optimaliseren.

## Opdrachten

1.\ Teken het Data Flow Diagram van de beschreven casus. 

2.\ Definieer welke privacyrisico’s er per interface (plekken waar data over een trust boundary gaat) in de DFD aanwezig zijn. Hierbij komt kijken:

- Wat voor privacygevoelige informatie er over de interface gaat
- Wat voor probleem het is als deze informatie uitlekt, voor de verschillende stakeholders (bijv. patiënt, systeemverkoper, ziekenhuis)
- Waar mogelijk gebruik maken van de LINDDUN-afkorting om de types risico’s aan te geven in de DFD: 
Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness en Non-compliance. *Tip: maak een tabel met interfaces vs. de genoemde LINDUNN-categorieën.*

3.\ Bepaal wat de risicoscenario’s zijn.

4.\ Prioriteer deze risico’s en onderbouw deze prioritering ook.

5.\ Bedenk zo veel mogelijke maatregelen om deze risico’s te verminderen.