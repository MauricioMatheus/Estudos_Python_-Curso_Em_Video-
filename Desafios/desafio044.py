#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

price = float(input('Por favor, digite o preço do produto em R$.'))
pagamento = int(input('''Qual será a condição de pagamento? Digite:
[ 1 ] para à vista em dinheiro/cheque
[ 2 ] para à vista no cartão
[ 3 ] para até duas vezes no cartão
[ 4 ] para 3x ou mais'''))
valor_total = 0
qtd_parcelas = 0

if pagamento == 4:
    qtd_parcelas = int(input('Em quantas parcelas você deseja fazer o pagamento?'))

print(f'O preço do produto que é de R${price:.2f}', end=' ')
if pagamento == 1: #Pagamento à vista em dinheiro/cheque
    valor_total = price * (90/100)
    print(f'Custará R${valor_total:.2f}')
elif pagamento == 2: #Pagamento à vista no cartão
    valor_total = price * (95/100)
    print(f'custará R${valor_total:.2f} no final.')
elif pagamento == 3: #Pagamento em até duas vezes no cartão
    valor_total = price
    parcela = valor_total / 2
    print(f'custará 2 parcelas de R${parcela:.2f}. Não haverá juros.')
elif pagamento == 4: #Pagamento parcelado em 3x ou mais
    valor_total = price * (120/100)
    parcela = valor_total / qtd_parcelas
    print(f'custará {qtd_parcelas} parcelas de R${parcela:.2f} COM juros. O preço total será de R${valor_total:.2f}.')
else:
    print(f'custará R${price:.2f}.')
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente.')

