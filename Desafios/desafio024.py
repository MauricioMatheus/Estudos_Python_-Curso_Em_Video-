'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cidade = input('Digite o nome de uma cidade').strip()
cidade = cidade.title()
dividida = cidade.split(' ')
print(dividida)
print('Santo' in dividida[0])
