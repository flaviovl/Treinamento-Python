"""
    "is" vs "=="
    "is" -> As expressões são avaliadas como "True" se as duas variáveis apontam para o mesmo objeto()
    "==" -> É avaliado como "True" se os objetos referidos pelas variáveis são iguais
"""

a = [1, 2, 3]
b = a  # b = recebe a mesma referencia de a (a e b aponta para o mesmo objeto)

print(id(a), id(b))

print(id(a) == id(b))  # output: True
print(a is b)  # output: True
print(a == b)  # output: True

c = list(a)  # c = nova lista(objeto) cópia da lista a
print(
    f"id: {id(a)} ->  value: {a}\n id: {id(b)} -> value: {b}\n id: {id(c)} -> value: {c}"
)

x = id(a) == id(c)  # output: False
a is c  # output: False
a == c  # output: True

c.append(4)
print(f" {a}\n {b}\n {c}")

a.append(5)
print(f" {a}\n {b}\n {c}")
