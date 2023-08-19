'''Crie um programa que faça o computador jogar Jokenpô com você.'''

import random
num = random.randint(1, 3)

if num == 1:
    comp = 'Pedra'
elif num == 2:
    comp = 'Tesoura'
else:
    comp = 'Papel'

print('Vamos jogar Jokenpo! Faça a sua escolha!')
usuario = int(input('Digite 1 para escolher pedra, 2 para tesoura ou 3 para papel.'))

print('O que será que eu escolhi? hahaha')

if usuario == num:  #Empate
    print(f'Droga, empatamos! Eu escolhi {comp}!')

#Vitórias do computador
elif usuario == 3 and num == 2:
    print(f'HAHAHA eu ganhei! Eu escolhi {comp}!')
elif usuario == 2 and num == 1:
    print(f'HAHAHA eu ganhei! Eu escolhi {comp}!')
elif usuario == 1 and num == 3:
    print(f'HAHAHA eu ganhei! Eu escolhi {comp}!')

#Vitórias do usuário
elif usuario == 2 and num == 3:
    print(f'Droga, você ganhou de mim!!! Eu escolhi {comp}!')
elif usuario == 1 and num == 2:
    print(f'Droga, você ganhou de mim!!! Eu escolhi {comp}!')
elif usuario == 3 and num == 1:
    print(f'Droga, você ganhou de mim!!! Eu escolhi {comp}!')
