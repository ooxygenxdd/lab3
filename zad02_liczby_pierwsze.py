"""Zad. 2 - 10 pierwszych liczb pierwszych (pętla while + break)."""

znalezione = []
kandydat = 2

while len(znalezione) < 10:
    pierwsza = True
    dzielnik = 2
    while dzielnik * dzielnik <= kandydat:
        if kandydat % dzielnik == 0:
            pierwsza = False
            break  # znaleziono dzielnik - to nie jest liczba pierwsza
        dzielnik += 1
    if pierwsza:
        znalezione.append(kandydat)
    kandydat += 1

print(",".join(str(x) for x in znalezione))
# Wynik: 2,3,5,7,11,13,17,19,23,29
