'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = mais_barato = mais_que_1000 = cont = 0 #Contadores
nome_mais_barato = ''
while True:
    nome_produto = input('Por favor, digite o nome do produto.').strip().upper()
    preco = float(input('Por favor, digite o preço do produto em R$.'))
    cont += 1
    if preco < 0: #Evitando dígitos inválidos do usuário
        while preco < 0:
            preco = float(input('Preço inválido. Por favor, digite um preço diferente.'))
    if cont == 1 or preco < mais_barato: #Determinando o mais barato
        mais_barato = preco
        nome_mais_barato = nome_produto
    if preco > 1000:
        mais_que_1000 += 1
    total += preco
    decisao = input('Deseja continuar? [Sim/Não]').strip().upper()[0] #Perguntando ao usuário se ele deseja continuar
    if decisao not in 'SN': #Evitando dígitos inválidos do usuário
        while decisao not in 'SN':
            print('Decisão inválida. Por favor, tente novamente')
            print('~~'*30)
            decisao = input('Deseja continuar? [Sim/Não]').strip().upper()[0]
    print('~~' * 20)
    if decisao in 'N': #Condição de interrupção da estrutura de repetição
        break
print(f'Total gasto nas compras em {cont} produto(s)→ R${total:.2f}')
print(f'Quantidade de produtos que custaram mais que R$1000,00 → {mais_que_1000}')
print(f'{nome_mais_barato} é o produto mais barato, custando R${mais_barato:.2f}.')
