# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. - Para salários
# superiores a R$1.250,00, calcule um aumento de 10%. -Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário em R$.'))
if salario > 1250:
    aumento = salario*(10/100)
else:
    aumento = salario*(15/100)
print(f'Após o aumento você receberá R${aumento:.2f} a mais de salário.')
print(f'Agora você ganhará R${salario+aumento:.2f}!')
