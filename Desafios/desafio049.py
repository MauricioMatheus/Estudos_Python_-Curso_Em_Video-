'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Por favor, digite um número inteiro'))
print(f'A tabuada de {n} é:')
for i in range(1, 11, 1):
    print(f'{n} x {i} = {n*i}')
