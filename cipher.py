# Plaintext

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TEST_STR = "Sphinx of black quartz, judge my vow."
TEST_CIP = "YXLQPBSHFNGGQSYGXXBLYFIGQAXSY"
TEST_KEY = 2

def encrypt(plaintext, key = 0):
    # remove spaces, punctuation, and convert to uppercase
    plaintext = plaintext.upper()

    for p in plaintext:
        if p not in ALPHABET:
            #print(p)
            plaintext = plaintext.replace(p, '')

    if len(plaintext) < 1:
        return "string does not contain any recognized letters!"
    
    print(plaintext)
    # string is now trimmed, apply key and modify
    if key == 0:
        # if key 0, return without modifying
        return plaintext
    # use modulo to figure out rotational length
    key = key % 26

    cipher = rotate(ALPHABET, key)
    #print(cipher)
    
    # find the position of a letter in the alphabet, then replace it with the corresponding cipher
    text = list(plaintext)

    for i in range(0,len(text)):
        loc = ALPHABET.find(text[i])
        print(ALPHABET[loc] + ' > ' + cipher[loc])
        text[i] = cipher[loc]
        print(text)

    plaintext = "".join(text)
    print(plaintext)
    #return plaintext


def decrypt(ciphertext, key):
    key = (key + 26) % 26

    cipher = rotate(ALPHABET, key)
    #print(cipher)

    for c in ciphertext:
        loc = cipher.find(c)
        print(ALPHABET[loc])
        ciphertext = ciphertext.replace(c, ALPHABET[loc])
    # find the position of a letter in the cipher and replace with alphabet letter

    print(ciphertext)
    #return ciphertext


def rot13(text):
    return encrypt(text, 13)
    

# rotate a string about n by using the split operand
def rotate(seq, n):
    return seq[n:] + seq[:n]


encrypt(TEST_STR, TEST_KEY)
#print(encrypt(TEST_STR, TEST_KEY))
#print(decrypt(TEST_CIP, TEST_KEY))