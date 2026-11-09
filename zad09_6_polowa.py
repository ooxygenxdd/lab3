"""Zad. 9.6 - pierwsza połowa łańcucha zapisana w trzecim łańcuchu."""

pierwszy = input("Podaj pierwszy łańcuch: ")
drugi = input("Podaj drugi łańcuch: ")
# pierwsza połowa pierwszego łańcucha
trzeci = pierwszy[:len(pierwszy) // 2]
print(trzeci)
