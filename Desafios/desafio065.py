'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num = quant_num = maior = menor = soma = 0
decisao = 'S'
while decisao not in 'N':
    num = int(input('Digite um número inteiro'))
    quant_num += 1
    soma += num
    if quant_num == 1: # Valores iniciais para o maior e menor
        maior = menor = num
    if num > maior: # Determinando o maior número
        maior = num
    if num < menor: # Determinando o menor número
        menor = num
    decisao = input('Deseja adicionar mais um valor? [Sim/Não]').strip().upper()[0]
    if decisao not in 'SN': # Caso o usuário introduza alguma opção inválida
        while decisao not in 'SN':
            print('Opção inválida. Por favor, tente novamente.')
            print('~~'*20)
            decisao = input('Deseja adicionar mais um valor? [Sim/Não]').strip().upper()[0]
media = soma/quant_num
print(f'Você digitou {quant_num} número(s). O maior foi {maior}, o menor foi {menor}', end=' ')
print(f'e a média entre eles é {media:.2f}.')
