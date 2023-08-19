'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. 
'''

while True:
  num = int(input('Por favor, digite um número inteiro.'))
  if num < 0:
    break
  print(f'A tabuada de {num} é:')
  for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
  print('~' * 20)
print('Número negativo introduzido. Fim do programa')
