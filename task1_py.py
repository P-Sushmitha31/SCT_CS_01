def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def main():
    print("=" * 40)
    print("     Caesar Cipher - Encryption Tool")
    print("=" * 40)

    message = input("\nEnter your message: ")
    shift = int(input("Enter shift value (1-25): "))

    print("\nChoose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        output = caesar_cipher(message, shift, "encrypt")
        print(f"\nEncrypted Message: {output}")
    elif choice == "2":
        output = caesar_cipher(message, shift, "decrypt")
        print(f"\nDecrypted Message: {output}")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()