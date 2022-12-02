def index(seq, target):
    found = False
    for uuid, val in enumerate(seq):
        if val == target:
            found = True
            break
    if not found:
        raise ValueError(f"{target} is not in the sequence")

    return uuid


def index2(seq, target):
    for id, val in enumerate(seq):
        if val == target:
            return id
    raise ValueError(f"{target} is not in the sequence")


def index3(seq, target):
    if found := next((True for val in seq if val == target), False):
        return idx
    else:
        raise ValueError(f"{target} is not in the sequence")


if __name__ == "__main__":

    lista = [1, 2, 3, 4, 5, 6]
    key = 8

    idx = index(lista, key)
    print(idx)

    idx2 = index(lista, key)
    print(idx2)

    idx3 = index(lista, key)
    print(idx3)
