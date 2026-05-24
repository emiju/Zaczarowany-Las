import random

nazwa_wyprawy = "Wyprawa przez Zaczarowany Las"
poczatkowe_x = 0
poczatkowe_y = 0
poczatkowa_energia = 10

print(f"=== {nazwa_wyprawy} ===")
bohater = input("Podaj imię swojego bohatera: ")

x = poczatkowe_x
y = poczatkowe_y
energia = poczatkowa_energia
kroki = 0

historia_zdarzen = []
przyczyna_zakonczenia = ""
wynik_koncowy = ""

print(f"\nWitaj {bohater}! Zaczynasz na pozycji ({x}, {y}) z {energia} punktami energii.")
print("Twój cel: Dotrzeć do skarbu na pozycji (3, 3).")
print("Uważaj, by nie wyjść poza granice lasu (od -5 do 5) i nie stracić całej energii!")
print("------------------------------------------")

while True:
    kroki = kroki + 1
    print(f"\n--- KROK {kroki} ---")
    print(f"Pozycja: ({x}, {y}) | Energia: {energia}")
    
    ruch = input("Gdzie idziesz? (w - góra, s - dół, a - lewo, d - prawo): ").lower()
    

    wykonano_ruch = False
    

    if ruch == 'w':
        y = y + 1
        wykonano_ruch = True
    elif ruch == 's':
        y = y - 1
        wykonano_ruch = True
    elif ruch == 'd':
        x = x + 1
        wykonano_ruch = True
    elif ruch == 'a':
        x = x - 1
        wykonano_ruch = True
    else:
        print("Nieznany kierunek! Stoisz w miejscu, ale tracisz czas.")
    

    energia = energia - 1
    
    if wykonano_ruch == True:
        szansa = random.randint(1, 3)
        
        if szansa == 1:
            print("! ZDARZENIE: Znalazłeś dzikie jagody! Zyskujesz 3 energii.")
            energia = energia + 3
            historia_zdarzen.append(f"Krok {kroki}: Znaleziono jagody na pozycji ({x}, {y})")
            
        elif szansa == 2:
            print("! ZDARZENIE: Potknąłeś się o ukryty korzeń! Tracisz 2 energii.")
            energia = energia - 2
            historia_zdarzen.append(f"Krok {kroki}: Wypadek na pozycji ({x}, {y}) - utrata energii")
        

    if x == 3 and y == 3:
        przyczyna_zakonczenia = "Dotarcie do wyznaczonego celu (Skarbu)."
        wynik_koncowy = "SUKCES"
        break
        
    if energia <= 0:
        przyczyna_zakonczenia = "Brak energii na dalszą podróż."
        wynik_koncowy = "PORAŻKA"
        break
        
    if x < -5 or x > 5 or y < -5 or y > 5:
        przyczyna_zakonczenia = "Przekroczenie bezpiecznej granicy mapy."
        wynik_koncowy = "PORAŻKA"
        break


print("\n" + "="*50)
print("             RAPORT PODSUMOWUJĄCY")
print("="*50)

print(f"1. Nazwa wyprawy/obiektu: {nazwa_wyprawy} (Bohater: {bohater})")
print(f"2. Parametry początkowe: Pozycja startowa ({poczatkowe_x}, {poczatkowe_y}), Początkowa energia: {poczatkowa_energia}")
print(f"3. Końcowa pozycja: ({x}, {y})")
print(f"4. Liczba wykonanych kroków: {kroki}")
print(f"5. Pozostały zasób (energia): {energia}")

print("6. Najważniejsze zdarzenia podczas wyprawy:")
if len(historia_zdarzen) > 0:
    for zdarzenie in historia_zdarzen:
        print(f"   - {zdarzenie}")
else:
    print("   - Brak ważnych zdarzeń. Podróż przebiegła spokojnie.")

print(f"7. Przyczyna zakończenia wyprawy: {przyczyna_zakonczenia}")
print(f"8. Końcowy wynik: {wynik_koncowy}")

print("="*50)

input("\nProgram zakończył działanie. Naciśnij ENTER, aby wyjść...")