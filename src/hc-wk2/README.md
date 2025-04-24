# Leuke voorbeelden voor in de colleges van week 2

## Cross-site Scripting (XSS)

Aan te tonen in app en app_without_defenses. Begin met app_without_defenses.
In commentaar staan drie soorten 'evil inputs' die je in de tekstbox kunt zetten om de app remote code te laten uitvoeren.
In app.py staat dezelde code, plus drie mogelijke 'defenses' om XSS tegen te gaan.
De eerste blokkeert alles, dus ook de styling van Bootstrap.
De tweede is specifieker; de derde (Talisman) is het mooist want die is helemaal configureerbaar.

## Cross-site Request Forgery (CSRF)

Ga eerst naar https://www.erikroos.org/roosbank/ en log in als 'erik' met wachtwoord '1234' (jaja).
Klik wat rond en doe een overboeking. Klik daarna het tabblad weer dicht, ZONDER eerst uit te loggen.
Open nu csrf.html in je browser, klik op de knop en kijk wat er gebeurt.
Daarna kun je de source van csrf.html laten zien om aan te tonen hoe dit mogelijk was,
in combinatie met het feit dat het cookie van de Roosbank geen 'samesite'-beveiliging heeft.
Daardoor is het mogelijk om vanuit overal een POST-request richting die site te doen.
NB: de code van de Roosbank staat in deze map maar is niet per se nodig.
Je kunt erin kijken om te zien hoe dat cookie gemaakt wordt.