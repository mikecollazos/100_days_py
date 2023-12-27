from ceasar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def ceasar(text, shift, direction):
    shifted_text =''
    if direction == "encode":
        for char in text:
            if char in alphabet:
                shifted_letter = alphabet.index(char) + shift
                shifted_text += alphabet[shifted_letter]
            else:
                shifted_text += char
        print(f"The encoded text is {shifted_text}")
    elif direction == "decode":
        for char in text:
            if char in alphabet:
                shifted_letter = alphabet.index(char) - shift
                shifted_text += alphabet[shifted_letter]
            else:
                shifted_text += char
        print(f"The decoded text is {shifted_text}")
    else:
        print("direction not clear")

should_continue = True
while should_continue: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text=text, shift=shift, direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == "no":
        should_continue == False
        print("Goodbye")
    else:
        should_continue == True