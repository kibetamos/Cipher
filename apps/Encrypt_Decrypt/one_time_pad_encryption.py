import onetimepad

def one_time_pad_encrytpion(inputFilePath, outputFilePath):
    text = ''
    with open(inputFilePath, 'r') as file:
        text = file.read()
    if len(text)%2:
        text+=' '
    print(len(text), " is the length of the input text")
    cipher = onetimepad.encrypt(text, 'random')
    print("Cipher text is ")
    print(cipher)
    with open(outputFilePath, 'w') as file:
        file.write(cipher)

    with open(outputFilePath, 'r') as file:
        outputFile = file.read()

    return outputFile