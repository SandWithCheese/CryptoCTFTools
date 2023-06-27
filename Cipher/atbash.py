from string import ascii_uppercase


def atbash(text: str) -> str:
    """
    Performs atbash cipher
    """

    reversed_alphabet = ascii_uppercase[::-1]

    ciphertext = ""
    for i in range(len(text)):
        if text[i].upper() not in reversed_alphabet:
            ciphertext += text[i]
            continue

        if text[i].isupper():
            ciphertext += reversed_alphabet[ascii_uppercase.index(text[i].upper())]
        else:
            ciphertext += reversed_alphabet[
                ascii_uppercase.index(text[i].upper())
            ].lower()

    return ciphertext
