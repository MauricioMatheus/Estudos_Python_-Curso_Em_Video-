'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

import random
cont_vitorias = 0
while True: #Estrutura de repetição que só irá parar quando o usuário perder
    escolha = input('Você escolhe par ou ímpar?').strip().upper()[0]
    if escolha not in 'PI':  # Evitando erros de digitação do usuário
        while escolha not in 'PIÍ':
            escolha = input('Opção inválida. Por favor, escolha se você deseja par ou ímpar').strip().upper()[0]
    if escolha == 'P':  # Caso o usuário escolha Par
        escolha_computador = 'I'
        print('Ok, então eu escolho ímpar!'.upper())
    elif escolha in 'ÍI':  # Caso o usuário escolha Ímpar
        escolha_computador = 'P'
        print('Ok, então eu escolho Par!'.upper())
    num = int(input('Escolha um número inteiro!'))
    num_computador = random.randint(1, 10)
    total = num + num_computador
    print(f'Você jogou {num}, eu joguei {num_computador} e o total foi {total}.')
    print('~~'*30)
    if total % 2 == 0 and escolha == 'P': #Condição 1 de vitória do usuário
        print(f'Droga! Eu escolhi o número {num_computador}, e o total {total} é par, então você venceu!!!')
        print('~~'*30)
        cont_vitorias += 1
    elif total % 2 != 0 and escolha in 'IÍ': #Condição 2 de vitória do usuário
        print(f'Droga! Eu escolhi o número {num_computador}, e o total {total} é ímpar, então você venceu!!!')
        print('~~' * 30)
        cont_vitorias += 1
    elif total % 2 == 0 and escolha in 'IÍ': #Condição 1 de vitória do computador
        print(f'Eu venci!!! Eu escolhi o número {num_computador}, então o total deu {total} e eu escolhi ímpar!!!')
        print('~~' * 30)
        break
    elif total % 2 != 0 and escolha == 'P': #Condição 2 de vitória do computador
        print(f'Eu venci!!! Eu escolhi o número {num_computador}, então o total deu {total} e eu escolhi par!!!')
        print('~~' * 30)
        break
print(f'FIM DE JOGO! VOCÊ CONSEGUIU ME VENCER {cont_vitorias} VEZES!')
