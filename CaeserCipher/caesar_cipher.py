alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [' ', '!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '-', '_']


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount = shift_amount*-1
    for item in plain_text:
        if item in alphabet:
            current_position = alphabet.index(item)
            shift_position = current_position + shift_amount
            if shift_position > 25:
                cipher_text += alphabet[(shift_position - 26)]
            else:
                cipher_text += alphabet[shift_position]
        else:
            cipher_text += item
    return cipher_text
