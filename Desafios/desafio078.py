'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

import random
values = []
for i in range(0, 5): #Repetion to randomly enter 5 numbers
    values.append(random.randint(1, 9))
biggest = max(values) #Determining the biggest number
smallest = min(values) #Determining the smallest number
print(f"List's size: {len(values)}.")
print(f'The list is made by: {values}')
print(f'The biggest number in the list is {biggest} and it is located at position {values.index(biggest)}.')
print(f'The smallest number in the list is {smallest} and it is located at position {values.index(smallest)}.')
