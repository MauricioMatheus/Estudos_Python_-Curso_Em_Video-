'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

primeiro = int(input('Digite o primeiro termo da PA.'))
razao = int(input('Digite a razão da PA'))
termo = primeiro
i = 1
print(f'Os termos da PA são: ', end='')
while i < 11:
    print(termo, end=', ')
    termo += razao
    i += 1
print('FIM.')
