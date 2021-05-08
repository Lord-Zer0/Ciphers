# Plaintext

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TEST_STR = "Sphinx of black quartz, judge my vow."
TEST_KEY = 0

def encrypt(plaintext, key = 0):
    # remove spaces, punctuation, and convert to uppercase
    plaintext = plaintext.upper()
    print(plaintext)

    for x in plaintext:
        if x not in ALPHABET:
            print(x)
            plaintext = plaintext.replace(x, '')

    if len(plaintext) < 1:
        return -1
    
    print(plaintext)
    # string is now trimmed, apply key and modify
    # escape for special cases, key must be > 0
    # if 0, return without modifying
    # if > 26, use modulo
    


encrypt(TEST_STR, TEST_KEY)