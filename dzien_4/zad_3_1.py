def policz_znaki(napis, znakp="<", znakk=">"):
    wynik = 0
    poziom = 0
    for znak in napis:
        if znak == znakp:
            poziom += 1
        elif znak == znakk:
            poziom -= 1
        else:
            wynik += poziom

    return wynik


def test_policz_znaki():
    assert policz_znaki("ala ma <kota> a kot ma ale") == 4
    assert policz_znaki("a <a<a<a>>>") == 6
    assert policz_znaki("ala [kota [a kot]] ma [ala]", "[","]") ==18

