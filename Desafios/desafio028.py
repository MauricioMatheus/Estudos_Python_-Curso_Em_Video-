# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir
# qual foi o número escolhido pelo computador. - O programa deverá escrever na tela se o usúario venceu ou perdeu.

import random
num = int(random.randrange(1, 5))
print('E então, qual número eu escolhi?')
num_usuario = int(input('Tente advinhar...'))
if num_usuario == num:
    print('Parabéns! Você acertou!')
else:
    print(f'Que pena, você errou... O número que eu escolhi foi {num}.')
