# zbiory
#
# x = set("abcde")
# print(x)
# print(dir(x))
#
# A = {1,2,3,4}
# B = {3,4,5,6}
#
# print(A | B)
# print(A-B)
# print(A&B)
# print(A^B)
# liczby = set()
# while True:
#     polecenie = str(input(print("wprowadź liczbe:")))
#
#     if polecenie == "k":
#
#         break
#     else:
#         liczby.add(int(polecenie))
# parzyste = set(range(0,101,2))
# print(f"zliczb unikalnych : {len(liczby)} w tym parzystych  {len(liczby&parzyste)}")




lista = [3,7,9,5,2,0,1]

for indeks_podstawienia in range(len(lista)):
    inddeks_min_wart = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia + 1):
        if lista[indeks_ogona] < lista[inddeks_min_wart]:
            inddeks_min_wart = indeks_ogona
            lista[indeks_podstawienia],lista[inddeks_min_wart] = lista[inddeks_min_wart],lista[indeks_podstawienia]

# assert lista == [0,1,2,3,5,7,9]
print(lista)