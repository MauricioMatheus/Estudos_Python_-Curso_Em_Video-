'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Por favor, digite o primeiro termo da PA.'))
razao = int(input('Por favor, digite a razão da PA.'))
decimo = primeiro + (10 - 1) * razao
print('Os termos da PA são:', end=' ')
for i in range(primeiro, decimo, razao):
    print(i, end=', ')
print('FIM.')


