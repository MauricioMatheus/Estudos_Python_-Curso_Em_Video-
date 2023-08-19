# Escreva um programa que leia a velocidade de um carro. - Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. - A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade do carro em km/h'))
lim = int(80)
multa = float(vel-lim)*7
if multa > 0:
    print(f'Você ultrapassou o limite de velocidade em {vel-lim} km/h, portanto pagará uma multa de R${multa:.2f}.')
else:
    print('Você não pagará multa. Tenha um bom dia!')
