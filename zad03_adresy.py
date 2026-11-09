"""Zad. 3 - lista wszystkich adresów w dzielnicy (pętla for)."""

ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
BLOKI_NA_ULICY = 5
LOKALE_W_BLOKU = 10

for ulica in ulice:
    for blok in range(1, BLOKI_NA_ULICY + 1):
        for lokal in range(1, LOKALE_W_BLOKU + 1):
            print(f"ul. {ulica} {blok}/{lokal}")
