# Webapp en bestanden voor het Hydra-practicum, week 1 van (Software) Security

## Webapp

`app.py`, `requirements.txt` en de map `mijnproject/` vormen een simpele Flask-webapp die je kunt gebruiken om te bruteforcen.
Zet deze bestanden op je eigen systeem, maak een virtual environment aan en installeer `requirements.txt`.
Daarna kan de webapp gedraaid worden. Nog gemakkelijker is het om de webapp te pullen van DockerHub en als container te draaien.

## Docker

[Download de image van DockerHub](https://hub.docker.com/r/tomerikroos/webapp-hydra) en draai hem als container.
Als je alles op de commandline doet, ziet het er als volgt uit:
```
docker pull tomerikroos/webapp-hydra
docker run --rm -p 5000:5000 tomerikroos/webapp-hydra
```
Gebruik je Docker Desktop o.i.d. voor het runnen, let er dan op dat je bij de "Optional settings" de host-poort 5000 koppelt aan poort 5000 van de container.
In beide gevallen kun je daarna via localhost:5000 bij de webapp.

## Bestanden

In `rockyou/` staat een verkorte versie van de RockYou-passwordlijst.