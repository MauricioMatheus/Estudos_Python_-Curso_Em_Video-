'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

import random
matriz = [[], [], []]
pares = []
for i in range(0, 3):
    num0 = random.randint(1, 9)
    matriz[0].append(num0)
    if num0 % 2 == 0:
        pares.append(num0)
for i in range(0, 3):
    num1 = random.randint(1, 9)
    matriz[1].append(num1)
    if num1 % 2 == 0:
        pares.append(num1)
for i in range(0, 3):
    num2 = random.randint(1, 9)
    matriz[2].append(num2)
    if num2 % 2 == 0:
        pares.append(num2)

print(f'A matriz 3x3 é composta por: ', '\n', matriz[0], '\n', matriz[1], '\n', matriz[2], '\n')
print(f'Os números pares são: {pares}.', '\n')
print(f'A soma dos números pares é igual a {sum(pares)}.', '\n')
print(f'A soma dos elementos da terceira coluna é igual a {matriz[0][2] + matriz[1][2] + matriz[2][2]}.', '\n')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')


