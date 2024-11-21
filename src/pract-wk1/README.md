# Webapp en bestanden voor het Hydra-practicum, week 1 van (Software) Security

## Webapp

`app.py`, `requirements.txt` en de map `mijnproject/` vormen een simpele Flask-webapp die je kunt gebruiken om te bruteforcen.
Zet deze bestanden op je eigen systeem, maak een virtual environment aan en installeer `requirements.txt`.
Daarna kan de webapp gedraaid worden. Makkelijker is het om de webapp te pullen van DockerHub en als container te draaien.

## Docker

[Download de image van DockerHub](https://hub.docker.com/r/tomerikroos/webapp-hydra) en draai hem als container.
Let erop dat je bij de "Optional settings" de host-poort 5000 koppelt aan poort 5000 van de container.
Daarna kun je via localhost:5000 bij de webapp.

## Bestanden

In `rockyou/` staat, in twee delen, de RockYou-passwordlijst.