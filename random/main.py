import random
def run():

    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    dBclaves = [
        'ÑANDU',
        'PERRO',
        'GATO',
    'POLLO'
    ]

    word =random.choice(dBclaves)
    spaces= ['_'] * len(word)
    attemps = 6
    while True:
        os.system('clear')
        for character in spaces:
            print(character,end=' ')
        print(images[attemps])
    letter = input('elige una letra').upper()

    fount = False
    for idx, character in enumerate(word):
        if character == letter:
            spaces[idx] = letter
            found = True
    if not found:
        attemps -= 1
        if '_'not in spaces:
            os.system('clear')
            print('ganaste')
            break
            input()
        if attemps == 0:
            os.system('clear')
            print('Ganaste')
            break
            input()


if __name__ == 'main':
    run()