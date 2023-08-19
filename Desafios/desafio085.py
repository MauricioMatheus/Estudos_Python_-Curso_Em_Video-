'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

valores = [[], []]
'''pares = []
impares = []''' #Utilizadas caso na não utilização de listas compostas
for i in range(0, 7):
    num = int(input('Por favor, digite um número inteiro'))
    if num % 2 == 0:
        valores[0].append(num) #Adicionando os valores para a sublista de números pares
    else:
        valores[1].append(num) #Adicionando os valores para a sublista de números ímpares

'''pares.sort() #Ordenando os elementos da lista pares
impares.sort() #Ordenando os elementos da lista impares
valores.append(pares[:]) #Adicionando uma cópia dos elementos da lista pares para a lista valores
valores.append(impares[:]) # '' '' impares ''' 

#Solução utilizada caso sejam criadas 3 listas individuais

valores[0].sort() #Ordenando os valores pares
valores[1].sort() #Ordenando os valores ímpares
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')