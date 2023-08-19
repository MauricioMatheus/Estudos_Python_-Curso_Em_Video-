'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = input('Digite uma frase qualquer').strip()
frase = frase.lower()
print(f'Na frase, a letra (a) aparece {frase.count("a")} vezes e pela primeira vez na posição {frase.find("a")+1}.')
print(f'E por fim, a letra (a) aparece pela última fez na posição {frase.rfind("a")+1}.')
