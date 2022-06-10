from heapq import merge
from itertools import chain

"""
Dada as sequências:

a = [1, 2, 3, 4]
b = [1, 3, 4, 5 , 6, 7]
c = [3, 6, 8, 9 ,10]

Como você pode gerar uma sequencia:
1. elementos únicos
2. respeitando a ordem
3. com espaço de memoria constante
4. tempo de execução linear
"""
def build_sequence(a, b, c):
    # full_list = a + b + c              # mais rápidp
    # full_list = list(chain(a, b, c))   # mais lento
    # full_list = [*a, *b, *c]             # quase o mais rápido (porém é mais bonito)
    
    # unique_list_ordered = list(dict.fromkeys(*a, *b, *c))
    
    # unique_list_ordered = list(set(*a, *b, *c))
    unique_list_ordered = list({*a, *b, *c})

    return unique_list_ordered

# =======================================================================================
def unique(*args):
    values, previous = merge(a, b, c), merge(*args)
    yield next(values)
    yield from(v for v, p in zip(values, previous) if v != p)

# =======================================================================================
def build_sequence2(a, b, c):
    return list(unique(a, b, c)) 



# =======================================================================================
# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, *args, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*args)

    if out == expected:
        sign = '\n✅'
        info = ''
    else:
        sign = '\n❌'
        info = f'\n\tcorreto é: {expected!r}'

    print(f'{sign} {f.__name__}{args!r} \n\tretornou : {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    a = [1, 2, 3, 4]
    b = [1, 3, 4, 5 , 6, 7]
    c = [3, 6, 8, 9, 10]
    
    d = [2, 1, 3, 4]
    e = [7, 3, 5, 4 , 6, 1]
    f = [8, 10, 3, 9, 6]

    expec = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
    
    print("=" * 80)
    test(build_sequence, c, b, a, expected=expec)
    print("=" * 80)
    test(build_sequence2, c, b, a, expected=expec)
    print("=" * 80)
    print("=" * 80)
    test(build_sequence, d, e, f, expected=expec)
    print("=" * 80)
    test(build_sequence2, d, e, f, expected=expec)
    print("=" * 80)
