'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular'''

products = ('Fridge', 1000.50, 'Stove', 890.45, 'Smart TV', 1499.99, 'PS5', 500.40, 'RTX 3090', 1530.99)
print('--'*20)
print(f'{"Identification and prices:":^30}') #Centralizando
print('--'*20)
for i in range(0, len(products) - 1, 2):
    print(f'{products[i]:.<30}', f'${products[i+1]:>7.2f}') #Deixando tudo organizado, alinhando os preços
print('--'*20)
print(f'{"FINISH":^30}') #Centralizando
