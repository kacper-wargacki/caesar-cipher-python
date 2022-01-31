from tqdm import tqdm

import cipher


def checkEncryption():
    textsToEncrypt = []
    keys = []
    encryptedTexts = []
    file = open('testFile.txt', 'r')
    lines = file.read().splitlines()
    for line in lines:
        splitString = line.split('\t')
        textsToEncrypt.append(splitString[0])
        keys.append(splitString[1])
        encryptedTexts.append(splitString[2])
    error = False
    testsLen = len(textsToEncrypt)
    for i in tqdm(range(testsLen)):
        result = cipher.encrypt(textsToEncrypt[i], int(keys[i]))
        if result != encryptedTexts[i]:
            print(result, '|', encryptedTexts[i], '\n')
            error = True
    if error:
        print('Znaleziono błąd w funkcji szyfrującej')
    else:
        print('Nie znaleziono błędów w funkcji szyfrującej')
