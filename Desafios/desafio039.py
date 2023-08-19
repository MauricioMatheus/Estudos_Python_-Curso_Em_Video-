'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

import datetime
nascimento = int(input('Digite o ano de seu nascimento.'))
atual = datetime.date.today().year
idade = atual - nascimento
saldo = 18 - idade
genero = int(input('''Você é homem ou mulher?
Digite [ 1 ] caso seja homem
Digite [ 2 ] caso seja mulher'''))

if genero == 1:
    if idade < 18:
        print(f'Você ainda vai se alistar no serviço militar. Você tem {idade} anos em {atual} e faltam', end=' ')
        print(f'{18 - idade} anos até o seu alistamento.')
    elif idade > 18:
        print(f'Você já passou do tempo de alistamento. Você tem {idade} anos em {atual}.', end=' ')
        print(f'Seu alistamento foi em {atual + saldo}.')
    else:
        print(f'É hora de se alistar! Você tem {idade} anos em {atual}!')

elif genero == 2:
    print('No Brasil o alistamento militar feminino não é obrigatório!')
else:
    print('Opção inválida. Tente novamente.')
