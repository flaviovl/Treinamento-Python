zero_list = [0, 0, 0, 0, 0]
number_list = [2, 1, 3, 8, 10, 11, 13]
string = "e necessario testar cada caracter da string para saber se tem um numero"

is_even = list(map(lambda x: x % 2 == 0, number_list))
is_odd = [x % 2 != 0 for x in number_list]

all_digit = [char.isdigit() for char in string]
all_alphabetic = list(map(lambda x: x.isalpha() or x.isspace(), string))

print(is_even)
print(is_odd)
print(all_digit)
print(all_alphabetic)

print(f"Are any of the elements even? {any(is_even)}")
print(f"Are all elements even? {all(is_even)}")

print(f"Are any of the elements odd? {any(is_odd)}")
print(f"Are all elements odd?? {all(is_odd)}")

print(all(number_list))
print(all(all_digit))
print(f"String contain only space and alphabets: {all(all_alphabetic)}")

# def list_zeros (zero_list): 
#     for i in zero_list:
#         if i == 0:
#             return True
#     return False
def list_zeros(zero_list):
    return any(i == 0 for i in zero_list)
