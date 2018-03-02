import string

from ciphers import Cipher


class Affine(Cipher):
    def __init__(self):
        self.alpha = string.ascii_uppercase

    def encrypt(self, text):
        """
        Takes text and encrypts it.
        try: converts each character of text into the variable index
        except ValueError: appends the character into output
        else: appends the encrypted text into output

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
                output.append(self.alpha[(index * 5 + 8) % 26])
        return "".join(output)


    def decrypt(self, text):
        """
        Takes text and decrypts it
        try: converts each character of text into the variable index
        except ValueError: appends the character into output
        else: appends decrypted text into output

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
                output.append(self.alpha[21 * (index - 8) % 26])
        return "".join(output)
