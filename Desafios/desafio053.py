'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = input('Digite uma frase').strip().upper()
palavra = frase.split()
mistura = ''.join(palavra)
condition = bool
contrario = ''
for i in range(len(mistura)-1, -1, -1):
    contrario += mistura[i]
print(mistura)
print(contrario)
if contrario == mistura:
    print('Palíndromo!')
else:
    print('Não é um palíndromo.')
