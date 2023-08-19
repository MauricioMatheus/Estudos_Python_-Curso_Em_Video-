'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

import datetime
atual = datetime.date.today().year
cont_maiores = 0
cont_menores = 0
for i in range(1, 8):
    nascimento = int(input(f'Por favor, digite o ano de nascimento da {i}ª pessoa.'))
    idade = atual - nascimento
    if idade >= 18:
        cont_maiores += 1
    else:
        cont_menores += 1
        continue
print(f'Dessas pessoas, {cont_maiores} são de maior enquanto {cont_menores} são de menor.')
