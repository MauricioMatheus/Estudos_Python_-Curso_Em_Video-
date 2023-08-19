'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Digite um valor.'))
n2 = float(input('Digite outro valor.'))
maior = n1 #Determinando um número maior de início
menu = int(input('''O que você deseja fazer com esses valores?
Digite [ 1 ] para somá-los
Digite [ 2 ] para multiplicá-los
Digite [ 3 ] para determinar qual é o maior
Digite [ 4 ] para escolher novos números
Digite [ 5 ] para sair do programa.'''))

while menu != 5:
    if menu == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é de {soma:.2f}.')
        print('=='*20)
        menu = int(input('''Deseja fazer mais algo?
        Digite [ 1 ] para somá-los
        Digite [ 2 ] para multiplicá-los
        Digite [ 3 ] para determinar qual é o maior
        Digite [ 4 ] para escolher novos números
        Digite [ 5 ] para sair do programa.'''))
    elif menu == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação {n1} e {n2} é de {multiplicacao}.')
        print('=='*20)
        menu = int(input('''Deseja fazer mais algo?
        Digite [ 1 ] para somá-los
        Digite [ 2 ] para multiplicá-los
        Digite [ 3 ] para determinar qual é o maior
        Digite [ 4 ] para escolher novos números
        Digite [ 5 ] para sair do programa.'''))
    elif menu == 3:
        if n2 > maior:
            maior = n2
        elif n1 > maior:
            maior = n1
        print(f'O maior valor entre {n1} e {n2} é {maior}.')
        print('=='*20)
        menu = int(input('''Deseja fazer mais algo?
        Digite [ 1 ] para somá-los
        Digite [ 2 ] para multiplicá-los
        Digite [ 3 ] para determinar qual é o maior
        Digite [ 4 ] para escolher novos números
        Digite [ 5 ] para sair do programa.'''))
    elif menu == 4:
        print('=='*20)
        n1 = float(input('Digite outro valor.'))
        n2 = float(input('Digite mais um valor.'))
        print('=='*20)
        menu = int(input('''O que você deseja fazer com esses novos valores?
        Digite [ 1 ] para somá-los
        Digite [ 2 ] para multiplicá-los
        Digite [ 3 ] para determinar qual é o maior
        Digite [ 4 ] para escolher novos números
        Digite [ 5 ] para sair do programa.'''))
    elif menu == 5:
        break
    else:
        print('Opção inválida, tente novamente')
        menu = int(input('''O que você deseja fazer com esses valores?
        Digite [ 1 ] para somá-los
        Digite [ 2 ] para multiplicá-los
        Digite [ 3 ] para determinar qual é o maior
        Digite [ 4 ] para escolher novos números
        Digite [ 5 ] para sair do programa.'''))
print('=='*20)
print('Fim do programa.')
