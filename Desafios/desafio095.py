''' Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

import random
time = []
jogador = {}
gols_partidas = []
partidas = []
condicao = ''

while True:
    jogador.clear()
    jogador['nome'] = input('Por favor, digite o nome do jogador').strip().title()
    quant_partidas = int(input('Por favor, digite a quantidade de partidas que ele jogou'))
    gols_partidas.clear()

    for i in range(0, quant_partidas): # Determinando a quantidade de gols por partida
        quant_gols = random.randint(1, 3)
        gols_partidas.append(quant_gols)

    jogador['gols'] = gols_partidas[:]
    jogador['total de gols'] = sum(gols_partidas)


    time.append(jogador.copy())



    condicao = input('Deseja acrescentar dados de mais um jogador? [S/N]').strip().upper()[0]
    if condicao not in 'SN':
        while condicao not in 'SN': #Impedindo erros de digitação do usuário
            print('Entrada inválida. Por favor, tente novamente.')
            condicao = input('Deseja acrescentar dados de mais um jogador? [S/N]').strip().upper()[0]
    if condicao == 'N':
        break


print('--'*30)

print('cod ', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end= '')
print() 

for k, v in enumerate (time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*30)

while True:
    busca = int(input('Deseja buscar dados de qual jogador? [999 para interromper]'))
    if busca == 999:
        break
    elif busca > len(time):
        print(f'Busca incorreta. Não existe jogador com o código {busca}')
    else:
        print(f'-- Dados do jogador {time[busca]["nome"]}: ')
        for i, j in enumerate (time[busca]['gols']):
            print(f'no jogo {i+1} fez {j} gols.')
        print('--'*40)

print('VOLTE SEMPRE!')

  

