# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# -----------------------------------------------------
# URI - 1001
# -----------------------------------------------------
A = int(input())
B = int(input())
X = A + B
print(f"X = {X}")

# -----------------------------------------------------
# URI - 1002
# -----------------------------------------------------

pi = 3.14159
a = float(input())
A = pi * a ** 2
print('A = {:.4f}'.format(A))
print(f"A = {A:.4f}")

# URI - 1003
# -----------------------------------------------------

a = int(input())
b = int(input())
soma = a + b
print(f"SOMA = {soma}")

# URI - 1004
# -----------------------------------------------------

a = int(input())
b = int(input())
prod = a * b
print(f"PROD = {prod}")

# URI - 1005
# -----------------------------------------------------

p1 = 3.5
p2 = 7.5
a = float(input())
b = float(input())
m = ((a * p1) + (b * p2)) / 11
print('MEDIA = {:.5f}'.format(m))

# URI - 1006
# -----------------------------------------------------

p1 = 2
p2 = 3
p3 = 5

a = float(input())
b = float(input())
c = float(input())

m = ((a * p1) + (b * p2) + (c * p3)) / 10
print('MEDIA = {:.1f}'.format(m))

# URI - 1007
# -----------------------------------------------------

a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = (a * b) - (c * d)
print(f'DIFERENCA = {x}')

# URI - 1008
# -----------------------------------------------------

a = int(input())
b = int(input())
c = float(input())

x = b * c

print(f'NUMBER = {a}')
print('SALARY = U$ {:.2f}'.format(x))

# URI - 1009
# -----------------------------------------------------

nome = input()
a = float(input())
b = float(input())
x = a + (b * 0.15)

print('TOTAL = R$ {:.2f}'.format(x))

# URI - 1010
# -----------------------------------------------------

la = input().split()
lb = input().split()

a = int(la[1]) * float(la[2])
b = int(lb[1]) * float(lb[2])

print('VALOR A PAGAR: R$ {:.2f}'.format(a + b))

# URI 1011
# -----------------------------------------------------

pi = 3.14159
raio = float(input())
volume = 4 / 3 * pi * raio ** 3

print('VOLUME = {:.3f}'.format(volume))

# URI 1012
# -----------------------------------------------------

pi = 3.14159
a, b, c, d = input().split(" ")

areaTriangulo = float(a) * float(c) / 2
areaCirculo = pi * float(c) ** 2
areaTrapezio = (float(a) + float(b)) * float(c) / 2
areaQuadrado = float(b) ** 2
areaRetangulo = float(a) * float(b)

print('TRIANGULO: {:.3f}\n'.format(areaTriangulo) +
      'CIRCULO: {:.3f}\n'.format(areaCirculo) +
      'TRAPEZIO: {:.3f}\n'.format(areaTrapezio) +
      'QUADRADO: {:.3f}\n'.format(areaQuadrado) +
      'RETANGULO: {:.3f}'.format(areaRetangulo))

# URI 1013
# -----------------------------------------------------

a, b, c = input().split(" ")

m2 = (int(a) + int(b) + abs(int(a) - int(b))) / 2
m2 = (int(c) + m2 + abs(int(c) - m2)) / 2

print(f'{int(m2)} eh o maior')

# URI 1014
# -----------------------------------------------------

distancia = int(input())
combustivel = float(input())

print('{:.3f} km/l'.format(distancia / combustivel))

# URI 1015
# -----------------------------------------------------

x1, y1 = input().split(" ")
x2, y2 = input().split(" ")

