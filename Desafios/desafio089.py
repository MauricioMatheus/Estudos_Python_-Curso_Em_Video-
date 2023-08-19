'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''


'''nomes = []
notas1 = []
notas2 = []''' #Utilizadas na não utilização de listas compostas

aluno = [[], [], []]
medias = []
decisao = ''
while True:
    nome = input('Por favor, digite o nome do(a) aluno(a)')
    nota1 = float(input('Por favor, digite a nota 1 do(a) aluno(a)'))
    nota2 = float(input('Por favor, digite a nota 2 do(a) aluno(a)'))
    media = (nota1 + nota2)/2
    aluno[0].append(nome)
    aluno[1].append(nota1)
    aluno[2].append(nota2)
    medias.append(media)
    decisao = input('Deseja adicionar informações de mais algum aluno? [Sim/Não]').strip().title()[0]
    if decisao not in 'SN': #Evitando erros do usuário
        while decisao not in 'SN':
            print('Decisão inválida. Por favor tente novamente.')
            decisao = input('Deseja adicionar informações de mais algum aluno? [Sim/Não]').strip().title()[0]
    if decisao == 'N':
        break
print(aluno[0], '\n', aluno[1], '\n', aluno[2])