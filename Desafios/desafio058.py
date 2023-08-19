'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random
print('Vamos jogar um joguinho!')
computador = random.randint(1, 10)
cont = 0
print('Pronto, já escolhi meu número de 1 a 10! Será que você consegue adivinhar qual eu escolhi? hahaha')
num = -1
while num != computador:
    num = int(input('Digite um número de 1 a 10'))
    cont += 1
    if num != computador:
        print('Haa! Eu ganhei, tente novamente!')
if num == computador:
    print(f'Parabéns! Com {cont} tentativa(s) você conseguiu adivinhar o número que eu escolhi que foi', end=' ')
    print(f'{computador}! Não perderei na próxima vez!')
