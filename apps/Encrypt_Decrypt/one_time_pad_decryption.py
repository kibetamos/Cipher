import onetimepad


def one_time_pad_decrytpion(inputFilePath, outputFilePath):
    text = ''
    with open(inputFilePath, 'r') as file:
        cipher = file.read()
    if len(cipher) % 2:
        cipher += ' '
    print(len(cipher), " is the length of the input text")
    msg = onetimepad.decrypt(cipher, 'random')
    print(msg)
    with open(outputFilePath, 'w') as file:
        file.write(msg)
    with open(outputFilePath, 'r') as file:
        outputFile = file.read()

    return outputFile


