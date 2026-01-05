import string

# printing welcoming
print("Welcome to Caesar Cipher!")

# Create a string containing all lowercase letters of the English alphabet
alphabet = string.ascii_lowercase


def caesar_cipher(text, number, cryptic):

    # String that will store the final encrypted/decrypted word
    new_word = ""

    # If decoding, reverse the shift direction
    if cryptic == "decode":
        number *= -1

    for letter in text:
        # Process only alphabetic characters
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + number
            shifted_position %= len(alphabet)
            new_word += alphabet[shifted_position]
        else:
            # Keep spaces, numbers, and punctuation unchanged
            new_word += letter

    print(f"Here is the {cryptic}d result: {new_word}")

in_program = True

while in_program:
    # Ask the user whether they want to encode (encrypt) or decode (decrypt) a message
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    # Ask the user to enter the text they want to encrypt/decrypt
    user_text = input("Type your message: ").lower()

    # Ask the user for the shift number (how many positions to move in the alphabet)
    shift = int(input("Type the shift number: "))

    # Call the function with user input
    caesar_cipher(user_text, shift, direction)

    restart = input("Please type 'yes' if you want to go again and 'no' if you want to exit the program: ").lower()

    if restart == "no":
        in_program = False
        print("Goodbye!")




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
