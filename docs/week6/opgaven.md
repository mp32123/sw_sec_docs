# Opgave week 6 – security: de verantwoordelijkheid van de ontwikkelaar(?)
 
Je hebt in deze cursus allemaal tools aangereikt gekregen om veilige(re) applicaties te bouwen. Betekent dit nu dat security exclusief jouw verantwoordelijkheid als engineer<sup>*</sup> is? Ben je als engineer immers niet ook onderdeel van een groter geheel (team, bedrijf, sector, land, EU...) en is security niet eerder een gedeelde verantwoordelijkheid? Welke partijen kun je allemaal aanwijzen en voor welk aspect van security (welk onderdeel van de Software Development Life Cycle) zouden zij verantwoordelijk kunnen/moeten zijn?

Ga eerst over deze vragen in discussie je klasgenoten en vorm zo je eigen mening.

Dan de casus (kenners herkennen in deze casus wellicht delen van de cultfilm [Office Space](https://www.imdb.com/title/tt0151804/), verplichte kost voor elke ICT'er). Je bent engineer<sup>*</sup> bij de firma Initech. Het management heeft het plan opgevat om maandelijks zogenaamde [TPS Reports](https://en.wikipedia.org/wiki/TPS_report#Office_Space) te laten genereren die allerlei informatie bevatten over de productiviteit van elke medewerker. Denk hierbij aan data als: ziekte en ander verzuim, aantal vergaderuren, aantal geschreven regels code, aantal ingediende pull-requests, percentage goedgekeurde pull-requests etc. De rapporten zijn intern en bestemd voor de managers van de betreffende medewerkers. Aan jou is gevraagd om de applicatie te (helpen) ontwikkelen die deze rapporten kan genereren en verdelen onder de juiste personen.

Het moge duidelijk zijn dat, als Initech dit per se wil doen, het heel zorgvuldig moet gebeuren, omdat hier allerlei risico's op de loer liggen, op het gebied van privacy, datalekken, tampering etc. Welke adviezen kun jij aan [de CEO van Initech](https://en.wikipedia.org/wiki/Bill_Lumbergh) geven om deze risico's in ieder geval te minimaliseren?

## Deel 1

Noem 3 activiteiten die jij als engineer<sup>*</sup> kunt doen om tot een zo veilig mogelijke applicatie te komen. Leg bij elke activiteit uit in welke fase je deze toepast (Requirements, Ontwerp, Ontwikkeling, Testen en Deployment) en waarom deze bijdraagt aan een veilige applicatie.

_Voorbeeld: in de fase Ontwerp plannen we een sessie in met een security-expert om een Security Design Review te doen van het gemaakte ontwerp. Dit komt de veiligheid ten goede omdat de expert fouten in het ontwerp zal zien die wij als ontwikkelaars niet gezien hadden. En doordat we er vroeg bij zijn, kunnen deze nog zonder al te veel kosten worden gecorrigeerd._

## Deel 2

Je bent natuurlijk niet de enige binnen dit project. Noem 3 andere partijen die volgens jou ook een rol (zouden moeten) hebben bij de security van de TPS Reports, plus bij elk een korte beschrijving wat die rol dan zou moeten inhouden en in welke fase(s) van de SDLC deze van toepassing is.

Met _partijen_ bedoelen we onder andere: andere teamleden, andere functies of afdelingen binnen hetzelfde bedrijf, de klant, andere bedrijven, providers, (cloud)hosts, vakbonden, politie, bestuursorganen zoals gemeentes, provincies, de Tweede Kamer, de regering en de EU maar ook bijvoorbeeld de Autoriteit Persoonsgegevens. Eigen toevoegingen zijn van harte welkom!

_Voorbeeld: er moet een security-expert, intern of van een extern bureau, bij het project betrokken worden, zodat diegene de requirements, ontwerpen, gerealiseerde code en de uiteindelijke setup kan controleren op veiligheidsissues._

## Oplevering

Maak van bovenstaande punten een lopend verhaal, en voeg een korte inleiding en conclusie toe. Schrijf het in de vorm van een advies aan het management van de firma Initech. Richtlijn: 1 A4'tje, ongeveer 300 woorden.

-----
<sup>*</sup> _Lees hier, afhankelijk van je gekozen richting, software engineer danwel network & security engineer._
