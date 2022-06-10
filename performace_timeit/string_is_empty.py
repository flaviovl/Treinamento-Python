# https://peps.python.org/pep-0008/#programming-recommendations

import timeit

A = ""
A == ""
# True

A is ""
# True

not A
# True

# O último método not A é uma forma Pythonica recomendada por Recomendações de Programação no PEP8.
# Por padrão, seqüências e coleções vazias são avaliadas como False em um contexto Boolean.


# O not A é recomendado não só porque é Pythonic, mas também porque é o mais eficiente.

timeit.timeit('A == ""', setup='A=""', number=10000000)

timeit.timeit('A is ""', setup='A=""', number=10000000)

timeit.timeit('not A', setup='A=""', number=10000000)
