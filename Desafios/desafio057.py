'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = input('Por favor, digite o seu gênero: [M/F]').strip().upper()[0]
while sexo not in 'MF':
    if sexo not in 'MF':
        sexo = input('Dados inválidos. Por favor, tente novamente.').strip().upper()[0]
if sexo == 'F':
    print('Sexo feminino registrado com sucesso.')
else:
    print('Sexo masculino registrado com sucesso.')
