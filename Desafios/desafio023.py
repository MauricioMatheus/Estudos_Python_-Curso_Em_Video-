'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

num = int(input('Digite um número entre 0 e 9999'))
u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10
print(f' Unidade: {u} \n Dezena: {d} \n Centena: {c} \n Milhar: {m}')
