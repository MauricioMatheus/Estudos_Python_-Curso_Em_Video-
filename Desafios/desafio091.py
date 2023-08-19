'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

import random
from operator import itemgetter

# Solução utilizando dicionário de listas:
'''jogo = {'jogador': [], 'resultado': []}
for i in range(0, 4):
    nome = input('Por favor, digite o seu nome.')
    jogo['jogador'].append(nome)
    jogo['resultado'].append(random.randint(1, 6))
print(jogo) 
'''

#Solução "correta" com o intuito de utilizar o operator.itemgetter para ordenar os itens do dicionário
jogo = {'jogador1': random.randint(1, 6),
        'jogador2': random.randint(1, 6),
        'jogador3': random.randint(1, 6),
        'jogador4': random.randint(1, 6)}
print(jogo)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Itemgetter(0) para keys, e (1) para valores.
print('\n')
for i, v in enumerate(ranking): #Tratando a saída como lista
    print(f'{i+1}º lugar tirou {v} no dado')




#Solução utilizando dicionários dentro de uma lista:

'''jogo = []
for i in range(0, 4):
    jogadores = {'nome': input('Por favor, digite o seu nome'), 'resultado': random.randint(1, 6)}
    jogo.append(jogadores.copy())
print(jogo)
print(jogo.sort())'''