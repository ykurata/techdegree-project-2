from affine import Affine
from atbash import Atbash
from keyword_cipher import Keyword

#prints welcome messages
def welcome():
    print("Welcome to the Secret Messages!\n\n")
    print("These are the current available ciphers \n\n 1. Affine\n 2. Atbash\n 3. Keyword\n\n")
    print("Which cipher would you like to use?")

def encrypt_decrypt():
    """Encrypt or decrypt text."""

    playing = True

    while playing:
        #User input
        cipher = int(input("Enter the number of cipher associated with: "))
        text = input("What is the message?: ")
        choice = input("Are you going to encrypt or decrypt? Enter E or D: ").lower()
        print("\n")

        if choice == "e":
            #Generates affine cipher
            if cipher == 1:
                affine = Affine()
                print(affine.encrypt(text))
                playing = False

            #Generates atbash cipher
            elif cipher == 2:
                atbash = Atbash()
                print(atbash.encrypt(text))
                playing = False

            #Generates keyword cipher
            elif cipher == 3:
                #Ask user keyword
                secret_key = input("Enter your keyword: ")
                keyword = Keyword()
                print("\n")
                print(keyword.encrypt(text, secret_key))
                playing = False

        if choice == "d":
            #Decrypts affine cipher
            if cipher == 1:
                affine = Affine()
                print(affine.decrypt(text))
                playing = False

            #Decrypts atbash cipher
            elif cipher == 2:
                atbash = Atbash()
                print(atbash.decrypt(text))
                playing = False

            #Decrypts keyword cipher
            elif cipher == 3:
                secret_key = input("Enter your keyword: ")
                keyword = Keyword()
                print("\n")
                print(keyword.decrypt(text, secret_key))
                playing = False

    #Asks user to play again or not
    else:
        if input("\nDo you want to contine? Y/N: ").lower() == "y":
            welcome()
            encrypt_decrypt()
        else:
            print("See you next time!")

if __name__ == '__main__':
    welcome()
    encrypt_decrypt()
