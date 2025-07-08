def decrypt_vigenere(ciphertext, keyword):
    i = 0
    keyword = list(keyword.lower())
    ciphertext = list(ciphertext.lower())
    if len(keyword) != len(ciphertext):
        while len(keyword) <= len(ciphertext):
            keyword.append(keyword[i])
            i += 1
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append(chr((ord(ciphertext[i]) - ord(keyword[i]) + 26) % 26 + ord('a')))
    print(plaintext)
    return plaintext

decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
