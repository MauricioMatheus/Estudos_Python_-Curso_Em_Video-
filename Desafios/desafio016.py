'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

import math
n = float(input('Digite um número'))
ni = math.trunc(n)
print(f'A porção inteira de {n} é {ni}.')

