'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n = int(input('Por favor, digite um número inteiro'))
contador = 0
for i in range(1, n+1):
    if i == 1 or i == n:
        if n % i == 0:
            contador += 1
    elif i != 1 and i != n and n % i == 0:
        contador += 1
if contador == 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
