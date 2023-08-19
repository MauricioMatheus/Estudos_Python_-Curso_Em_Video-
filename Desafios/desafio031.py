# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule e peça o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.


dist = float(input('Digite a distância da viagem em Km.'))
if dist <= 200:
    preco = float(dist*0.5)
else:
    preco = float(dist*0.45)
print(f'Você fará uma viagem de {dist} km de distância.')
print(f'O preço da passagem será de R${preco:.2f}.')


