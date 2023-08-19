'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

four_values = (int(input('Please, enter the first number')), int(input('Please, enter the second number')),
               int(input('Please, enter the third number')), int(input('Please, enter the last number')))
even_num = 0
for i in range(0, len(four_values)):
    if four_values[i] % 2 == 0:
        even_num += 1
print(f'The four numbers entered are: {four_values}')
print('~~'*30)
print(f'The biggest number is {max(four_values)} and the smallest one is {min(four_values)}.')
print('~~'*30)
if 9 in four_values: #If we don't have the number 9 in the tuple
    print(f'The number 9 appears {four_values.count(9)} times.')
    print('~~'*30)
if 3 in four_values: #If we don't have the number 3 in the tuple
    print(f'The number 3 was first entered in the position {four_values.index(3, 0)}.')
    print('~~' * 30)
print(f'There are {even_num} even numbers.')

