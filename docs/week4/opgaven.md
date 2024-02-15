# Opgave week 4: threat modelling van een slimme koelkast

We gaan deze week bezig met het bepalen van risico’s van een geheel systeem in een voorbeeldcasus aan de hand van de STRIDE-methode. 

## Casus

Een bedrijf heeft een nieuwe slimme koelkast ontwikkeld die is verbonden met het internet. Het bedrijf heeft je de volgende informatie verstrekt (vul waar nodig aan op een fantasievolle maar logische manier).

De koelkast heeft een touchscreen-interface waarmee gebruikers hun boodschappenlijstjes kunnen beheren, receptsuggesties kunnen ontvangen en de temperatuur van de koelkast kunnen regelen. De koelkast is verbonden met het WiFi-netwerk. Er is een mobiele app en een webinterface (via HTTP) om op afstand toegang te bieden tot de functies. Op de koelkast zit bij aankoop een zegel-sticker met daarop een nummer (bestaande uit 25 willekeurige cijfers), waarmee je een account kunt maken op de webinterface.

Naast het touchscreen heeft de koelkast ook spraakherkenningssoftware, zodat gebruikers gesproken commando's kunnen geven om bijvoorbeeld de temperatuur aan te passen of om herinneringen in te stellen. De microfoon en de spraakherkenningsfunctie zijn standaard ingeschakeld, maar gebruikers kunnen deze handmatig uitschakelen via de instellingen.

De koelkast is ontworpen om automatisch bij te houden welke producten erin liggen en hun vervaldatums. Het systeem kan gebruikers waarschuwen wanneer producten dreigen te bederven. Deze informatie wordt opgeslagen in de cloud en is toegankelijk via de mobiele app en webinterface.

Om het abonnementssysteem mogelijk te maken, betalen gebruikers maandelijks een vergoeding voor de toegang tot de extra functies. Het bedrijf biedt ook klantenondersteuning en onderhoudsdiensten aan als onderdeel van het abonnement. De klantgegevens die worden gebruikt voor facturering staan in een database en zijn toegankelijk voor de factureringsafdeling via TCP over een intern netwerk. De facturen worden via e-mail naar de klanten verzonden.

De koelkast heeft ook een USB-poort voor software-updates en onderhoudsdoeleinden. Tijdens onderhoud kunnen gecertificeerde monteurs het onderhoudsgedeelte, waar de USB-poort onderdeel van is, openen met een specifieke sleutel.

Het bedrijf heeft ook plannen om samen te werken met supermarkten om automatisch boodschappenlijstjes te genereren op basis van de inhoud van de koelkast. Hierbij wordt informatie gedeeld tussen de slimme koelkast en de supermarkt-apps.

## Opdrachten

1.\ Teken het Data Flow Diagram (DFD) van de beschreven casus. Het diagram moet het systeem op een niveau laten zien dat geschikt is voor een risicoanalyse. Zorg dat de DFD overzichtelijk en navolgbaar neergezet wordt. Dit kan op papier, maar mag uiteraard ook met een softwaretool (zie onderstaande lijst).

2.\ Pas threat modelling toe op je DFD. Geef in je DFD aan waar welke risico’s zitten (interfaces: plekken waar data over een trust boundary gaat). Gebruik hiervoor de STRIDE-methodiek. Denk hierbij aan de afkorting:

* <b>S</b>poofing: je voordoen als iemand anders of een ander system, bijv. doordat er geen wachtwoordeisen zijn.
* <b>T</b>ampering: aanpassen van data op een systeem of netwerk, bijv. XSS.
* <b>R</b>epudiation: ontkennen van iets dat je gedaan hebt, bijv. doordat er geen logging is.
* <b>I</b>nformation Disclosure: ongeautoriseerd toegang verschaffen tot data, bijv. mogelijk gemaakt door *plain text* versturen van data.
* <b>D</b>enial of Service: werking van services verhinderen, bijv. DDOS-aanval.
* <b>E</b>levation of Privilege: toegang krijgen tot rechten die je niet had, bijv. door gebruik te maken van kwetsbaarheden in slechte/oude software.

3.\ 

A. Maak een opsomming van de interfaces waarvan jij denk dat ze getest moeten worden op security-aspecten.

B. Prioriteer deze lijst en onderbouw je keuzes daarin. 

C. Beschrijf voor de top 3 van kwetsbare interfaces welke maatregelen er genomen kunnen worden (geef meerdere opties; denk ook aan tijd-/geld-investering van het bedrijf!). Denk hierbij aan de afkorting META:

* <b>M</b>itigate: een tegenmaatregel implementeren
* <b>E</b>liminate: de interface geheel verwijderen
* <b>T</b>ransfer: de verantwoordelijkheid overdragen aan een andere partij
* <b>A</b>ccept: het risico voor lief nemen en niets doen

*Tip: je kunt 2, 3A, B en C grotendeels in één keer maken door gebruik te maken een tabel met kolommen voor de interfaces, de STRIDE-letters, de scenario's, de prioriteiten en de tegenmaatregelen, en deze te sorteren op prioriteit. Zie bijvoorbeeld de Excel-sheet die op Blackboard staat. Denk er wel om dat je de **onderbouwing** van je prioritering erbij vermeldt!*

## Tools voor het tekenen van DFD's

De DFD is de basis voor de opdracht van deze (en volgende) week. Je mag hem op papier tekenen of desnoods in MS Paint, maar er zijn betere (gratis) tools beschikbaar die je het leven wat gemakkelijker kunnen maken, zoals:

* [LucidChart](https://www.lucidchart.com/pages/data-flow-diagram)
* [Draw.io](https://app.diagrams.net/) met [deze plugin](https://github.com/michenriksen/drawio-threatmodeling)
* [Miro](https://miro.com/templates/data-flow-diagram/)
* [Drawboard PDF](https://www.drawboard.com/pdf/)
* [GraphViz](https://graphviz.org/)
* [SDL: de Microsoft Threat Modeling Tool](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling)

Om maar een paar te noemen. Aanvullingen (in de vorm van een [pull request](https://github.com/hanze-hbo-ict/sw_sec_docs)) zijn van harte welkom.