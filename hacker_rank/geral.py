# ===============================================================================
def main(a, b, c, d):
    p = a ** b
    q = c ** d
    print(p + q)
# ===============================================================================

def print_statement():
    for i in range(1, int(input())):
        print(str(i) * i)
# ===============================================================================

def print_statement2():
    for i in range(1, int(input())):
        for _ in range(i):
            print(i, end="")
        print()

# ===============================================================================
def print_statement3():
    for i in range(1, int(input())):
        x = 10 ** i
        z = x // 9
        y = z * i
        print(f"i = {i}")
        print(f"10^i     = {x}")
        print(f"{x} // 9 = {y}")
        print(f"{y} * i  = {z}")
        print()
# ===============================================================================

def permutations(x, y, z, n):
    lista = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    lista.append([i, j, k])
                    # print(f"{i} {j} {k}")

    return lista

    # for i in range(x + 1):
        # lista.extend([i, j, k] for j, k in itertools.product(range(y + 1), range(z + 1)) if i + j + k != n)
# ===============================================================================


def list_comprehensions(x, y, z, n):
    lista = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(lista)
# ===============================================================================

def runner_up(n, array):
    x = sorted(set(array))
    return x[-2]

# ===============================================================================


# ===============================================================================


if __name__ == '__main__':
    
    # print_statement3()
    
    # a = int(input())
    # b = int(input())
    # c = int(input())
    # d = int(input())

    # print(permutations(a, b, c, d))
    # list_comprehensions(1, 1, 1, 2)
    
    # main(a, b, c, d)
    
    # n = int(input())
    # array = list(map(int, input().split()))
    # print(runner_up(n, array))
    
    # records = {{input(): float(input())} for _ in range(int(input()))}
    # records = {{input(): input()} for _ in range(int(input()))}
    
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # records = {**records, **{name: score}}          # Bem top
        records[name] = score

