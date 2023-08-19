'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

print('Todos os números pares entre 1 e 50 são:')
for i in range(0, 51, 2):
    if i != 0 and i != 50:
        print(i, end=', ')
    if i == 50:
        print(f'{i}.')
