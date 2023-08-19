'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.'''

import random
#Uma lista para cada linha da matriz 3x3:
matriz = [[], [], []]
'''lista0 = []
lista1 = []
lista2 = []''' #Utilizadas no caso da não utilização de listas compostas
for i in range(0, 3): # Linha 0
    num0 = random.randint(1, 9)
    matriz[0].append(num0)
for i in range(0, 3): # Linha 1
    num1 = random.randint(1, 9)
    matriz[1].append(num1)
for i in range(0, 3): # Linha 2
    num2 = random.randint(1, 9)
    matriz[2].append(num2)

print('A matriz 3x3 é composta por:')
print('\n', matriz[0], '\n', matriz[1], '\n', matriz[2]) # Formatando a saída como uma matriz 3x3