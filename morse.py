#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Gabby collabs: Sondos and Shanquel, got help from Piero'
__references__ = 'Piero'

from morse_dict import MORSE_2_ASCII

import re


def decode_bits(bits):
    # removes starting and ending extra's 0
    bits = bits.strip("0")

    # find the least amount of occurrences of either a 0 or 1
    time_unit = min([len(g) for g in re.findall(r"1+|0+", bits)])
    morse_bits = bits.replace("0000000"*time_unit, "   ")
    morse_bits = morse_bits.replace("000"*time_unit, " ")
    morse_bits = morse_bits.replace("111"*time_unit, "-")
    morse_bits = morse_bits.replace("1"*time_unit, ".")
    morse_bits = morse_bits.replace("0"*time_unit, "")

    # decoded into the morse
    return morse_bits


def decode_morse(morse):
    decoded_message = ''

    # Iterate through morse code and match the words
    for word in morse.strip().split("   "):
        for char in word.split(" "):
            decoded_message += MORSE_2_ASCII[char]
        decoded_message += " "
    return decoded_message.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
