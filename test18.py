letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(text, shift):
    newMessage = ""
    for letter in text:
        if letter in letters:
            position = letters.index(letter)
            newPosition = (position + shift) % 26
            newMessage += letters[newPosition]

        else:
            newMessage += letter

    print(f"Encrypted message is: {newMessage}")

def decryption(cipherText, shift):
    text = ""
    for letter in cipherText:
        if letter in letters:
            position = letters.index(letter)
            newPosition = (position - shift) % 26
            text += letters[newPosition]

        else:
            text += letter

    print(f"Decrypted message is: {text}")

isEnd = False

while not isEnd: 

    beginInput = input("Type \'encrpt\' for encryption and type \'decrypt\' for decryption: ")
    message = input("Type the message: ")
    shiftNo = int(input("Enter the shift number: "))

    if beginInput == 'encrypt':
        encryption(text = message, shift = shiftNo)

    elif beginInput == 'decrypt':
        decryption(cipherText = message, shift = shiftNo)

    endInput = input("\nType \'yes\' for start again and type \'no\' for exit: ")

    if endInput == 'no':
        isEnd = True
        break
