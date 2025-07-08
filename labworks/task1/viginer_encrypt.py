def encrypt_vigenere(plaintext, keyword):
    i = 0
    keyword = list(keyword.lower())
    plaintext = list(plaintext.lower())
    if len(keyword) != len(plaintext):
        while len(keyword) <= len(plaintext):
            keyword.append(keyword[i])
            i += 1
    cypher_text = []
    for i in range(len(plaintext)):
        cypher_text.append(chr((ord(keyword[i]) - ord('a') + ord(plaintext[i]) - ord('a')) % 26 + ord('a')))
    print(cypher_text)
    return cypher_text 


encrypt_vigenere("ATTACKATDAWN", "LEMON")