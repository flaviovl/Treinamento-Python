"""Inverter uma lista
"""
# ----------------------------------------------------------------------------------------------------------
def reverse_list(lst):
    print(len(lst))

    # for index in range(len(lst)):
    #     lst[index] = lst[-1-index]

    for index in range(len(lst) // 2):
        print(lst[index], lst[-1 - index])
        lst[index], lst[-1 - index] = lst[-1 - index], lst[index]
        print(lst[index], lst[-1 - index])

    return lst


# ----------------------------------------------------------------------------------------------------------
def reverse_list0(lst):
    return lst[::-1]


# ----------------------------------------------------------------------------------------------------------
def reverse_list_1(lst):
    mid = len(lst) // 2
    print(f"mid = {mid}")

    before_middle = lst[:mid]
    after_middle = lst[mid:]
    reverse = lst[::-1]
    reverse2 = lst[::-2]

    print(f"before_middle = {before_middle}")
    print(f"after_middle  = {after_middle}")
    print(f"reverse  = {reverse}")
    print(f"reverse2 = {reverse2}")

    aux = list(lst[::-1])
    aux2 = [value for value in lst[::-1]]

    return aux2


# -------------------------------------------------------------------------------------------------


def test(func, *args, expected):
    correct = "✅- "
    wrong = f"❌-\n\t correto é: {expected!r}"

    output = func(*args)
    value = correct if output == expected else wrong
    sign, info = value.split("-")

    print("=" * 80)
    print(f"\n{sign} => {func.__name__}{args!r} \n\tretornou : {output!r} {info}\n")
    print("=" * 80)


if __name__ == "__main__":
    lst = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]

    test(reverse_list, lst, expected=expected)
