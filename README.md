# Library Desktop
Aplikacja desktopowa do obsługi biblioteki

## Spis treści
* [Informacje](#informacje)
* [Instalacja](#instalacja)
* [Użycie](#użycie)

## Informacje
Program ten został zaprojektowany przy użyciu technologii PySide 2 (Qt5). 
Został stworzony na potrzeby projektu łączącego zewnętrzne API z aplikacją 
desktopową. Program ten można zainstalować z poniższą instrukcją, albo przejść
do wydań po prawej stronie (Releases), gdzie będzie możliwość pobrania pliku
instalacyjnego.

## Setup
Aby uruchomić projekt, upewnij się, że masz zainstalowanego Pythona w wersji 
co najmniej 3.6 i wykonaj poniższe polecenia:

```
$ git clone https://github.com/Zaawansowane-metodyp-programowania/Library-Desktop.git
$ cd Library-Desktop
# pip install virtualenv
$ python -m venv venv
$ virtualenv venv
$ source venv/bin/activate              - Linux and Mac
# Set-ExecutionPolicy RemoteSigned      - Windows
$ venv\Scripts\activate                 - Windows
# Set-ExecutionPolicy Restricted        - Windows
$ pip install -r requirements.txt
```

## Użycie
Uruchom program za pomocą komendy: `python main.py`

Jako zwykły użytkownik należy się zarejestrować. Po utworzeniu konta można się
zalogować. Użytkownik po zalogowaniu się widzi okno powitalne wraz z kilkoma
przyciskami u góry.

* **Strona główna** - strona, na której jesteś, strona powitalna.
  
* **Wypożyczone książki** - tutaj znajdą się wszystkie wypożyczone książki.
W przypadku, gdy użytkownik nie wypożyczył żadnej książki, ta karta jest pusta. Tylko
  pracownicy mogą zwracać wypożyczone książki.
  
* **Biblioteka** - wszystkie dostępne książki. Jako zwykły użytkownik możesz jedynie
zarezerwować interesujące cię tytuły, klikając jednokrotnie w wiersz. 
  Jako pracownik możesz edytować, usuwać, a także wypożyczać dane tytuły 
  innym użytkownikom.
  
* **Profil** - znajdziesz tutaj ustawienia dotyczące twojego profilu, takie jak
imię, nazwisko oraz email. Możesz także z tego poziomu usunąć swoje konto. Jako administrator możesz usuwać konta pozostałych użytkowników.
  
* **Utwórz konto z uprawnieniami** - przycisk widoczny tylko dla administratora.
Dzięki niemu możesz utworzyć konto dla pracownika z odpowiednimi uprawnieniami,
  a także konto drugiego administratora.

* **Zmiana hasła** - tutaj możesz dokonać zmiany swojego hasła. Jako administrator
możesz dokonać zmiany hasła każdego zarejestrowanego użytkownika.
  
* **Wylogowanie** - możesz powrócić do menu logowania.