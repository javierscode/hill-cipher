import numpy as np
import sympy as sympy

# Which characters can be encrypted and its position in the array is used to assign them a value.
VALID_CHARACTERS = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             '.', ',', ':', '?', ' '])

# PADDING is used to add an extra character when the Hill cipher requires it.
PADDING = 'X'


# Returns the position of a character in the array of valid characters
def get_position(char):
    # Character is normalized to uppercase
    char = char.upper()
    # Look for the position of the character in the array
    position = np.where(VALID_CHARACTERS == char)[0]
    if len(position) > 0:
        return position[0]
    else:
        return -1


# Splits an array according to size, the last chunk can be smaller than the given size.
def split_array(array, size):
    new_array = []
    temporal_array = []
    for value in array:
        temporal_array.append(value)
        if len(temporal_array) >= size:
            new_array.append(temporal_array)
            temporal_array = []
    if len(temporal_array)> 0:
        new_array.append(temporal_array)
    return new_array


# Returns the inverse matrix of the key. This inverse matrix is used for decryption of ciphertext.
def get_inverse_key(key):
    matrix = sympy.Matrix(key)
    inv_matrix = matrix.inv_mod(len(VALID_CHARACTERS))
    return np.array(inv_matrix).astype(np.int64)

# ----------------------------------------------------------------------------


def uoc_hill_genkey(size):
    """
    EXERCISE 1: Hill Key Generation
    :size: matrix size
    :return: size x size matrix containing the key
    """

    # --- IMPLEMENTATION GOES HERE ---
    # Generates a size x size matrix with random numbers between 0 and the total of valid characters.
    matrix = np.random.randint(len(VALID_CHARACTERS), size=(size, size))
    # --------------------------------

    return matrix


def uoc_hill_cipher(message, key):
    """
    EXERCISE 2: Hill cipher
    :message: message to cipher (plaintext)
    :key: key to use when ciphering the message (as it is returned by 
          uoc_hill_genkey() )
    :return: ciphered text
    """

    ciphertext = ""

    # --- IMPLEMENTATION GOES HERE ---

    # An array is generated with the values assigned to each character of the message.
    message_values = []
    for char in message:
        value = get_position(char)
        message_values.append(value)

    # The array is divided by the size of the key
    splitted_array = split_array(message_values, len(key))

    # For each group of the splitted array, the multiplication is done with the matrix
    # and the module of the number of valid characters is applied.
    for group in splitted_array:

        # If it is the last group and it is smaller than the size of the key,
        # the PADDING is added until the desired size is reached
        if len(group) < len(key):
            while len(group) < len(key):
                group=np.append(group, get_position(PADDING))

        # The multiplication between the group and the matrix the module of the number of valid characters
        new_values = np.dot(key, group) % len(VALID_CHARACTERS)

        # The ciphertext is generated with the new values obtained
        for value in new_values:
            ciphertext = ciphertext + VALID_CHARACTERS[value]

    # --------------------------------

    return ciphertext


def uoc_hill_decipher(message, key):
    """
    EXERCISE 3: Hill decipher
    :message: message to decipher (ciphertext)
    :key: key to use when deciphering the message (as it is returned by 
          uoc_hill_genkey() )
    :return: plaintext corresponding to the ciphertext
    """

    plaintext = ""

    # --- IMPLEMENTATION GOES HERE ---

    # The matrix of the key is inverted
    invers_key = get_inverse_key(key)

    # An array is generated with the values assigned to each character of the message.
    message_values = []
    for char in message:
        value = get_position(char)
        message_values.append(value)

    # The array is divided by the size of the key
    splited_array = split_array(message_values, len(invers_key))

    # For each group of the splitted array, the multiplication is done with the inverted matrix
    # and the module of the number of valid characters is applied.
    for group in splited_array:

        # The multiplication between the group and the inverse matrix + the module of the number of valid characters
        new_values = np.dot(invers_key, group) % len(VALID_CHARACTERS)

        # The plaintext is generated with the new values obtained
        for value in new_values:
            plaintext = plaintext + VALID_CHARACTERS[int(value)]

    # Padding that may be in the text is removed
    while plaintext[len(plaintext)-1] == PADDING:
        plaintext= plaintext[0:len(plaintext)-1]
    # --------------------------------

    return plaintext
