# "is" vs "=="

a = [1, 2, 3]
b = a

print(id(a), id(b))

id(a) == id(b)         # output: True
a is b                 # output: True
a == b                 # output: True

c = list(a)
print(f'id: {id(a)} -> value: {a}\nid: {id(b)} -> value: {b}\nid: {id(c)} -> value: {c}')

id(a) == id(c)         # output: False
a is c                 # output: False
a == c                 # output: True

c.append(4)
print(f' {a}\n {b}\n {c}')

a.append(5)
print(f' {a}\n {b}\n {c}')


"is" -> As expressões são avaliadas como "True" se as duas variáveis apontam para o mesmo objeto
"==" -> É avaliado como "True" se os objetos referidos pelas variáveis são iguais

