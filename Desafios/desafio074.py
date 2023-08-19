'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random
num = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
       random.randint(1, 100), random.randint(1, 100))
maior = menor = 0
print(f'Os valores sorteados foram {num}')
'''for i in range(0, len(num)): #Desnecessário nas variáveis compostas
    if i == 0: #Definindo valores iniciais para o maior e menor
        maior = menor = num[i]
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]'''
print(f'O maior número sorteado foi {max(num)}, enquanto o menor foi {min(num)}.')