distancia = ((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2) ** (1 / 2)

print('{:.4f}'.format(distancia))

# URI 1016
# -----------------------------------------------------

distancia = int(input())
print(f'{distancia * 2} minutos')

# URI 1017
# -----------------------------------------------------

consumoLitro = 12
tempo = int(input())
velocidadeMedia = int(input())

distancia = tempo * velocidadeMedia
consumoViagem = distancia / consumoLitro

print('{:.3f}'.format(consumoViagem))

# URI 1018
# -----------------------------------------------------

valor = int(input())

print(f'{valor}')
if valor >= 100:
    notas100 = valor // 100
    valor -= notas100 * 100
else:
    notas100 = 0

if valor >= 50:
    notas50 = valor // 50
    valor -= notas50 * 50
else:
    notas50 = 0

if valor >= 20:
    notas20 = valor // 20
    valor -= notas20 * 20
else:
    notas20 = 0

if valor >= 10:
    notas10 = valor // 10
    valor -= notas10 * 10
else:
    notas10 = 0

if valor >= 5:
    notas5 = valor // 5
    valor -= notas5 * 5
else:
    notas5 = 0

if valor >= 2:
    notas2 = valor // 2
    valor -= notas2 * 2
else:
    notas2 = 0

notas1 = valor

print(('{} nota(s) de R$ 100,00\n'.format(notas100) + '{} nota(s) de R$ 50,00\n'.format(notas50) + '{} nota(s) de R$ 20,00\n'.format(notas20) + '{} nota(s) de R$ 10,00\n'.format(notas10) + '{} nota(s) de R$ 5,00\n'.format(notas5) + '{} nota(s) de R$ 2,00\n'.format(notas2) + f'{notas1} nota(s) de R$ 1,00'))


# URI 1019
# -----------------------------------------------------

tempoSeg = int(input())

hora = int(tempoSeg // 3600)
min = int(tempoSeg % 60 - (hora * 60))
seg = int(tempoSeg % 60)

print(f'{hora}:{min}:{seg}')

# URI 1020
# -----------------------------------------------------

nDias = int(input())

ano = nDias // 365
mes = (nDias % 365) / 30
dia = (mes - int(mes)) * 30

print(('{} ano(s)\n'.format(ano) + '{} mes(es)\n'.format(int(mes)) + f'{int(dia)} dia(s)'))


# URI 1021
# -----------------------------------------------------

valor = eval(input())
valor = float("%.2f" % valor)

c100 = valor // 100
resto = valor - c100 * 100

c50 = resto // 50
resto -= c50 * 50

c20 = resto // 20
resto -= c20 * 20

c10 = resto // 10
resto -= c10 * 10

c5 = resto // 5
resto -= c5 * 5

c2 = resto // 2
resto -= c2 * 2
resto = float("%.2f" % resto)

# -----------------------------------
resto *= 100
m100 = int(resto // 100)
resto -= m100 * 100
m50 = resto // 50
resto -= m50 * 50
m25 = resto // 25
resto -= m25 * 25
m10 = resto // 10
resto -= m10 * 10
m5 = resto // 5
resto -= m5 * 5
m1 = resto
# -----------------------------------
print('NOTAS:')
print(('{} nota(s) de R$ 100.00\n'.format(int(c100)) + '{} nota(s) de R$ 50.00\n'.format(int(c50)) + '{} nota(s) de R$ 20.00\n'.format(int(c20)) + '{} nota(s) de R$ 10.00\n'.format(int(c10)) + '{} nota(s) de R$ 5.00\n'.format(int(c5)) + f'{int(c2)} nota(s) de R$ 2.00'))


print('MOEDAS:')
print((('{} moeda(s) de R$ 1.00\n'.format(m100) + '{} moeda(s) de R$ 0.50\n'.format(int(m50))) + '{} moeda(s) de R$ 0.25\n'.format(int(m25)) + '{} moeda(s) de R$ 0.10\n'.format(int(m10)) + '{} moeda(s) de R$ 0.05\n'.format(int(m5)) + f'{m1} moeda(s) de R$ 0.01'))


# URI 1022
# -----------------------------------------------------

li = input().split()
a, b, c, d = li

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (a % 2 == 0) and (c and b > 0):
    if b > c & d > a and c + d > a + b:
        print("Valores aceitos")
else:
    print("Valores nao aceitos")

    # URI 1035
    # -----------------------------------------------------

    li = [int(i) for i in input().split()]
    a, b, c, d = li

    if (a % 2 == 0) and (c > 0 and d > 0) and (b > c and d > a) and (c + b > a + b):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")


# URI 1036 - sem math e com com funÃ§Ã£o
# -----------------------------------------------------

def main():
    li = [float(i) for i in input().split(" ")]
    a, b, c = li

    x1, x2 = baskara(a, b, c)

    if x1 and x2:
        print("Impossivel calcular")
    else:
        print('R1 = {:.5f}'.format(x1))
        print('R2 = {:.5f}'.format(x2))


# -----------------------------------------------------
def baskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if a != 0:
        if delta > 0:
            return deltaMaior(a, b, delta)

        if delta == 0:
            return deltaIgual(a, b)

    return True, True


# -----------------------------------------------------
def deltaMaior(a, b, delta):
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    return x1, x2


# -----------------------------------------------------
def deltaIgual(a, b):
    x = -b / (2 * a)
    return x, x


# -----------------------------------------------------
if __name__ == '__main__':
    main()

# URI 1037
# -----------------------------------------------------

a = float(input())

if (a >= 0 and a <= 25):
    print('Intervalo [0,25]')
elif (a > 25 and a <= 50):
    print("Intervalo (25,50]")
elif (a > 50 and a <= 75):
    print('Intervalo (50,75]')
elif (a > 75 and a <= 100):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')


# URI 1038
# -----------------------------------------------------

def main():
    cod, qtd = map(int, input().split())
    valor = codValor(cod)
    total = qtd * valor
    print('Total: R$ {:.2f}'.format(total))


# -----------------------------------------------------
def codValor(cod):
    switcher = {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50,
    }
    return switcher.get(cod, "Nao encontradado")


# -----------------------------------------------------
if __name__ == '__main__':
    main()
