''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

brasileirao_2022 = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athlético-PR',
                    'Atlético Mineiro', 'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 'Goiás', 'São Paulo',
                    'Bragantino', 'Coritiba', 'Ceará', 'Cuiabá', 'Avaí', 'Atlético Goianiense', 'Juventude')

print('Os cinco primeiros colocados da tabela são:')
print(brasileirao_2022[0:5])
print('~~'*40)
print('Os quatro últimos colocados da tabela são:')
print(brasileirao_2022[-4:])
print('~~'*40)
print(f'Lista dos times em ordem alfabética: {sorted(brasileirao_2022)}.')
print(f'Palmeiras está na {brasileirao_2022.index("Palmeiras")+1}ª posição.')
