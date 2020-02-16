
def capital_index(tekst):
    tab =[]
    for i in range(len(tekst)):
        if tekst[i].isupper():
           tab.append(i)
    return tab

a= capital_index("HellOW")
print(a)