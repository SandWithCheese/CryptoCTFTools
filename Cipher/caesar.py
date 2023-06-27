from string import ascii_uppercase


def caesar(text: str, key: int) -> str:
    """
    Performs caesar cipher on a text with a given key
    """

    substitute_alphabet = ""
    for i in range(key, len(ascii_uppercase) + key):
        substitute_alphabet += ascii_uppercase[i % 26]

    ciphertext = ""
    for i in range(len(text)):
        if text[i].upper() not in substitute_alphabet:
            ciphertext += text[i]
            continue

        if text[i].isupper():
            ciphertext += substitute_alphabet[ascii_uppercase.index(text[i].upper())]
        else:
            ciphertext += substitute_alphabet[
                ascii_uppercase.index(text[i].upper())
            ].lower()

    return ciphertext


def caesar_bruteforce(text: str) -> list[str]:
    """
    Returns a list of all possible caesar cipher
    """
    
    possible_cipher = ["" for i in range(26)]
    for i in range(26):
        possible_cipher[i] = caesar(text, i)

    return possible_cipher
