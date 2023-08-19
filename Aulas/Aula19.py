pessoas = {'nome': 'Maurício', 'idade': 22, 'sexo': 'Masculino'}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('--'*30)
for i in pessoas.keys(): #Apenas as chaves
    print(i)
print('--'*30)
for i in pessoas.values(): #Apenas os valores
    print(i)
print('--'*30)
for k, v in pessoas.items(): #Nos dicionários não é necessário utilizar o enumerate, pois há o comando .items()
    print(f'{k} = {v}')
print('--'*30)
del pessoas['sexo'] #Nos dicionários os elementos são referidos por chaves.
print(pessoas)
pessoas['nome'] = 'Matheus' #Trocando o valor de nome no dicionário
print(pessoas)
pessoas['peso'] = 53 #Adicionando um novo item no dicionário (O append não precisa ser utilizado em dicionários)
print(pessoas)

print('**'*30)
#Criando um dicionário dentro de uma lista:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

'''brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = {}
brasil = []
for i in range(0, 3): #Adicionando 3 índices
    estado['uf'] = input('Por favor, digite o nome do estado')
    estado['sigla'] = input('Por favor, digite a sigla do estado')
    brasil.append(estado.copy()) #Não é possível utilizar [:] nos dicionários. Para isso, há o comando .copy()

print('---'*20)
for e in brasil:
    print(e)

print('-----'*20)

for e in range(0, 3):
    print(brasil[e])

print('--'*20)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

print('---'*20)

for e in brasil:
    for v in e.values():
        print(v)

'''dicionario.clear() para limpar'''