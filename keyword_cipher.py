from ciphers import Cipher

class Keyword(Cipher):
    def __init__(self):
        self.alpha = "abcdefghijklmnopqrstuvwxyz ".upper()

    def encrypt(self, text, secret_key):
        """Takes text and secret_key and encrypts the text"""

        text = text.upper()
        secret_key = secret_key.upper()
        key = "".upper()
        output = []

        #Checks if characters of secret_key are in alpha, but not in key
        for char in secret_key:
            if char in self.alpha:
                if char not in key:
                    key += char

        #Checks if characters of alpha are not in key.
        for char in self.alpha:
            if char not in key:
                key += char

        #Appends encrypted text into output
        for char in text:
            try:
                index = self.alpha.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(key[index])
        return "".join(output)

    def decrypt(self, text, secret_key):
        """Takes text and secret_key and decrypts text"""

        text = text.upper()
        secret_key = secret_key.upper()
        key = "".upper()
        output = []

        #Checks if characters of secret_key are in alpha, but not in key
        for char in secret_key:
            if char in self.alpha:
                if char not in key:
                    key += char

        #Checks if characters of alpha are not in key
        for char in self.alpha:
            if char not in key:
                key += char

        #Appends decrypted text into output
        for char in text:
            try:
                index = key.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.alpha[index])
        return "".join(output)
