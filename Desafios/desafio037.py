''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 
2 para octal e 
3 para hexadecimal.'''

n = int(input('Digite um número inteiro.'))
base = int(input('''Digite a base de conversão desejada:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL '''))

if base == 1:
    print(f'O número {n} convertido para base binária é igual a {bin(n)[2:]}.')
elif base == 2:
    print(f'O número {n} convertido para base octal é igual a {oct(n)[2:]}.')
elif base == 3:
    print(f'O número {n} convertido para base hexadecimal é igual a {hex(n)[2:]}.')
else:
    print('Opção inválida, tente novamente.')

