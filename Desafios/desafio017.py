'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

import math
c_oposto = float(input('Digite o comprimento do cateto oposto do triângulo'))
c_adjacente = float(input('Digite o comprimento do cateto adjacente do triângulo'))
hipotenusa = float(math.hypot(c_oposto, c_adjacente))
print(f'O comprimento da hipotenusa do triângulo retângulo é igual a {hipotenusa:.2f} m.')


