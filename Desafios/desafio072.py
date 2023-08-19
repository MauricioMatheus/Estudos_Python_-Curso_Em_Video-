'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

until_20 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze,', 'Doze',
            'Treze', 'Quatorze','Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
decision = ''
while True:
    num = int(input('Por favor, digite um número inteiro entre 0 e 20.'))
    if num < 0 or num > 20: #Impedindo erros de digitação do usuário
        while num < 0 or num > 20:
            print('Número inválido. Por favor tente novamente.')
            num = int(input('Por favor, digite um número inteiro entre 0 e 20.'))
            print('~~' * 20)
    print(f'O número que você digitou foi {until_20[num].upper()}.')
    decision = input('Deseja digitar mais algum número? [Sim/Não]').strip().upper()[0] #Decisão do usuário
    if decision not in 'SN': #Impedindo erros de digitação do usuário
        while decision not in 'SN':
            print('Opção inválida. Por favor tente novamente.')
            decision = input('Deseja digitar mais algum número? [Sim/Não]').strip().upper()[0]
    if decision == 'N': #Condição de parada do laço
        break
    else:
        print('~~' * 20)
        continue
print('FIM DO PROGRAMA.')


