test = []
test.append('Mauricio')
test.append(21)
galera = []
galera.append(test[:]) #Usa-se [:] para criar uma cópia da lista, assim evitando a ligação entre elas duas
test[0] = 'Jason'
test[1] = 25
galera.append(test[:]) #Usa-se [:] para criar uma cópia da lista, assim evitando a ligação entre elas duas e também a
# repositions dos elementos em test[]
#print(galera)
galera = [['Paulo', 19], ['Carlos', 20], ['Luíza', 25], ['Alice', 29]] #Outra forma de fazer a lista composta
#print(galera[3])
'''for p in range(len(galera)): #Maneira 1 de mostrar os dados
    print(galera[p])'''
'''for p in galera: #Maneira 2 de mostrar os dados
    print(p)'''
galera = []
dados = []
print('Por favor, introduza os seguintes dados:')
print('~~'*20)
for i in range(0, 3): #Maneira 3 de ler os dados
    dados.append(input('Nome'))
    dados.append(int(input('Idade')))
    galera.append(dados[:])
    dados.clear()
print(galera)

