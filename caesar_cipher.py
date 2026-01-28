def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)

while True:
    choice = input("Would you like to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()
    
    if choice == 'q':
        break
    elif choice == 'e':
        text = input("Enter message: ")
        shift = int(input("Enter shift (1-25): "))
        print(f"Encrypted: {encrypt(text, shift)}")
    elif choice == 'd':
        text = input("Enter encrypted message: ")
        shift = int(input("Enter shift (1-25): "))
        print(f"Decrypted: {decrypt(text, shift)}")
    else:
        print("Invalid choice")
