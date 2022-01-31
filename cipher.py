def encrypt(text, s):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text):
    result = []
    for s in range(26):
        temp = ''
        for char in text:
            if char.isupper():
                temp += chr((ord(char) + s - 65) % 26 + 65)
            elif char.islower():
                temp += chr((ord(char) + s - 97) % 26 + 97)
            else:
                temp += char
        result.append(temp)
    return result
