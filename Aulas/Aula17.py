import random
num = [0, 2, 3, 4, 6, 8, 11, 21, 19, 1]
num[8] = 33 #Alterando elementos da lista
num.append(10) #Adicionando novos indices no fim da lista
num.sort() #Ordenando a lista em ordem crescente
# num.sort(reverse=True) #Ordenando a lista em ordem decrescente
num.insert(1, 44) #Inserindo o número 44 no índice 1 da lista
# num.pop() #removendo o último índice da lista
num.remove(3) #Removento o número 3 da lista, independente de qual seja o seu índice
print(type(num))
print(f'A lista tem {len(num)} elementos.')
print(num)

values = []
for i in range(0, 11):
    values.append(random.randint(1, 99))
# values_2 = values #Dessa maneira é criada uma ligação entre duas listas, o que não é ideal
values_2 = values[:] #Assim, fazemos de values_2 uma cópia da lista values
values_2[6] = 199

for position, value in enumerate(values):
    print(f'I found {value} in the position {position}!')
print(f'{"Finish!":^30}')
print(values_2)


