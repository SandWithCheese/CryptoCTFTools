def rail_fence_encrypt(plaintext: str, rails: int, offset: int = 0) -> str:
    """
    Performs rail fence cipher with a given number of rails and an offset
    """

    plaintext = "\0" * offset + plaintext
    period = 2 * (rails - 1)

    arr = [[] for _ in range(rails)]
    idx = 0
    for i in range(len(plaintext)):
        if i % period >= period // 2:
            isDown = False
        else:
            isDown = True

        arr[idx].append(plaintext[i])

        if isDown:
            idx += 1
        else:
            idx -= 1

    ciphertext = ""
    for sub_arr in arr:
        for char in sub_arr:
            ciphertext += char

    return ciphertext.replace("\0", "")


def get_encrypted_array(plaintext: str, rails: int, offset: int = 0) -> list[chr]:
    """
    Helper function to decrypt rail fence cipher
    """

    plaintext = "\0" * offset + plaintext
    period = 2 * (rails - 1)

    arr = [[] for _ in range(rails)]
    idx = 0
    for i in range(len(plaintext)):
        if i % period >= period // 2:
            isDown = False
        else:
            isDown = True

        arr[idx].append(plaintext[i])

        if isDown:
            idx += 1
        else:
            idx -= 1

    return arr


def rail_fence_decrypt(ciphertext: str, rails: int, offset: int = 0) -> str:
    """
    Decrypts rail fence cipher with a given number of rails and an offset
    """

    period = 2 * (rails - 1)
    temp = get_encrypted_array(ciphertext, rails, offset)

    arr = [[] for _ in range(len(temp))]
    idx = 0
    for i in range(offset):
        if i % period >= period // 2:
            isDown = False
        else:
            isDown = True

        arr[idx].append("\0")

        if isDown:
            idx += 1
        else:
            idx -= 1

    idx = 0
    for i in range(len(arr)):
        length = len(arr[i])
        for _ in range(length, len(temp[i])):
            arr[i].append(ciphertext[idx])
            idx += 1

    for i in range(len(arr)):
        while "\0" in arr[i]:
            arr[i].remove("\0")

    if offset % period >= period // 2:
        idx = period // 2 - offset % (period // 2)
    else:
        idx = offset % (period // 2)

    plaintext = ""
    i = offset % period
    while sum_len(arr) != 0:
        if i % period >= period // 2:
            isDown = False
        else:
            isDown = True

        if arr[idx] != []:
            plaintext += arr[idx][0]
            arr[idx] = arr[idx][1:]

        if isDown:
            idx += 1
        else:
            idx -= 1
        i += 1

    return plaintext


def rail_fence_bruteforce(ciphertext: str) -> list[str]:
    """
    Returns a list of all possible rail fence cipher
    """

    rails_range = len(ciphertext) + 1
    possible_cipher = []
    for i in range(2, rails_range):
        for j in range(rails_range - 1):
            result = rail_fence_decrypt(ciphertext, i, j)
            if result not in possible_cipher:
                possible_cipher.append(result)

    return possible_cipher


def sum_len(arr: list[list]) -> int:
    """
    Returns a sum of length of every list inside a list
    """

    total = 0
    for a in arr:
        total += len(a)

    return total
