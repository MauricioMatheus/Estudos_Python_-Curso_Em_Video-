def mostraLinha(): #Utilizando uma função sem parâmetros
    print('--'*20)

def mensagem(msg): #Utilizando uma função com parâmetro
    print('--'*20)
    print(msg)
    print('--'*20)

#Sem parâmetros

'''mostraLinha()
print('   SISTEMA DE ALUNOS   ')

mostraLinha()
print('   CADASTRO DE FUNCIONÁRIOS   ')

mostraLinha()
print('   ERRO DO SISTEMA   ')'''

#Função com parâmetro

mensagem('   SISTEMA DE ALUNOS   ')
#mensagem('   CADASTRO DE FUNCIONÁRIOS   ')
#mensagem('   ERRO DO SISTEMA   ')



a = 3
b = 5
s = a + b
print(s, '\n')

#melhorando com função:

def soma(a, b):
    s = a + b
    print(f'A soma resulta em: {s}')

soma(13, 18)
soma(5, 10)
soma(20, 40)

print() #Pulando uma linha. (Também serve '\n')

def multiplica(a, b, c):
    p = a*b + 2*c
    print(f'A multiplicação resulta em: {p}')

multiplica(2, 3, 5)
multiplica(2, 3, 4)
multiplica(1, 2, 3)

print()
#Utilizando desempacotamento [*] (Qualquer quantidade de parâmetros na função): Usa tuplas

'''def contador (* num):
    print(num)'''

#Utilizando laço na função

def contador(* num): 
    print(f'Foram recebidos {len(num)} valores:')
    for i in num:
        print(f'{i}')
    print('FIM!')

contador(1, 2, 3, 4)
contador(2, 3, 4, 5, 6)
contador(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

#Utilizando função para manipular listas: [Não é desempacotamento!]

def dobra(list):
    pos = 0
    print('Os algarismos múltiplicados por 2 resultam em:')
    for i in range(0, len(list)):
        list[i] = (list[i])*2
        print(f'O {i+1}º termo resulta em {list[i]}')
    print('FIM!')

value = [2, 3, 4, 5, 6, 7, 8, 9, 10]

dobra(value)