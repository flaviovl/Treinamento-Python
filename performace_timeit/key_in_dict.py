# https://peps.python.org/pep-0008/#programming-recommendations

import timeit

dic = {"A" : 1, "B" : 2}

def key_in_dict(key, dicObj):
    if key in dicObj:
        print("Existing key")
    else:
        print("Not existing")


key_in_dict("A", dic)
key_in_dict("C", dic)


x = timeit.timeit('"A" in dic', setup='dic = {"A":1, "B":2}', number=1000000)
print(round(x, 4))
# 0.0283

y = timeit.timeit('"A" in dic.keys()', setup='dic = {"A":1, "B":2}', number=1000000)
print(round(y, 4))
# 0.0701


# Pode dar-lhe o mesmo resultado com a solução que acabámos de lhe mostrar. 
# Mas este método dicObj.keys() é aproximadamente quatro vezes mais lento porque
# leva tempo extra para converter as chaves do dicionário para uma lista.
