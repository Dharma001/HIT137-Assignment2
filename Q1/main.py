from file_handler import read_file, write_file
from encryption import encrypt
from decryption import decrypt
from verify import verify


def main():
    """
    Main function to perform encryption and decryption of text.
    Reads raw text, encrypts it with user-provided shifts, decrypts it back, and verifies.
    """
    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
    except ValueError:
        print("Invalid input. Please enter integers for shifts.")
        return

    # Read the original text
    text = read_file("Q1/raw_text.txt")

    # Encrypt the text
    encrypted = encrypt(text, shift1, shift2)
    write_file("Q1/encrypted_text.txt", encrypted)

    # Decrypt the encrypted text
    decrypted = decrypt(encrypted, shift1, shift2)
    write_file("Q1/decrypted_text.txt", decrypted)

    # Verify if decryption matches original
    if verify(text, decrypted):
        print("Decryption successful")
    else:
        print("Decryption failed")


if __name__ == "__main__":
    main()