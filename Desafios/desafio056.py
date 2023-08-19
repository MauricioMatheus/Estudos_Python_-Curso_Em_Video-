'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

maior_idade = 0 #Valor abstrato
mais_velho = 'a' #String abstrata
contador = 0
soma_idades = 0
for i in range(1, 5):
    nome = input('Por favor, digite o seu nome inteiro.').strip().title()
    idade = int(input('Por favor, digite a sua idade.'))
    sexo = int(input('''Qual o seu sexo? 
    Digite [ 1 ] para masculino
    Digite [ 2 ] para feminino.'''))
    soma_idades += idade
    if sexo == 1 and idade > maior_idade: #Determinando o homem mais velho
        maior_idade = idade
        mais_velho = nome
    if sexo == 2 and idade < 20: #Determinando quantas mulheres com menos de 20 anos há
        contador += 1
media = soma_idades/4
print(f'A média de idade do grupo é de {media} anos, {mais_velho} é o homem mais velho tendo {maior_idade}', end=' ')
print(f'anos, e há {contador} mulher(es) com menos de 20 anos.')
