import string

from ciphers import Cipher

class Atbash(Cipher):
    def __init__(self):
        self.alpha = string.ascii_uppercase
        self.reverse_alpha = string.ascii_uppercase[::-1]

    def encrypt(self, text):
        """
        Takes text and encrypts it.
        try: converts each character of text into the variable index
        except ValueError: appends the character into output
        else: appends encrypted text into output

        returns output to string
        """
        output = []
        text = text.upper()

        for char in text:
            try:
                index = self.alpha.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.reverse_alpha[index])
        return "".join(output)

    def decrypt(self, text):
        """
        Takes text and encrypts it.
        try: converts each character of text into the variable index
        except ValueError: appends the character into output
        else: appends decrypted text into output

        returns output to string
        """
        output = []
        text = text.upper()

        for char in text:
            try:
                index = self.reverse_alpha.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.alpha[index])
        return "".join(output)
