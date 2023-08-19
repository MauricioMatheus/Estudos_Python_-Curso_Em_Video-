'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0
print('A soma dos números ímpares múltiplos de 3 entre 1 e 500 é:')
for i in range(0, 501, 1):
    if i % 3 == 0 and i % 2 != 0 and i != 501:
        soma += i
        cont += 1
        print(i, end=', ')
    if i % 3 == 0 and i % 2 != 0 and i == 501:
        soma += i
        cont += 1
        print(f'{i}.')
print('\n' f'A soma dos {cont} números é igual a {soma}.')
