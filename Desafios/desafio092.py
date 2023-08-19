''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

import datetime

trabalhador = {}

#Lendo os dados
nome = input('Por favor, digite o seu nome').strip().title()
nascimento = int(input('Por favor, digite o ano de seu nascimento'))
CTPS = int(input('Por favor, insira os digitos da sua carteira de trabalho [Digite 0 caso não tenha]'))
ano_atual = datetime.date.today().year

#Introduzindo os dados no dicionário
trabalhador['Nome'] = nome
trabalhador['Idade'] = ano_atual - nascimento
trabalhador['CTPS'] = CTPS
if CTPS != 0: #Caso o usuário possua carteira de trabalho
    trabalhador['Ano de contratação'] = int(input('Por favor, digite o ano de sua contratação'))
    trabalhador['Salário'] = float(input('Por favor, digite o valor de seu salário'))
    trabalhador['Aposentadoria'] = trabalhador['Ano de contratação'] - nascimento + 35
    for k, v in trabalhador.items():
        if k == 'Aposentadoria':
            print(f'{k}: {v} anos de idade.')
        if k != 'Salário' and k != 'Aposentadoria':
            print(f'{k}: {v}.', '\n')
        elif k == 'Salário':
            print(f'{k}: R${v:.2f}', '\n')
else:
    print('Não possui carteira de trabalho.', '\n')
    trabalhador['CTPS'] = 'Não tem'
    for k, v in trabalhador.items():
        print(f'{k}: {v}.', '\n')

