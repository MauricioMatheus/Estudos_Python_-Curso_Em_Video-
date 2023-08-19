''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, 
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

values = []
while True:
    number = int(input('Please, enter an integer value.'))
    if number not in values: #Adding num  ber only if it isn't already inside the list
        values.append(number)
    else:
        print('This value is already inside the list.')
        print('~~'*20)
    decision = input('Would you like to enter another value? [Yes/No]').strip().upper()[0]
    if decision not in 'YN': #Avoiding invalid options from the user
        while decision not in 'YN':
            print('Error, invalid option. Please try again.')
            print('~~'*20)
            decision = input('Would you like to enter another value? [Yes/No]').strip().upper()[0]
    if decision == 'N': #Break condition
        break
    elif decision == 'S':
        continue
values.sort() #Sorting the list
print(f'The sorted list is: {values}')