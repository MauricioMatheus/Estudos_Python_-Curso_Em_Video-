'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

people = []
data = []
heaviest = lightest = 0
count = 0
while True:
    print('Please enter the following data')
    print('~~'*20)
    data.append(input('Name:').strip().title())
    data.append(float(input('Weight (Kg): ')))
    if count == 0: #Determining the heaviest and lightest weights
        heaviest = data[1]
        lightest = data[1]
    else:
        if data[1] > heaviest:
            heaviest = data[1]
        elif data[1] < lightest:
            lightest = data[1]
    count += 1
    people.append(data[:]) #Creating a copy of the list data
    data.clear() #deleting the list 'data' in order to add more information
    decision = input('Would you like to enter information about another person? [Yes/No]').strip().upper()[0]
    if decision not in 'YN':
        while decision not in 'YN':
            print('Invalid option, please try again.')
            print('~~'*20)
            decision = input('Would you like to enter information about another person? [Yes/No]').strip().upper()[0]
    if decision == 'N':
        break
print('~~'*20)
print(f'{count} people were registered.')
print(f'Heaviest: {heaviest} Kg. Weight of [', end=' ')
for i in range(len(people)): #Showing the people who have the heaviest weight
    if people[i][1] == heaviest:
        print(f'{people[i][0]}', end=' ')
print(']')
print(f'Lightest: {lightest} Kg. Weight of [', end=' ')
for i in range(len(people)): #Showing the people who have the lightest weight
    if people[i][1] == lightest:
        print(f'{people[i][0]}', end=' ')
print(']')

