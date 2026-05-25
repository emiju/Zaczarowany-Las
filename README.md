# Symulator wyprawy po dwuwymiarowym świecie: Zaczarowany Las

## Opis programu
Projekt to tekstowa gra przygodowa napisana w języku Python. Gracz wciela się w bohatera, który musi przejść przez las, aby odnaleźć ukryty skarb. Podczas wędrówki musi uważać na poziom swojej energii, reagować na losowe zdarzenia oraz pilnować, aby nie wyjść poza granice bezpiecznego obszaru. 

Projekt został przygotowany w ramach konkursu i spełnia wszystkie założenia symulacji w trybie tekstowym.

## Wymagania
* Zainstalowany Python w wersji 3.11 (zgodnie z wymaganiami zadania).
* Program korzysta wyłącznie z wbudowanych modułów (np. `random`), więc nie wymaga połączenia z Internetem ani instalacji dodatkowych bibliotek.

## Instrukcja uruchomienia
1. Pobierz plik `main.py` na dysk swojego komputera.
2. Otwórz wiersz poleceń (Terminal / CMD) w folderze, w którym zapisałeś plik.
3. Wpisz poniższą komendę i naciśnij klawisz ENTER:
   `python main.py`

*(W systemie Windows zazwyczaj wystarczy po prostu dwukrotnie kliknąć plik `main.py`, aby program uruchomił się w nowym oknie konsoli. Na końcu działania program poprosi o naciśnięcie klawisza ENTER, dzięki czemu okno nie zamknie się samoistnie przed przeczytaniem raportu).*

## Sterowanie i zasady gry
Gra toczy się w trybie turowym. W każdym kroku program zapyta Cię o kierunek ruchu. 
Wpisz literę i zatwierdź klawiszem ENTER:
* **w** - ruch w górę
* **s** - ruch w dół
* **a** - ruch w lewo
* **d** - ruch w prawo

**Cel:** Dotrzyj na pole o współrzędnych (3, 3) zanim stracisz całą energię!
