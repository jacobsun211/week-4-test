import string


def caesar(text, offset):
    alphabet = string.ascii_lowercase
    shifted_abc = alphabet[offset:] + alphabet[:offset]
    result = str.maketrans(alphabet, shifted_abc)
    text = text.lower()
    return text.translate(result)


def fence_encrypt(text):
    text = text.replace(" ", "")
    str1 = ''
    str2 = ''
    for i in range(len(text)):
        if i % 2 == 0:
            str1 += text[i]
        else:
            str2 += text[i]
    return str1 + str2


def fence_decrypt(text):
    decrypted = ''
    length = len(text)
    for i in range(length // 2):
        decrypted += text[i]
        decrypted += text[length // 2 + i + (length % 2)]

    if length % 2 == 1:  # adding the last char if the text is odd length
        decrypted += text[length // 2]
    return decrypted
