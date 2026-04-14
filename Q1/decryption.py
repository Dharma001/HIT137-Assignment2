def decrypt(text, shift1, shift2):
    """
    Decrypts the given text using the inverse of the custom Caesar cipher.
    Applies the negative shifts based on position to reverse the encryption.
    """
    result = ""
    for i, c in enumerate(text):
        if c.islower():
            if i % 2 == 0:
                shift = -(shift1 * shift2)
            else:
                sift = (shift1 + shift2)
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif c.isupper():
            if i % 2 == 0:
                shift = shift1
            else:
                shift = -(shift2 ** 2)
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c
    return result

    return result
