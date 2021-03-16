alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']



def ceaser(text, shift, direction):
    encryptedString = ""

    if direction == "encrypt":
        for i in range(0, len(text)):
            CurLetter = alphabet.index(text[i]) + shift
            if CurLetter >= len(alphabet):
                CurLetter = (alphabet.index(text[i]) - len(alphabet)) + shift
            encryptedString += alphabet[CurLetter]
    else:
        for i in range(0, len(text)):
            CurLetter = alphabet.index(text[i]) - shift
            if CurLetter >= len(alphabet):
                CurLetter = (alphabet.index(text[i]) + len(alphabet)) - shift
            encryptedString += alphabet[CurLetter]

    return encryptedString




if __name__ == '__main__':
    direction = input("Enter encrypt or decrypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(ceaser(text,shift,direction))

