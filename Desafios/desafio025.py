'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = input('Digite um nome completo').strip()
nome = nome.title()
dividido = nome.split()
print(f'O seu nome completo é {nome}, certo? \n Seu nome tem Silva? {"Silva" in dividido}')



