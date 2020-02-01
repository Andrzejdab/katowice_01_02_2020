zliczenie = {}
#tekst = input(print("podaj napis :"))
tekst = "0la ma kota"

# for znak in teks:
#     if znak in zliczenia;
#         zliczenia[znak] += 1
# else:
#     zliczenia[znak] = 1

# #  wer2
#
# for znak in tekst:
#     zliczenie[znak] = zliczenie.get(znak,0) + 1

#ver 3
from collections import defaultdict

zliczenie = defaultdict(int)
for znak in tekst.lower():
    zliczenie[znak] += 1
print(zliczenie)




