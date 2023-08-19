# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

import datetime
ano = int(input('Digite um ano. Se quiser o ano atual, digite "0".'))
if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
