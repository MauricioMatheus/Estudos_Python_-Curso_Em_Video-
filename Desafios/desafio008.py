'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

n = float(input('Digite um valor em metros'))
print('{} metros equivale a {:.3f} centrímetros e {:.3f} milímetros.'.format(n, n*(1/10), n*(1/100)))



