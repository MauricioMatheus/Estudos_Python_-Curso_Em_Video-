'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {'nome': input('Por favor, digite o nome do aluno'),
         'media': float(input('Por favor, digite a média do aluno'))}

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items(): #Mostrando tanto as keys quanto os values
    print(f'{k} é {v}.', '\n')
