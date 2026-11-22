"""
ASSIGNMENT 3: TEXT ENCODER AND DECODER
Algorithm: Caesar Cipher
Language: Python 3

The Caesar Cipher shifts each alphabetic character by a user-selected
number of positions. Non-alphabetic characters are preserved.
"""

def caesar_cipher(text: str, shift: int) -> str:
    """Return text encoded/decoded using the Caesar Cipher."""
    result = []

    # Normalize large and negative shifts to the alphabet range.
    shift = shift % 26

    for character in text:
        if "A" <= character <= "Z":
            new_position = (ord(character) - ord("A") + shift) % 26
            result.append(chr(new_position + ord("A")))
        elif "a" <= character <= "z":
            new_position = (ord(character) - ord("a") + shift) % 26
            result.append(chr(new_position + ord("a")))
        else:
            # Keep spaces, numbers, punctuation and symbols unchanged.
            result.append(character)

    return "".join(result)


def get_shift() -> int:
    """Ask for a valid integer shift value."""
    while True:
        value = input("Enter the shift key (whole number): ").strip()
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main() -> None:
    print("=" * 48)
    print("       TEXT ENCODER AND DECODER SYSTEM")
    print("              CAESAR CIPHER")
    print("=" * 48)

    while True:
        print("\nMAIN MENU")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            message = input("\nEnter the text to encode: ")
            shift = get_shift()
            encoded = caesar_cipher(message, shift)
            print("\nENCODED MESSAGE:", encoded)

        elif choice == "2":
            message = input("\nEnter the text to decode: ")
            shift = get_shift()
            decoded = caesar_cipher(message, -shift)
            print("\nDECODED MESSAGE:", decoded)

        elif choice == "3":
            print("\nThank you for using the Text Encoder and Decoder System.")
            break

        else:
            print("\nInvalid menu option. Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
