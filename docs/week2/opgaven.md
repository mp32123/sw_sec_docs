# Opgaven week 2: hacking the Juice Shop

In dit practicum gaan we aan de slag met het opsporen van beveiligingsproblemen binnen een webshop applicatie. Voor deze opdracht gaan we verder met OWASP ZAP, mocht deze nog niet geinstalleerd zijn kijk dan nog onder de opdracht van week 1 voor de installatie.
 
Aan de slag met de Juice Shop
We gaan in deze opdracht aan de slag met een Juice Shop web applicatie welke een aantal grote beveiligingslekken heeft. De Juice Shop applicatie gaan we via Docker draaien op je computer. Hierna gaan we beveiligingslekken opsporen in de applicatie.
1.	Met Docker is het mogelijk om een webapplicatie te starten in een vooropgezette omgeving, ook wel container genoemd. Je kunt een Docker container downloaden en deze bevat dan zowel een volledige ingerichte serveromgeving als een de geïnstalleerde en geconfigureerde webapplicatie. Let op: Als je VM-software hebt geïnstalleerd zal Docker niet werken. Maak in dit geval een Virtual Machine naar keuze (een servervariant van Linux is echter het snelst) en installeer Docker in deze VM.

Download en installer Docker via https://docs.docker.com/get-docker/
2.	Download en installeer de Juice Shop Docker container met de volgende commando’s:
$ docker pull bkimminich/juice-shop
$ docker run --rm -p 3000:3000 bkimminich/juice-shop
3.	Als alles goed is gegaan kun je de applicatie bereiken via http://localhost:3000 in de browser.
4.	Klik door de Juice shop heen en plaats bijvoorbeeld een bestelling
  
Opdracht: Het opsporen van beveiligingsproblemen
 In deze opdracht gaan we daadwerkelijk aan de slag met het opsporen van beveiligingsproblemen in de Juice Shop applicatie. Hiervoor is het belangrijk dat ZAP zonder problemen draait en dan de Juice Shop werkt op je eigen computer.
1.	Cross-site Scripting, ook wel XSS genoemd, betekent dat een externe partij JavaScript kan uitvoeren binnen de applicatie. Ga op zoek naar een plek in de webapplicatie waar het mogelijk is om javascript in te voeren die daarna wordt uitgevoerd. Tip: Met behulp van alert() in javascript is het mogelijk om een pop-up venster te openen. Het hoorcollege van deze week bevat hier voorbeeldcode voor die je kunt gebruiken.

Toon je antwoord aan met een of meer screenshots waaruit duidelijk naar voren komt waar de javascript ingevoerd wordt en dat deze uitgevoerd wordt. Laat ook de url zien die de XSS veroorzaakt. Beschrijf hierbij ook kort welke stappen je hebt uitgevoerd om tot je antwoord te komen.   (40%)
2.	Er zit een groot probleem in Juice Shop waardoor het mogelijk is om een bestelling te plaatsen met een negatief totaalbedrag. Hierdoor zou je in theorie geld toe moeten krijgen. Ga op zoek naar een manier om dit te veroorzaken. Tip: Via ZAP zie je alle uitgaande requests. Maak een aantal bestellingen en ga op zoek naar een PUT- of POST-request die je kunt aanpassen. Om een bestelling te plaatsen zul je eerst moeten inloggen. Hiervoor kun je een account aanmaken, of je kunt proberen om met bv. SQL-injectie het inloggen te omzeilen (zie opdracht 3)...

Toon je antwoord aan met de PDF van je bestelling waar een negatief te betalen bedrag op staat. Laat daarnaast je aangepaste PUT/POST-request zien, en beschrijf welke stappen je hebt uitgevoerd om tot je antwoord te komen. (40%)
3.	Ga zelf op zoek naar nog een beveiligingslek en toon deze ook weer aan doormiddel van screenshots en indien van toepassing aangepaste requests. Beschrijf daarnaast welke stappen je hebt uitgevoerd om tot je antwoord te komen. (20%)

Enkele suggesties om te proberen:
- Laat een review achter onder andermans naam
- Log in op het admin-account d.m.v. SQL-injectie
- Ontdek het patroon in de kortingscoupons en maak je eigen coupon om tot wel 90% korting te krijgen
Of bedenk zelf iets anders!

