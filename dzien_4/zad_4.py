# # def formatuj(*args,**kwargs):
# #     tekst =""+ "\n".join(args)
# #
# #     for slowo,wartosc in kwargs.items():
# #         klucz = "$" + slowo
# #
# #         tekst = tekst.replace(klucz, wartosc)
# #
# #     return tekst
# #
# # # formatuj("koszt $cena PLN",
# # #         "kwota $cena brutto",
# # #         "podatek $podatek %",
# # #         cena = 10,
# # #         podatek = 23
# #
# # #)
# #
# #
# # def test_formatuj():
# #     assert formatuj(
# #         'koszt $cena'
# #         "kwota $cena brutto",
# #         "podatek $podatek %",
# #         cena = 10,
# #         podatek = 23
# #     )
# #
#
#
# #
# # def add(a,b):
# #
# # def sub(a, b):
# #
# # def mul(a, b):
# #
# # def aiv(a, b):
#
# lista = [1, 2, 3, 4, 5, 6, 7]
#
# # def select(lista, func):
# #     return [x for x in lista if func(x)]
# #
# # def test_select():
# #     assert select(lista, lambda x: x % 2 == 0) == [12, 8, 4, 16]
# #     assert select(lista, lambda x: x > 10) == [12, 16]
#
# def przytnij(lista, func, func1):
#    wynik = []
#    dodawaj = False
#     for i in lista:
#         if func(i):
#             dodawaj = True
#         if dodawaj:
#             wynik.append(i)
#         if func1(i):
#             break
#     return wynik
#
# def test_przytnij():
#     assert przytnij(lista=[1, 2, 3, 4, 5, 6],
#                     start=lambda x: x > 3,
#                     stop=lambda x: x == 6 ) == [4, 5, 6]
#

# def silnia(x):
#     y = 1
#     for i in range(x):
#         y = y * (i + 1)
#     return y
#
# def test_silnia():
#     assert silnia(4) == 24
#     assert silnia(5) == 120

def silnia(x):
    if x == 0:
        return 1
    else:
        return x * silnia(x-1)

def test_silnia():
    assert silnia(4) == 24
    assert silnia(5) == 120