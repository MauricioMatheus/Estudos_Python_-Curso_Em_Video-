'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

import datetime
nascimento = int(input('Digite o ano de seu nascimento.'))
atual = datetime.date.today().year
idade = atual - nascimento

if idade <= 9:
    print(f'Você tem {idade} anos em {atual}, portanto pertence à categoria MIRIM.')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos em {atual}, portanto pertence à categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos em {atual}, portanto pertence à categoria JUNIOR.')
elif 19 < idade <= 25:
    print(f'Você tem {idade} anos em {atual}, portanto pertence à categoria SÊNIOR.')
else:
    print(f'Você tem {idade} anos em {atual}, portanto pertence à categoria MASTER.')
