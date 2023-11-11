# Basisproject API Development
*Jorben Sterckx 2CCS02*
## Thema API
Voor mijn project heb ik het thema **voetbal** gekozen. 
Ik heb dit gekozen omdat ik al jaren bezig ben met voetbal en zelf ook een lange tijd heb gevoetbald.

In mijn database staan 2 tabellen:
- football_clubs
- players

Waarbij ik door een POST request een voetbalclub kan aanmaken en spelers kan toevoegen aan deze club.

## Werking API
In deze sectie ga ik laten zien hoe mijn API werkt en welke endpoints ik heb gebruikt.

### POST
Ik heb 2 POST endpoints gemaakt.
1. De eerste dient voor het aanmaken van een voetbalclub.
2. De tweede dient voor het aanmaken van een speler.
#### Aanmaken voetbalclub:
![Screen van postman voor het aanmaken van een voetbalclub](/screens/aanmaken_voetbalclub.png)
![Screen van postman voor het aanmaken van een voetbalclub](/screens/aanmaken_voetbalclub2.png)

#### Aanmaken speler:
![Screen van postman voor het aanmaken van een speler](/screens/aanmaken_speler.png)
![Screen van postman voor het aanmaken van een speler](/screens/aanmaken_speler2.png)
![Screen van postman voor het aanmaken van een speler](/screens/aanmaken_speler3.png)

### GET
Ik heb 4 GET endpoints gemaakt:
1. De eerst dient voor het terug krijgen van elke voetbalclub inclusief de spelers.
2. De tweede dient voor het terugkrijgen van een specifieke voetbalclub inclusief de spelers door de clubID toe te voegen.
3. De derde dient voor het terug krijgen van alle spelers van een specifieke voetbalclub.
4. De laatste dient voor het terug krijgen van een specifieke speler door de spelerID toe te voegen.
#### Terugkrijgen van elke voetbalclub (inc. speleres)
![Screen van postman voor het krijgen van voetbalclubs](/screens/krijgen_clubs1.png)
![Screen van postman voor het krijgen van voetbalclubs](/screens/krijgen_clubs2.png)

#### Terugkrijgen van een specifieke voetbalclub (inc. speleres)
![Screen van postman voor het krijgen van een specifieke voetbalclubs](/screens/krijgen_specifieke_club.png)

#### Terugkrijgen van alle spelers van een voetbalclub
![Screen van postman voor het krijgen van de spelers van een voetbalclubs](/screens/krijgen_spelers_van_club.png)

#### Terugkrijgen van een specifieke speler
![Screen van postman voor het krijgen van een speler](/screens/krijgen_speler.png)

### DELETE
Ik heb 2 DELETE endpoints gemaakt:
1. De eerste dient voor het verwijderen van een speler.
2. De tweede dient voor het verwijderen van een voetbalclub.
#### Verwijderen van een speler
![Screen van postman voor het verwijdren van een speler](/screens/delete_player.png)

#### Verwijderen van een voetbalclub
Voor een voetbalclub te verwijderen mogen er geen spelers meer in de club zitten.
Daarom heb ik dus eerst alle spelers verwijderd in voetbalclub id=2.
![Screen van postman voor het verwijdren van een voetbalclub](/screens/delete_club.png)

#### Resultaat
![Screen van postman van het resultaat na het verwijderen](/screens/result.png)

### PUT
De PUT request dient voor alle data in de aangegeven voetbalclub aan te passen.
Ookal geef je sommige velden niet mee in de request, worden deze toch aangepast.
#### Updaten van een voetbalclub
![Screen van postman van de put](/screens/put_van_club.png)
> Note: Voor de oplettende kijker zie je dat de id van de speler is vernaderd.
> De PUT request heb ik helemaal als laatste getest. Wat wilt zeggen dat ik hiervoor dus nog wat
> testen heb gedaan met spelers maken en verwijderen. daarom dat de id verschillend is als op
> de andere screens.

### PATCH
De PATCH request dient voor gedeeltelijke aanpassingen te doen in de aangegeven voetbalclub.
Hierbij moet je niet elk veld meegeven en worden alleen de velden die je stuurt aangepast.
#### Gedeeltelijk updaten van een voetbalclub
![Screen van postman van de patch](/screens/patch_van_club.png)

## OpenAPI docs
Dit is mijn OpenAPI documentatie die ik terug vind wanneer ik naar mijn localhoste op poort 8000 /docs ga http://127.0.0.1:8000/docs.
![Screen van OpenAPI docs](/screens/docs1.png)
![Screen van OpenAPI docs](/screens/post1.png)
![Screen van OpenAPI docs](/screens/post2.png)
![Screen van OpenAPI docs](/screens/get1.png)
![Screen van OpenAPI docs](/screens/get2.png)
![Screen van OpenAPI docs](/screens/get3.png)
![Screen van OpenAPI docs](/screens/get4.png)
![Screen van OpenAPI docs](/screens/delete1.png)
![Screen van OpenAPI docs](/screens/delete2.png)
![Screen van OpenAPI docs](/screens/put.png)
![Screen van OpenAPI docs](/screens/patch.png)
![Screen van OpenAPI docs](/screens/schemas.png)

## Hosted API
Dit is de link waar mijn API wordt gehost: [Hosted API](https://project-service-jorbensterckx.cloud.okteto.net)

## Extra
### PUT & PATCH
Als extra heb ik nog een PUT & PATCH request aangemaakt.
Dit dient voor het updaten van de data via een request.

### Security
Als ik iets wil uitvoeren op de OpenAPI site of op mijn hosted API,
wordt er naar een gebruikersnaam en wachtwoord gevraagd. Hiervoor heb ik gebrukt:
- Gebruikersnaam: ***testtest@yahoo.com***
- Wachtwoord: ***ILoveInternetExplorer***