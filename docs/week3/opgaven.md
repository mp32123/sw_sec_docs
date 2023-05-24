# Opgaven week 3: security tooling in software development

Deze week gaan we niet bezig met een technische opgave, maar gaan we zelfstandig onderzoek doen naar een belangrijke vraag voor de praktijk: wat is de toegevoegde waarde van security tooling in het proces van softwareontwikkeling? 

Software-ontwikkelingsprojecten bestaan uit meerdere trajecten en omvatten meer dan alleen ontwikkeling en testen: voor elk project moet rekening worden gehouden met regionale en internationale wetgeving en standaarden, die niet alleen een impact kunnen hebben op de requirements van het project, maar ook op verscheidene aspecten van security. Deployment en operationeel onderhoud zijn daarnaast ook onderdeel van het proces van softwareontwikkeling en in moderne omgevingen maken DevOps-teams (een werkmethode waarbij development en post-deployment onderhoud & support door hetzelfde team worden uitgevoerd) de grens tussen Software Security en IT Security nóg waziger. 

Tijdens deze opdracht kijken we naar de niche die software security tooling kan vullen in een softwareontwikkelingsproject en voor welke aspecten het minder of helemaal niet nuttig is. Het is voor een bedrijf namelijk heel makkelijk om veel geld uit te geven aan tooling die in de praktijk weinig toegevoegde waarde heeft, maar tegelijkertijd zijn sommige aspecten van software security nagenoeg onmogelijk zonder het gebruik van de juiste tooling. 

