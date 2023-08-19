'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

import random
jogador = {}
gols_partidas = []
nome = input('Por favor, digite o nome do jogador').strip().title()
partidas = int(input('Por favor, digite a quantidade de partidas que ele jogou'))
jogador['Nome'] = nome
jogador['Partidas'] = partidas
for i in range(0, partidas): # Determinando a quantidade de gols por partida
    quant_gols = random.randint(1, 3)
    gols_partidas.append(quant_gols)
jogador['Quantidade de gols p/ partida'] = gols_partidas #Adicionando a lista ao dicionário
total_de_gols = sum(gols_partidas) #Determinando a soma de gols em todas as partidas
jogador['Total de gols'] = total_de_gols #Adicionando essa soma ao dicionário
print(jogador)

for k, v in jogador.items():
    if k == 'Nome':
        print(f'O {k} do jogador é {v}.', '\n')
    elif k == 'Quantidade de gols p/ partida':
        for i in range(0, len(gols_partidas)):
            print(f'Na {i+1}ª partida fez {gols_partidas[i]} gols.', '\n')
    else:
        print(f'{k}: {v}.', '\n')