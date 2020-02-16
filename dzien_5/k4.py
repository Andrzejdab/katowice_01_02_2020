def double_letters(tekst):

    for i in range(len(tekst) -1):
        if tekst[i] == tekst[i+1]:
            return  True
        else: return False


tekst = "Alla"

print(double_letters(tekst))
