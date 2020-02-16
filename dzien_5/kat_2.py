wynik = []
# for liczba in range(21)
#     if liczba % 3 == 0
#         wynik.append(liczba ** 3)

wynik = [liczba ** 3 for liczba in range(21) if liczba % 3 == 0]
print(wynik)