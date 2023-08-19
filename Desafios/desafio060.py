'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

num = int(input('Digite um número'))
cont = num
fatorial = 1
if num != 0:
    print(f'{num}! = {num}', end='')
if num == 0:
    fatorial = 1
else:
    while cont != 1:
        fatorial *= cont
        cont -= 1
        print(f'x{cont}', end='')
if num == 0:
    print(f'{num}! = {fatorial}.')
else:
    print(f' = {fatorial}.')
    