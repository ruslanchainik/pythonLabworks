def caesar_encrypt(plaintext):
    plaintext = list(plaintext) 
    for i in range(len(plaintext)):
        if 65 <= ord(plaintext[i]) <= 88:
            plaintext[i] = chr(ord(plaintext[i]) + 3)
        elif 88 < ord(plaintext[i]) < 91:
            plaintext[i] = chr(ord(plaintext[i]) - 23)
        elif 97 <= ord(plaintext[i]) < 120:
            plaintext[i] = chr(ord(plaintext[i]) + 3)
        elif 120 <= ord(plaintext[i]) < 123:
            plaintext[i] = chr(ord(plaintext[i]) - 23)

    cypher_text = ''.join(plaintext)
    print(cypher_text)
    return cypher_text