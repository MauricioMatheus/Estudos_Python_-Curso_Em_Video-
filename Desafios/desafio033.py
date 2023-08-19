# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um número inteiro.'))
num2 = int(input('Digite outro número inteiro.'))
num3 = int(input('Digite mais um número inteiro.'))

# Determinando o maior número:
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

# Determinando o menor número:
menor = num2

if num3 < num1 and num3 < num2:
    menor = num3
if num1 < num2 and num1 < num3:
    menor = num1

print(f'O menor número é {menor} e o maior número é {maior}.')

