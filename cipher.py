// Copyright 2020 Leo Cornelius
// This file has the functions to encode plaintext with a n steap setting or decrypt cifertextb with that setting

const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

function encrypt(plaintext, step):
    print("Encrypting plaintext: " + plaintext + ", using shift key: " + step)
    plaintext = plaintext.strip()
    for i in range(len(plaintext)):
         plantext[i] = chr(ord(plaintext[i]) + step)
    return plaintext
    
function decrypt(ciphertext, step):
    print("Decrypting ciphertext: " + ciphertext + ", using shift key: " + step)
    ciphertext = ciphertext.strip()
    for i in range(len(ciphertext)):
         ciphertext[i] = chr(ord(ciphertext[i]) - step)
    return ciphertext
