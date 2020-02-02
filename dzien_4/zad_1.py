#
#
# def is_anagram(a : str, b: str) -> bool:
#    """
#
#    :param a: str
#    :param b: str
#    :return: bool
#    """
#     return sorted(a.lower()) == sorted(b.lower())
#
#     for i, litera in enumerate(napis):
#         a.add(napis[litera])
#     for i, litera in enumerate(napis1):
#         b.add(napis1[litera])
#     return
#
#
# def test_is_anagram():
#     assert is_anagram("Tokio", "Kioto") is True
#     assert is_anagram("anna", "bob") is False

# def flatten(*elements): # *args
#     if len(elements) ==1:
#         elements = elements[0]
#     result = []
#     for el in elements:
#         result.extend(el)
#     return result
#
#
# def test_flatten():
#     assert flatten([[1,2], [3,4]]) == [1,2,3,4]


def largest_different(lista):
    if lista:
        return max(lista) - min(lista)

    # lista = lista.sort()
    #     # return lista[len(s) - 1] - lista[0]





# def largest_different2(*lista):
#     if lista:
#         return max(lista) - min(lista)
#
#
# def test_largest_different():
#     assert  largest_different([3,2,4,1]) == 3
#     assert largest_different([]) == None
# def test_largest_different2():
#     assert  largest_different2(3,2,4,1) == 3
#     assert largest_different2() == None


# def div(a,b=2):
#
#     return a % b == 0
#
#
# def test_div():
#     assert div(10,5) is True
#     assert div(10,3) is False
#     assert div(10)  is True

board = [
    ["X", "O", "X"],
    ["", "", ""],
    ["O", "", ""]
]


# def get_row_col(position):
#     columnes = "ABC"
#     rows= "123"
#     col_n, row_n = list(position)
#
#     try:
#         return rows.index(row_n), columnes.index(col_n)
#     except:
#         return "poza planszą"
#
# def test_get_row_col():
#     assert get_row_col("A3") == (2,0)
#     assert get_row_col("D4") == "poza planszą"
# napis = "Kajak"
# len(napis)
# print(napis[:].lower())
# print(napis[(len(napis) -1) :  :-1] .lower())
import string

def palindrome(napis):
    napis = napis.lower()
    for s in string.punctuation + string.ascii_lowercase:
        napis = napis.replace(s,"")

    return napis[::-1] == napis.lower()

def test_palindroms():
    assert palindrome("Kajak") == True
    assert palindrome("A to idiota") == True
