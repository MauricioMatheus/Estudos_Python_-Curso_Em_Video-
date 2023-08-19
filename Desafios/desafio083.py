'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

count_1 = count_2 = 0
expression = input('Please, enter a mathematical expression').strip().lower()
for i in range(len(expression)):
    if expression[i] == '(':
        count_1 += 1
    elif expression[i] == ')':
        count_2 += 1
if count_1 != count_2:
    print('Invalid mathematical expression!')
else:
    print('Valid mathematical expression!')