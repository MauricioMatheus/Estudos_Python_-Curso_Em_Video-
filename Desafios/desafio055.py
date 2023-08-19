'''Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''

menor_peso = 0
maior_peso = 0
for i in range(1, 6):
    peso = float(input('Por favor, digite o seu peso em kg.'))
    if i == 1: #Introduzindo o maior e o menor peso
        menor_peso = peso
        maior_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
        else:
            continue
print(f'Dessas cinco pessoas, {maior_peso} kg foi o maior peso, enquanto {menor_peso} kg foi o menor.')

