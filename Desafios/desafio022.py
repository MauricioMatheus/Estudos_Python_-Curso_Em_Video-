'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Digite o seu nome completo').strip()
# espacos = int(nome.count(' '))
separa = nome.split(' ')
print(f'Seu nome com todas as letras maiúsculas:  {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas:  {nome.lower()}')
print(f'Seu nome completo possui {len(nome)-nome.count(" ")} letras.')
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')


