'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = input('Digite um nome completo').strip()
nome = nome.title()
dividido = nome.split(' ')
print(dividido)
print(f' Prazer em te conhecer! \n O seu primeiro nome é {dividido[0]} e o último é {dividido[len(dividido)-1]}.')

print('_'.join(dividido)) #teste

