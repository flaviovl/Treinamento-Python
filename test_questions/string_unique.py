"""
    Dado um string S, retorne True se todos os caracters forem
    únicos e False caso exista algum duplicado.
    Valores em minúsculo e maiúsculo são considerados os mesmos.
    Ex:
        >> is_unique("flavio ")
        True
        >> is_unique("vieira")
        False
"""
import sys
from collections import OrderedDict

# =======================================================================================

def is_unique_0(string: str) -> bool:
    count = 0
    for index, char in enumerate(string):
        for other_char in string[index + 1:]:
            if char == other_char:
                return False
            count += 1
    print(f"is_unique_0 - count: {count}")
    return True

# =======================================================================================

def is_unique_1(string: str) -> bool:
    return all(char not in string[index + 1:] for index, char in enumerate(string))

# =======================================================================================

def is_unique_2(string: str) -> bool:
    count = 0
    for index, char in enumerate(string):
        if char in string[index + 1:]:
            return False
        count += 1
    print(f"is_unique_2 -  count: {count}")
    return True

# =======================================================================================
def is_unique_3(string: str) -> bool:
    char_seen = {}

    for count, char in enumerate(string, start=1):
        if char_seen.get(char):
            return False
        char_seen[char] = True
    print(f"is_unique_3 - count: {count}")
    return True

# =======================================================================================
# bin(1 << 128)
# bin(1 << 4)
# ord("f")    # 102
# ord("l")    # 108    
# ord("a")    # 97
# ord("v")    # 118        
# ord("i")    # 105    
# ord("o")    # 111

# string = "flavio"
# char = "f"
# print(bytearray(char, "utf-8"))

# binary_converted = ' '.join(format(c, 'b') for c in bytearray(string, "utf-8"))
# print("The Binary Represntation is:", binary_converted)


# =======================================================================================
def is_unique_4(string: str) -> bool:
    # str_unique = list(OrderedDict.fromkeys(string))   # mantem a ordem 
    # str_unique = list(dict.fromkeys(string))          # mantem a ordem 
    str_unique = set(string)                            # não mantem a ordem

    print(len(string), string)
    print(len(str_unique), str_unique)

    return True if len(str_unique) == len(string) else False
# =======================================================================================

if __name__ == "__main__":
    try:
        string = sys.argv[1]
    except IndexError:
        string = "flavio"
    
    # print(f"is_unique_0({string}) -> ", is_unique_0(string))
    # print(f"is_unique_1({string}) -> ", is_unique_1(string))
    # print(f"is_unique_2({string}) -> ", is_unique_2(string))
    # print(f"is_unique_3({string}) -> ", is_unique_3(string))
    print(f"is_unique_4({string}) -> ", is_unique_4(string))
