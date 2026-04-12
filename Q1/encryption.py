def encrypt(text, shift1, shift2):
    """
    Encrypts the given text using a custom Caesar cipher with position-based shifts.
    For lowercase letters: even positions use shift1 * shift2, odd positions use -(shift1 + shift2)
    For uppercase letters: even positions use -shift1, odd positions use shift2 ** 2
    Non-alphabetic characters remain unchanged.
    """
    result = ""
    for i, c in enumerate(text):
        if c.islower():
            if i % 2 == 0:
                shift = shift1 * shift2
            else:
                shift = -(shift1 + shift2)
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif c.isupper():
            if i % 2 == 0:
                shift = -shift1
            else:
                shift = shift2 ** 2
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c
    return result