'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
cont = 0
for i in range(1, 7):
    n = int(input('Por favor, digite um número inteiro'))
    if n % 2 == 0:
        soma += n
        cont += 1
    else:
        continue
print(f'A soma dos {cont} números pares que você informou é de {soma}.')
