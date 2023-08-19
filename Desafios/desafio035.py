# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

reta1 = float(input('Digite o comprimento da reta 1 em m.'))
reta2 = float(input('Digite o comprimento da reta 2 em m.'))
reta3 = float(input('Digite o comprimento da reta 3 em m.'))
condicao = bool()

# Condição da existência de um triângulo:
if reta2 - reta3 < reta1 < reta2 + reta3:
    if reta1 - reta3 < reta2 < reta1 + reta3:
        if reta1 - reta2 < reta3 < reta1 + reta2:
            condicao = True
else:
    condicao = False

if condicao is True:
    print('Essas retas PODEM formar um triângulo.')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')
