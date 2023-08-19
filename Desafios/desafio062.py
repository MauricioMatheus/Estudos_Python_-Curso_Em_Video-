'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Digite o primeiro termo da PA.'))
razao = int(input('Digite a razão da PA'))
termo = primeiro
i = 1
termos = 11
print(f'Os termos da PA são: ', end='')
while i < termos:
    print(termo, end=', ')
    termo += razao
    i += 1
    if i == termos: #Fim da PA
        print('PAUSA.')
    if i == termos: #Perguntando ao usuário se ele deseja ver mais algum termo
        decisao = input('Deseja ver mais alguns termos? [Sim/Não]').strip().upper()[0]
        if decisao not in 'SN': #Evitando digitações erradas do usuário
            while decisao not in 'SN':
                decisao = input('''Opção inválida, tente novamente. 
                Deseja ver mais algum termo? [Sim/Não]''').strip().upper()[0]
        if decisao == 'S': #Opção 1: Usuário deseja ver mais termos na PA
            adicionais = int(input('Quantos termos você deseja adicionar?'))
            termos = termos + adicionais
        elif decisao == 'N': #Opção 2: O usuário deseja encerrar o programa.
            break

print('FIM DO PROGRAMA.')
