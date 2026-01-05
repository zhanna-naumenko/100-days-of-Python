import string

# printing welcoming
print("Welcome to Caesar Cipher!")

# Create a string containing all lowercase letters of the English alphabet
alphabet = string.ascii_lowercase

# Ask the user whether they want to encode (encrypt) or decode (decrypt) a message
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

# Ask the user to enter the text they want to encrypt/decrypt
user_text = input("Type your message: ").lower()

# Ask the user for the shift number (how many positions to move in the alphabet)
shift = int(input("Type the shift number: "))


def caesar_cipher(text, number, cryptic):
    # List to store the numeric positions of each character in the alphabet
    numb_of_position = []

    # String that will store the final encrypted/decrypted word
    new_word = ""

    # If decoding, reverse the shift direction
    if cryptic == "decode":
        number *= -1

    # Convert each character in the text to its index in the alphabet
    for val in text:
        numb_of_position.append(alphabet.index(val))

    # Apply the shift to each index and wrap around using modulo
    list_of_numbers = [(x + number) % len(alphabet) for x in numb_of_position]

    # Convert shifted indices back into letters
    for char in list_of_numbers:
        new_word = new_word + alphabet[char]

    # Display the final result
    print(f"Here is the {cryptic}d result: {new_word}")


# Call the function with user input
caesar_cipher(user_text, shift, direction)
# -------------------------------------------------------------------------
# more Pythonic version

# Constant containing all lowercase English letters
ALPHABET = string.ascii_lowercase


def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts a text using the Caesar cipher.

    :param text: Input message
    :param shift: Number of positions to shift
    :param mode: 'encode' to encrypt, 'decode' to decrypt
    :return: Transformed text
    """

    # Reverse the shift for decoding
    if mode == "decode":
        shift *= -1

    result = ""

    for char in text:
        # Process only alphabetic characters
        if char in ALPHABET:
            original_index = ALPHABET.index(char)
            new_index = (original_index + shift) % len(ALPHABET)
            result += ALPHABET[new_index]
        else:
            # Keep spaces, numbers, and punctuation unchanged
            result += char

    return result


# ---- User input ----
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
user_text = input("Type your message: ").lower()
shift_number = int(input("Type the shift number: "))

# ---- Run cipher ----
output = caesar_cipher(user_text, shift_number, direction)
print(f"Here is the {direction}d result: {output}")