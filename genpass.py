""" Gerador de senhas """
import random
import pyperclip

UPPERCASE = []
LOWERCASE= []
SPECIALS= ['.', ',', '?', '^', '@', '!', '#', '$']

for letter in range(65, 91):
    UPPERCASE.append(chr(letter))

for letter in range(97, 123):
    LOWERCASE.append(chr(letter))

passlen = int(input('Tamanho da senha: '))

PASSWORD = ''

def rand_letter(arr):
    """
    Randomiza os arrays e retorna um valor

    Parameters:
        arr (list): Array

    Returns:
        value(int): Número aleatório"""
    return random.randint(0, (len(arr) - 1))


for i in range(0, (passlen + 1)):
    chartype = random.randint(1,4)

    if chartype == 1:
        letter = rand_letter(UPPERCASE)
        PASSWORD += UPPERCASE[letter]

    if chartype == 2:
        letter = rand_letter(LOWERCASE)
        PASSWORD += LOWERCASE[letter]

    if chartype == 3:
        LETTER = str(random.randint(0,10))
        PASSWORD += LETTER

    if chartype == 4:
        letter = rand_letter(SPECIALS)
        PASSWORD += SPECIALS[letter]

pyperclip.copy(PASSWORD)
print(PASSWORD)
