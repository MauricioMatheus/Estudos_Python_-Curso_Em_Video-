''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

cont_maiores = cont_masc = cont_fem20 = 0 #Contadores
while True:
    idade = int(input('Por favor, digite a idade.'))
    sexo = input('Por favor, digite o gênero sexual: [Masculino/Feminino]').strip().upper()[0]
    if sexo not in 'MF': #Evitando erros de digitação do usuário
        while sexo not in 'MF':
            print('Opção inválida, por favor tente novamente.')
            print('~~'*20)
            sexo = input('Por favor, digite o gênero sexual: [Masculino/Feminino]').strip().upper()[0]
    if idade > 18:
        cont_maiores += 1
    if sexo in 'M':
        cont_masc += 1
    if sexo in 'F' and idade < 20:
        cont_fem20 += 1
    decisao = input('Deseja continuar?').strip().upper()[0]
    print('~~'*20)
    if decisao in 'N': #Condição de parada da estrutura de repetição
        break
    if decisao not in 'SN': #Evitando erros de digitação do usuário
        while decisao not in 'SN':
            print('Opção inválida. Por favor tente novamente.')
            decisao = input('Deseja continuar?').strip().upper()[0]
            print('~~'*20)
print(f'Total de pessoas com mais de 18 anos: {cont_maiores}')
print(f'Quantidade de homens: {cont_masc}')
print(f'Quantidade de mulheres com menos de 20 anos: {cont_fem20}')
