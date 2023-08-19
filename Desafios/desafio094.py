'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = {}
pessoas = [] #Lista de pessoas contendo os dicionários com dados de cada uma.
mulheres = []
acima_media_idades = []
cont = 0 #Contador de pessoas
while True:
    nome = input('Por favor, digite o seu nome').strip().title()
    sexo = input('Por favor, digite o seu sexo [Masculino/Feminino]').strip().upper()[0]
    if sexo not in 'MF': #Evitando opções inválidas do usuário
        while sexo not in 'MF':
            print('Opção inválida. Por favor, tente novamente.')
            sexo = input('Por favor, digite o seu sexo [Masculino/Feminino]').strip().upper()[0]
    idade = int(input('Por favor, digite a sua idade'))
    dados['Nome'] = nome
    dados['Sexo'] = sexo
    dados['Idade'] = idade
    pessoas.append(dados.copy())
    cont += 1
    decisao = input('Deseja adicionar dados de mais uma pessoa? [Sim/Não]').strip().upper()[0]
    if decisao not in 'S/N': #Evitando opções inválidas do usuário
        while decisao not in 'S/N':
            print('Decisão inválida. Por favor, tente novamente.')
            decisao = input('Deseja adicionar dados de mais uma pessoa? [Sim/Não]').strip().upper()[0]
    print('=-'*30)
    if decisao == 'N':
        break
for i in range(0, len(pessoas)): #Criando uma lista só com mulheres
    if pessoas[i]['Sexo'] == 'F':
        mulheres.append(pessoas[i])

soma_idades = 0 #Para o cálculo da média idades
for i in range(0, len(pessoas)):
    soma_idades += pessoas[i]['Idade']
media_idades = soma_idades/cont

for i in range(0, len(pessoas)):
    if pessoas[i]['Idade'] > media_idades:
        acima_media_idades.append(pessoas[i])
print(f'{cont} pessoas foram cadastradas.', '\n')
print(f'A média de idades do grupo é {media_idades:.2f}', '\n')
print(f'A lista composta por mulheres: {mulheres}')
print(f'A lista composta por pessoas mais velhas que a media de idades: {acima_media_idades}')






