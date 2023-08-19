'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Digite o valor da casa em R$.'))
salario = float(input('Digite o seu salário.'))
anos = int(input('Em quantos anos você pretende pagar a casa?'))
valor_mensal = float(valor_casa/(anos*12))
if valor_mensal > salario * (30/100):
    print(f'Infelizmente o valor mensal de R${valor_mensal:.2f}', end='')
    print(' excedeu 30% de seu salário, portanto o empréstimo será negado.')
else:
    print(f'O valor da prestação mensal será de R${valor_mensal:.2f}.')
