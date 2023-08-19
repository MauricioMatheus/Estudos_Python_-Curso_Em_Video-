'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

import random
values = []
even_values = []
odd_values = []
for i in range(0, 30):
    number = random.randint(1, 99)
    values.append(number)
for i in range(len(values)):
    if values[i] % 2 == 0:
        even_values.append(values[i])
    else:
        odd_values.append(values[i])
print(f'The main list is made by: {values}.')
print('~~'*60)
print(f"The even numbers' list is made by: {even_values}.")
print('~~'*60)
print(f"The odd numbers' list is made by: {odd_values}.")