## Opdracht 1 
Voor je begint met je daadwerkelijke analyse is het bijzonder handig om wat extra informatie tot je te nemen. Lees vooral eens de onderstaande bronnen door:

 * De [BSIMM software security activity list](https://www.bsimm.com/framework/) is een software security framework dat in de praktijk vaak gebruikt wordt. Het framework is onderverdeeld in vier domeinen met elk drie aspecten van het softwareontwikkelingsproces. Onder elk van deze aspecten kun je vervolgens lezen over de verscheidene activiteiten die in de praktijk worden gebruikt. 
 * In [deze whitepaper van de versimpelde implementatie van Microsofts SDL](https://www.microsoft.com/en-us/download/details.aspx?id=12379) kun je lezen over de verschillende eisen die Microsoft stelt aan hun eigen ontwikkelproces. 

Niet alles wat in deze bronnen staat is trouwens per se een goed idee, en je moet ze vooral ook niet interpreteren als een harde eis waar elk softwareontwikkelingsproject aan moet voldoen. Het zijn meningen en voorbeelden - al zij het meningen en voorbeelden van teams met ervaring. Probeer tijdens het lezen van de bronnen alvast te denken aan hoe je de informatie kunt gebruiken om opdracht 2 te maken. Hiervoor kun je jezelf de volgende vragen stellen:

1. Lijkt er een bepaalde soort activiteit binnen het softwareontwikkelingsproces te zijn waar vaak tooling bij wordt gebruikt? Waarom is dit denk je? 
2. Zijn er ook activiteiten waar juist nooit enige vorm van tooling of automatisering wordt toegepast? Is er een gemene deler tussen deze activiteiten? 
3. Verwacht je dat er een verschil is tussen de hoeveelheid en soorten tools die worden gebruikt in verschillende software projecten? Onderstaande enkele voorbeelden van verschillende projecten:

    A. Een Agile/Scrum-project waarbij een boel nieuwe code wordt geschreven voor Node.js

    B. Een project dat een gigantische C++ codebase uit 1992 moet onderhouden

    C. Een C-project voor medische apparatuur die een kritieke rol speelt in patiëntveiligheid

    D. Een open-source Python-project dat GNU GPL code schrijft en publiceert op GitHub

    E. Een topgeheim militair project in Erlang

### Wat moet je inleveren? 
Kopieer bovenstaande drie vragen en geef daarop antwoord. Voor vraag 3 wordt niet verwacht dat je diepgaande kennis van de relevante talen, projectvormen en bedrijfsprocessen hebt of toont, maar probeer met de kennis die je wel hebt zo oprecht mogelijk de vragen te beantwoorden: maak een schatting of extrapoleer op basis van de kennis die je wél hebt. 

Opdracht 1 wordt beoordeeld met een voldoende/onvoldoende op basis van getoonde inzet; je cijfer van deze week wordt vervolgens bepaald door opdracht 2. Voor opdracht 1 geldt qua woordental geen ondergrens en **een maximum van 500 woorden** (exclusief de vragen). 

## Opdracht 2 
Kies één commerciële of niet-commerciële tool die zich hoofdzakelijk richt op het verbeteren van software security. Hieronder staat een lijst voorbeelden om uit te kiezen, maar je bent vrij om zelf een andere tool te vinden. Sommige zijn voorzien van een link die je als startpunt van je leerproces kunt gebruiken. Let er wel op dat wanneer je zelf een tool kiest, dit er een is die een directe impact heeft op softwareontwikkeling of -onderhoud. Kies dus niet iets als een firewall, VPN, IDS of antivirussoftware. Bij twijfel kun je altijd aan je docent vragen of de tool geschikt is.

**Vulnerability Scanners**

 * [Acunetix](https://www.softwaretestinghelp.com/acunetix-web-vulnerability-scanner-wvs-review/)
 * [Nessus](https://medium.com/@PenTest_duck/offensive-nessus-installation-simple-windows-vulnerability-scanning-2d4d707859ae)
 * OWASP ZAP (is toegestaan, maar omdat deze tool al enigszins bekend is, verwachten we hier wel wat extra diepgang)

**Security Testing Frameworks**

 * [Metasploit](https://medium.com/swlh/intro-to-metasploit-19e3d07ff725)

**[Static Analysis](https://unicorn-dev.medium.com/the-way-static-analyzers-fight-against-false-positives-and-why-they-do-it-743de1f2a1bd)**

 * [PyLint](https://medium.com/@ryangordon210/build-a-python-ci-cd-system-code-quality-with-pylint-f6dea78461c6)
 * [Coverity](https://www.synopsys.com/blogs/software-security/coverity-setting-the-standard/)
 * [snyk](https://eldadfux.medium.com/this-is-how-we-use-snyk-to-protect-our-open-source-projects-from-evil-dependencies-6ee258ca5815)
 * [SonarQube](https://betterprogramming.pub/how-to-improve-code-quality-with-sonarqube-465744eb66db)
 * [Veracode](https://medium.com/@AccompliceVC/the-veracode-journey-origin-and-introspection-13c0c74b82e2)

**Source code compliance scanners / Software Composition Analysis (SCA)**

 * [Black Duck](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html)

**Threat Modeling Tools**

 * [Attack Trees](https://medium.com/@tashjnorris/using-threat-models-for-incidents-and-how-incidents-helped-me-like-attack-trees-a27eb65f9039)
 * [Microsoft SDL](https://www.youtube.com/watch?v=wUt8gVxmO-0)

**Configuratiecheckers**

 * [testssl.sh](https://www.blackhillsinfosec.com/testssl-sh-assessing-ssltls-configurations-at-scale/)
 * Docker Bench for Security

**Load-testers**

 * Zie [https://theqalead.com/tools/load-testing-tools/]( https://theqalead.com/tools/load-testing-tools/)

**Modellen (beide aangestipt in het HC)**

 * [BSIMM](https://www.synopsys.com/software-integrity/software-security-services/bsimm-maturity-model.html)
 * [OWASP SAMM](https://owaspsamm.org/)

Verdiep je na het selecteren van een tool in de functionaliteit ervan d.m.v. feature lists, whitepapers, handleidingen, demovideo’s, Medium-artikelen etc. Let hierbij op de redenen die worden gegeven voor waarom je het product zou moeten gaan gebruiken, wat het precies doet ("scanning" is een nogal vage term...) en wat de tool belooft op te leveren. 
 
### Wat moet je inleveren?
Beantwoord de onderstaande vragen. Kopieer de vragen en schrijf je antwoord daar direct onder. Je hoeft slechts een paar zinnen per vraag te schrijven, maar **let erop dat je antwoord duidelijk laat zien dat je een doordachte analyse hebt uitgevoerd**. Let voor een voldoende hierbij ook goed op dat je de waarom-vragen beantwoordt.

1. Welke tool heb je onderzocht? 
2. In welk deel van het softwareontwikkelingsproces kan de tool het beste worden toegepast (bijv. projectbeheer, productbeheer, testen, deployment, post-deployment support)? Waarom juist daar en niet een ander deel? Onderbouw je antwoord a.d.h.v. de kwaliteiten & gebreken van de tool.
3. Noem minstens twee werkzaamheden **binnen dit deel van het softwareontwikkelingsproces** die wel moeten gebeuren, maar waar de tool niet bij helpt. Waarom past de tool hier niet bij? 
4. Leg uit hoe de tool werkt vanuit een technisch perspectief. M.a.w.: omschrijf de onderliggende technieken die de tool gebruikt om zijn functionaliteit te leveren. *Bijvoorbeeld: Radamsa is een generator voor fuzzing-testcases. Deze tool werkt door a.d.h.v van een set mogelijke wijzigingen (e.g. bit flipping, byte insertion, line deletion, etc.) een gegeven string te muteren. Door vele verschillende versies van deze mutaties te genereren bouwt Radamsa een representatieve set mogelijke mutaties van een realistische inputstring.*
5. Wat voor risico’s helpt te tool om te voorkomen? Hoe? Onderbouw je antwoord door uit te leggen hoe specifieke functionaliteit van de tool leidt ot mitigatie van de genoemde risico’s. In het (onwaarschijnlijke) geval dat de tool geen enkel risico afdekt: onderbouw hoe je tot die conclusie bent gekomen.
6. Wat voor problemen zul je rekening mee moeten houden je als je de tool zou willen toepassen in een echt project? En belangrijker: waarom verwacht je deze problemen tegen te komen? *(Voorbeelden van dergelijke problemen zijn: er is veel specialistische kennis nodig om te tool te gebruiken; kan de tool opschalen voor grotere organisaties; is het veel werk om de tool überhaupt op te zetten; zullen developers de tool willen gebruiken gezien de tijdsdruk waar ze onder werken; vertraagt het andere onderdelen van het ontwikkelproces; kost het veel handmatig werk om te gebruiken of in de bestaande ‘toolchain’ te integreren; past de tool binnen een agile werkproces; etc.)*

N.B.: zorg dat je in je antwoord geen tekst van de promotie-/informatiematerialen van de tool kopieert. Er geldt geen minimumlengte, zolang je maar zorgt dat je antwoorden goed onderbouwd zijn en aantonen dat je onderzoek hebt gedaan. Er is wel een maximumlengte: exclusief de vragen mag je antwoord **maximaal 1000 woorden** bevatten.

Wat betreft het gebruik van **ChatGPT** of andere soortgelijke technieken: het is niet toegestaan om je antwoorden te laten genereren, het dient eigen werk te zijn. Hier zal ook op gecontroleerd worden. Wat wel mag, is deelvragen voorleggen aan ChatGPT en de antwoorden hierop, voorzien van bronvermelding en eigen reflectie, mee te nemen in je antwoorden.

Je moet opdracht 1 met een voldoende maken om een cijfer te kunnen krijgen, dit cijfer wordt vervolgens bepaald door je antwoorden op opdracht 2. Hierbij kijken we voornamelijk naar hoe goed je analyse de laatste vraag ontleedt, en dan vooral hoe goed je de waarom-vraag beantwoordt: alleen een probleem noemen zonder een goede reden te geven zal weinig punten opleveren. 

Voor **herkansers** geldt dat zij een andere tool dan het voorgaande jaar dienen te kiezen! Hierop zal gecontroleerd worden.