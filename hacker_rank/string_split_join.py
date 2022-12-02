
def split_join_str(line: str):
    string = line.split(" ")
    print(line)
    print(string)
    b = "-".join(string)
    print(b)

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

def change_value_string(string: str):
    base = list(string)
    base[-1] = "o"
    string = "".join(base)
    print(string)

def mutate_string(string, position, character):
    base = list(string)
    base[position] = character

    return "".join(base)


if __name__ == "__main__":
    
    # first_name = input()
    # last_name = input()
    # print_full_name(first_name, last_name)
    
    string = input()
    position, character = input().split()
    
    string_new = mutate_string(string, int(position), character)
    print(string_new)

