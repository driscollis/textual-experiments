# cipher.py

import string

numbers = list(range(1, 27))
letter2number_dict = dict(zip(string.ascii_uppercase, numbers))

number2letter_dict = dict(zip(numbers, string.ascii_uppercase))

def encode_message(message):
    encoded_msg = ""
    for letter in message.upper():
        if letter in letter2number_dict:
            encoded_msg += f" {letter2number_dict[letter]} "
        elif letter == " ":
            encoded_msg += "\n"

    print(encoded_msg)
    return encoded_msg

def decode_message(encoded_msg):
    words = [word.strip() for word in encoded_msg.split("\n")]

    decoded = ""
    for word in words:
        numbers = [int(number) for number in word.split()]
        for number in numbers:
            if number in number2letter_dict:
                decoded += number2letter_dict[number]
        decoded += "\n"

    print(decoded)
    return decoded

encoded_msg = encode_message("Hello Python")
decode_message(encoded_msg)