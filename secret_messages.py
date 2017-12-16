import os
import sys
from ciphers import Atbash
from ciphers import Keyword
from ciphers import PolybiusSquare


def clear():
    """ Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    """ Presents a welcome menu and obtains
    and checks validity of user's preferences
    for encryption/decryption and a choice
    between three ciphers.
    """
    clear()
    print('Welcome!\n'
          'Would you like to encrypt or decrypt a message?')
    while True:
        encrypt_or_decrypt = input('> ').lower()
        if encrypt_or_decrypt == 'encrypt':
            break
        if encrypt_or_decrypt == 'decrypt':
            break
        else:
            clear()
            print('Welcome!\n'
                  'Please enter either \'encrypt\' or \'decrypt\'.')
            continue
    clear()
    print('The available ciphers are:\n'
          '- Atbash\n'
          '- Keyword\n'
          '- Polybius Square\n\n'
          'Please enter the name of the cipher you wish to use.')
    while True:
        cipher = input('> ').lower()
        if cipher == 'atbash':
            break
        if cipher == 'keyword':
            break
        if cipher == 'polybius square' or cipher == 'polybiussquare':
            break
        if cipher == 'q' or cipher == 'quit' or cipher == 'exit':
            sys.exit()
        else:
            clear()
            print('The available ciphers are:\n'
                  '- Atbash\n'
                  '- Keyword\n'
                  '- Polybius Square\n\n'
                  'Sorry, I am not able to use the \'{}\' cipher. '
                  'Please enter the name of a cipher '
                  'from the list above.'.format(cipher.title()))
            continue
    return encrypt_or_decrypt, cipher


def get_string(encrypt_or_decrypt, cipher):
    """ Obtains and checks validity of the message
    to be encrypted/decrypted.
    """
    clear()
    print('What would you like to {0}?'.format(encrypt_or_decrypt))
    # Prepares input for decrypting with Polybius Square cipher
    if cipher == 'polybius square' and encrypt_or_decrypt == 'decrypt':
        print('(Only valid number pairs will be decrypted, '
              'other characters will be part of decrypted message)')
        string = input('> ')
        # splits user input into list items
        string_blocks = string.split(' ')
        return string_blocks
    # ensure user input is one or more unicode letters
    else:
        while True:
            string = input('> ')
            if all(chars.isalpha() or chars.isspace() for chars in string):
                clear()
                return string
            else:
                clear()
                print('Please enter a message that consists of only letters '
                      'and spaces.')
                continue


def encrypt(string):
    """ Encrypts user defined message with the chosen cipher
    and prints the result.
    """
    clear()
    if cipher == 'atbash':
        print('The encrypted message is \''
              + str(Atbash().encrypt(string)) + '\'')
    elif cipher == 'keyword':
        print('The encrypted message is \''
              + str(Keyword().encrypt(string)) + '\'')
    elif cipher == 'polybius square':
        print('The encrypted message is \''
              + str(PolybiusSquare().encrypt(string)) + '\'')


def decrypt(string):
    """ Decrypts user defined message with the chosen cipher
    and prints the result.
    """
    clear()
    if cipher == 'atbash':
        print('The decrypted message is \''
              + str(Atbash().decrypt(string)) + '\'')
    elif cipher == 'keyword':
        print('The decrypted message is \''
              + str(Keyword().decrypt(string)) + '\'')
    elif cipher == 'polybius square':
        print('The decrypted message is \''
              + str(PolybiusSquare().decrypt(string)) + '\'')

if __name__ == '__main__':
    encrypt_or_decrypt, cipher = welcome()
    string = get_string(encrypt_or_decrypt, cipher)
    if encrypt_or_decrypt == 'encrypt':
        encrypt(string)
    elif encrypt_or_decrypt == 'decrypt':
        decrypt(string)
