# https://peps.python.org/pep-0008/#programming-recommendations

import timeit

# O último método not A é uma forma Pythonica recomendada por Recomendações de Programação no PEP8.
# Por padrão, seqüências e coleções vazias são avaliadas como False em um contexto Boolean.


# O not A é recomendado não só porque é Pythonic, mas também porque é o mais eficiente.


def main():  # sourcery skip: simplify-empty-collection-comparison
    A = ""
    print(A == "")
    # True

    print(A is "")
    # True

    print(A != "")
    # True

    print(not A)
    # True

    time_eq = timeit.timeit('A == ""', setup='A=""', number=10000000)
    print(f'Time (A == ""): {round(time_eq, 6)}')
    # output => 0.233691

    time_is = timeit.timeit('A is ""', setup='A=""', number=100000000)
    print(f'Time (A is ""): {round(time_is, 6)}')
    # output => 1.786247

    time_dif = timeit.timeit('A != ""', setup='A=""', number=100000000)
    print(f'Time (A != ""): {round(time_dif, 6)}')
    # output => 2.306655

    time_not = timeit.timeit("not A", setup='A=""', number=100000000)
    print(f"Time (not A)  : {round(time_not, 6)}")
    # output => 1.75003


if __name__ == "__main__":
    main()
