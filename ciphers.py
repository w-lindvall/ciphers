import string


class Cipher:
    """ Parent class of ciphers that raises error
    if subclass does not have an encrypt or decrypt method.
    """
    def __init__(self):
        """ Raises error if subclass does not have
        an encrypt or decrypt method.
        """
        def encrypt(self):
            raise NotImplementedError()

        def decrypt(self):
            raise NotImplementedError()


class Atbash(Cipher):
    """ The Atbash cipher maps each letter of the alphabet
    onto a letter of the same alphabet reversed.
    """
    def __init__(self):
        """ Initializes an instance of the Atbash class
        and defines required variables."""
        super().__init__()
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_reverse = self.alphabet[::-1]
        self.output = []

    def encrypt(self, string):
        """ Encrypts user-defined message using the Atbash cipher."""
        for letter in string:
            # gets index value of each letter in alphabet
            try:
                original_index = self.alphabet.index(letter.lower())
                self.output.append(self.alphabet_reverse[original_index])
            # appends non-letter character to output[]
            except ValueError:
                self.output.append(letter)
        # joins list of output letters
        return ''.join(self.output)

    def decrypt(self, string):
        """ Decrypts user-defined message using the Atbash cipher."""
        for letter in string:
            try:
                original_index = self.alphabet_reverse.index(letter.lower())
                self.output.append(self.alphabet[original_index])
            except ValueError:
                self.output.append(letter)
        return ''.join(self.output)


class Keyword(Cipher):
    """ The Keyword cipher maps each letter of the alphabet
    onto the same alphabet offset by placing each non-repeating
    letter of the keyword in front of the remaining letters
    alphabetically.
    """
    def __init__(self):
        """ Initializes an instance of the Keyword class
        and defines required variables."""
        super().__init__()
        self.keyword = input('Please enter the keyword you wish to use\n'
                             '(Character duplicates and non-letter characters '
                             'will be ignored)\n'
                             '> ').lower()
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_modified = []
        self.output = []

    def encrypt(self, string):
        """ Encrypts user-defined message using the Keyword cipher."""
        for letter in self.keyword:
            # letter by letter places non-repeated letters of keyword into list
            if (letter.lower() in self.alphabet
                    and letter.lower() not in self.alphabet_modified):
                self.alphabet_modified.append(letter)
        for letter in self.alphabet:
            # places non-repeated remaining letters of alphabet into list
            if letter.lower() not in self.alphabet_modified:
                self.alphabet_modified.append(letter)
        for letter in string:
            if letter == ' ':
                self.output.append(' ')
            else:
                original_index = self.alphabet.index(letter.lower())
                self.output.append(self.alphabet_modified[original_index])
        return ''.join(self.output)

    def decrypt(self, string):
        """ Decrypts user-defined message using the Keyword cipher."""
        for letter in self.keyword:
            # letter by letter places non-repeated letters of keyword into list
            if (letter.lower() in self.alphabet
                    and letter.lower() not in self.alphabet_modified):
                self.alphabet_modified.append(letter)
        for letter in self.alphabet:
            # places non-repeated remaining letters of alphabet into list
            if letter.lower() not in self.alphabet_modified:
                self.alphabet_modified.append(letter)
        for letter in string:
            if letter == ' ':
                self.output.append(' ')
            else:
                original_index = self.alphabet_modified.index(letter.lower())
                self.output.append(self.alphabet[original_index])
        return ''.join(self.output)


class PolybiusSquare(Cipher):
    """ The Polybius Square cipher places the alphabet into a
    5x5 grid and makes use of the letter’s coordinates within
    this grid to encrypt and decrypt messages. To fit the 26
    letters of the English alphabet into the grid the letters
    ‘i’ and ‘j’ are often combined and use the same coordinates.
    """
    def __init__(self):
        """ Initializes an instance of the PolybiusSquare class."""
        super().__init__()
        rows = list(range(1, 6))
        cols = list(range(1, 6))
        # creates list of number pairs used as coordinate index
        self.coordinates = [(str(x) + str(y)) for x in rows for y in cols]
        # alphabet_modified contains letters 'i' and 'j' on same index value
        self.alphabet_modified = list(string.ascii_lowercase)
        self.alphabet_modified.remove('i')
        self.alphabet_modified.remove('j')
        self.alphabet_modified.insert(8, '(i/j)')
        self.output = []

    def encrypt(self, string):
        """ Encrypts user-defined message using the Polybius Square cipher."""
        # creates dict with letters as keys and corresponding coordinates
        alphabet_lookup = {letter: number for letter, number
                           in zip(self.alphabet_modified, self.coordinates)}
        for letter in string:
            if letter.lower() == 'i' or letter.lower() == 'j':
                self.output.append('24')
            elif letter == ' ':
                continue
            else:
                self.output.append(str(alphabet_lookup.get(letter.lower())))
        return ' '.join(self.output)

    def decrypt(self, string):
        """ Decrypts user-defined message using the Polybius Square cipher."""
        # creates dict with letters as keys and corresponding coordinates
        alphabet_lookup = {number: letter for letter, number
                           in zip(self.alphabet_modified, self.coordinates)}
        for number_pair in string:
            if number_pair not in alphabet_lookup.keys():
                self.output.append(number_pair)
            else:
                self.output.append(alphabet_lookup.get(number_pair))
        return ''.join(self.output)
