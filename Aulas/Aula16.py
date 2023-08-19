drinks = ('Refrigerante', 'Suco', 'Água', 'Energético')
#for i in bebidas:
#for i in range(len(bebidas)):
for pos, drink in enumerate(drinks): #Mostra tanto a posição quando o elemento
    print(f'Eu vou beber {drink} na posição {pos}.')
#print('Cara, bebi muita coisa!')
print(sorted(drinks))
#print(drinks)
a = (1, 2, 3, 4, 5, 5, 6, 1, 2, 3, 4, 4, 6, 5, 9, 8, 7, 1, 2, 5)
b = (6, 7, 8, 9, 6, 9, 8, 7, 4, 9, 10)
c = a + b
print(c)
print('~~'*20)
print(len(c))
print('~~'*20)
print(c.count(1)) #Quantidade de elementos "1"
print('~~'*20)
print(c.index(4, 5)) #Primeira ocorrência do elemento 4 a partir da posição 5
del c #Deletando a tupla
print(c) #Erro, pois a tupla foi excluída.
