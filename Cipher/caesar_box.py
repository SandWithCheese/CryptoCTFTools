def caesar_box_encrypt(plaintext: str, column: int) -> str:
    """
    Performs caesar box cipher with a given column
    """

    if column == 1:
        return plaintext

    ciphertext = ""
    for i in range(column):
        idx = i
        while idx < len(plaintext):
            ciphertext += plaintext[idx]
            idx += column

    return ciphertext


def caesar_box_decrypt(ciphertext: str, column: int) -> str:
    """
    Decrypts caesar box cipher with a given column
    """

    if column == 1:
        return ciphertext

    plaintext = ""

    row, excess_row = divmod(len(ciphertext), column)
    if excess_row > 0:
        row += 1

    for i in range(row):
        idx = i
        excess_counter = 0
        while idx < len(ciphertext):
            if i == row - 1 and excess_counter >= excess_row:
                break

            plaintext += ciphertext[idx]

            if excess_counter < excess_row:
                idx += row
                excess_counter += 1
            else:
                idx += row - 1

    return plaintext


def caesar_box_bruteforce(ciphertext: str) -> str:
    """
    Returns a list of all possible caesar box cipher
    """

    possible_cipher = ["" for i in range(len(ciphertext) - 1)]
    for i in range(1, len(ciphertext)):
        possible_cipher[i - 1] = caesar_box_decrypt(ciphertext, i)

    return possible_cipher
