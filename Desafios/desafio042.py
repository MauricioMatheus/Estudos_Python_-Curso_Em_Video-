'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

reta1 = float(input('Digite o comprimento da reta 1 em m.'))
reta2 = float(input('Digite o comprimento da reta 2 em m.'))
reta3 = float(input('Digite o comprimento da reta 3 em m.'))
condicao = bool()

#Condição para a existência de triângulo
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    condicao = True
else:
    condicao = False

#Tipo de triângulo formado
if condicao is True:
    if reta1 == reta2 and reta1 == reta3:
        print('O triângulo formado é equilátero.')
    elif reta1 != reta2 != reta3 != reta1:
        print('O triângulo formado é escaleno.')
    else:
        print('O triângulo formado é isósceles.')
else:
    print('Não é possível formar um triângulo com essas retas.')




