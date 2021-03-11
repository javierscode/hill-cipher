#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
import numpy as np

VALID_CHARACTERS = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             '.', ',', ':', '?', ' '])


def get_position(char):
    # Uppercase the char
    char = char.upper()
    # get the position in the array
    position = np.where(VALID_CHARACTERS == char)[0]
    if len(position) > 0:
        return position[0]
    else:
        return -1


# ----------------------------------------------------------------------------


def uoc_hill_genkey(size):
    """
    EXERCISE 1: Hill Key Generation
    :size: matrix size
    :return: size x size matrix containing the key
    """

    # --- IMPLEMENTATION GOES HERE ---
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

    #### IMPLEMENTATION GOES HERE ####

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

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------

    return plaintext


if __name__ == '__main__':
    # my own examples
    matrix = uoc_hill_genkey(2)
    print(matrix)
    print(len(VALID_CHARACTERS))
    print(get_position('_'))
