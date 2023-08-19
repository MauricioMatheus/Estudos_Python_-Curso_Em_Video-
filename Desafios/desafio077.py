'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

words = ('Now', 'that', 'is', 'done', 'i', 'realize', 'the', 'error', 'of', 'my', 'ways', 'i', 'must', 'venture',
         'back', 'to', 'apologize', 'from', 'somewhere', 'far', 'beyond', 'the', 'grave') #A Little Piece Of Heaven :D

print(f"Tuple's size: {len(words)}")
for word in words: #Every tuple's elements
    print(f'In the word "{word.upper()}" we have:', end=' ')
    for letter in word: #Every elements' letters
        if letter.upper() in 'AEIOU': #If we have vowels in the word
            print(f'{letter.upper()}', end=' ')
    print('\n')
print(f'{"FINISH":^30}')
