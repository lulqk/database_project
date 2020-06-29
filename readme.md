# Projekt: Export danych z PostgreSQL do MongoDB przy uzyciu djangorestframework

## Wymagania:
+ Docker
+ docker-compose

## Opis

W celu uruchomienia projektu należy uruchomic plik docker-compose.yml
W terminalu wpisujemy:
> docker-compose build
> docker-compose up

Po porawnym zbudowaniu obrazu i uruchomieniu będziemy mogli przejśc do dwóch stron:
+ [Interfejs użytkownika](http://0.0.0.0:8008)
+ [Panel MongoExpress](http://0.0.0.0:8081)

W interfejsie użytkownika pokazane są dwie tabele: PostreSQL i MongoDB
![Screenshot](zrzut.png "Interfejs")

Dodając producenta oraz model pojazdu rekord dodawany jest do PostgreSQL.
W celu exportu bazy MongoDB należy przy danym modelu wciśnąć przycisk "Exportuj".

