'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

n = int(input('Digite um número inteiro.'))
t1 = 0
t2 = 1
t3 = t1 + t2
i = 0
print(f'{t1} → {t2}', end=' → ')
while i < n - 2:
    print(t3, end=' → ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    i += 1
print('Fim do programa.')
