'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

import random
palpites = []
jogos = int(input('Quantos jogos você deseja fazer?'))
for i in range(1, jogos + 1):
    palpite = [] #Lista que contém o palpite
    cont = 0 #Contador de números por palpite
    while cont < 6:
        num = random.randint(1, 60)
        if num not in palpite: #Adicionando o número no palpite somente se ele ainda não tiver sido sorteado
            palpite.append(num)
            cont += 1
    palpites.append(palpite[:])
    print(f'Resultado do jogo {i}: {palpite}')
    palpite.clear()

