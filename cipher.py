# Plaintext

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TEST_STR = "Sphinx of black quartz, judge my vow."
TEST_KEY = 2

def encrypt(plaintext, key = 0):
    # remove spaces, punctuation, and convert to uppercase
    plaintext = plaintext.upper()

    for x in plaintext:
        if x not in ALPHABET:
            #print(x)
            plaintext = plaintext.replace(x, '')

    if len(plaintext) < 1:
        return -1
    
    print(plaintext)
    # string is now trimmed, apply key and modify
    if key == 0:
        # if 0, return without modifying
        return plaintext
    # use modulo to figure out rotational length
    key = key % 26

    cipher = rotate(ALPHABET, key)
    print(cipher)
    
    # find the position of a letter in the alphabet, then replace it with the corresponding cipher
    for x in plaintext:
        s = ALPHABET.find(x)
        plaintext = plaintext.replace(x, cipher[s])

    print(plaintext)

def decrypt(ciphertext, key):
    key = key % 26
    


def rotate(seq, n):
    return seq[n:] + seq[:n]


encrypt(TEST_STR, TEST_KEY)