alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift] 
translation_table = str.maketrans(alphabet, shifted_alphabet)
text = 'hello world'
encrypted_text = text.translate(translation_table)

def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)
