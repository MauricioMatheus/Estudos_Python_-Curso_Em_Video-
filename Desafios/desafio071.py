'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

total_banknotes = 0
banknote = 50
print('~~'*30)
print('Bem vindo ao Nubank!')
print('~~'*30)
value = int(input('Por favor, digite o valor a ser sacado em R$.'))
total = value
while True:
    if total >= banknote: #Iniciando a contagem de cédulas pelas de R$50
        total_banknotes += 1
        total -= banknote
    else: #Caso o total já seja menor que a cédula indicada
        if total_banknotes > 0:
            print(f'Total de {total_banknotes} cédula(s) de R${banknote}')
        total_banknotes = 0 #Zerando a quantidade de cédulas
        if banknote == 50: #Trocando a cédula para a de R$20
            banknote = 20
        elif banknote == 20: #Trocando a cédula para a de R$10
            banknote = 10
        elif banknote == 10: #Trocando a cédula para a de R$1
            banknote = 1
        if total == 0: #Condição de parada da estrutura de repetição
            break
print('~~'*30)
print('Volte sempre! Tenha um bom dia!')



