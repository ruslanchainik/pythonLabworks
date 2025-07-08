def caesar_decrypt(cypher_text):
    cypher_text = list(cypher_text)
    for i in range(len(cypher_text)):
        if 68 <= ord(cypher_text[i]) <= 90:
            cypher_text[i] = chr(ord(cypher_text[i]) - 3)
        elif 65 <= ord(cypher_text[i]) < 68:
            cypher_text[i] = chr(ord(cypher_text[i]) + 23)
        elif 100 <= ord(cypher_text[i]) <= 122:
            cypher_text[i] = chr(ord(cypher_text[i]) - 3)
        elif 97 <= ord(cypher_text[i]) < 100:
            cypher_text[i] = chr(ord(cypher_text[i]) + 23)

    plaintext = ''.join(cypher_text)
    print(plaintext)
    return plaintext