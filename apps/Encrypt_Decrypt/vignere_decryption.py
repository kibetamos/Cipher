import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vignere_decryption(inputFilePath, outputFilePath, password):
    inputText = ''

    with open(inputFilePath, 'r') as file:
        inputText = file.read()

    originalText = decryptMessage(password, inputText)

    with open(outputFilePath, 'w') as file:
        file.write(originalText)


    with open(outputFilePath, 'r') as file:
        outputFile = file.read()

    return  outputFile


def decryptMessage(key, message):
    translated = []  # stores the encrypted/decrypted message string
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num -= LETTERS.find(key[keyIndex])
            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1

            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)
