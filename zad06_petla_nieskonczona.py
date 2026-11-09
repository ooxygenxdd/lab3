"""Zad. 6 - pętla nieskończona; liczba ujemna kończy pętlę."""

while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        print("Podano liczbę ujemną - koniec.")
        break
    print(f"Podałeś: {liczba}")
