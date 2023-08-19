'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math
angulo = int(input('Digite um ângulo'))
sen = float(math.sin(math.radians(angulo)))
cos = float(math.cos(math.radians(angulo)))
tg = float(math.tan(math.radians(angulo)))
print(f'O ângulo {angulo}° tem como: \n seno = {sen:.2f} \n cosseno = {cos:.2f} \n tangente = {tg:.2f}')
