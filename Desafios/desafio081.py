'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de valores, ordenada de forma decrescente;
c) Se o valor 5 foi digitado e está ou não na lista. '''

values = []
cont = 0
while True:
    number = int(input('Please, enter an integer number.'))
    values.append(number)
    cont += 1
    decision = input('Would you like to enter another number? [Yes/No]').strip().upper()[0]
    if decision not in 'YN':
        while decision not in 'YN':
            print('Error, invalid option. Please try again.')
            decision = input('Would you like to enter another number? [Yes/No]').strip().upper()[0]
            print('~~'*20)
    if decision == 'N':
        break
values.sort(reverse=True)
print(f'{cont} numbers were entered. The reversely sorted list is made by: {values}.')
if 5 in values:
    print('Number 5 was entered and it is located inside the list.')
else:
    print('Number 5 was not entered therefore it is not located inside the list.')
