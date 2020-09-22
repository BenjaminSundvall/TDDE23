from string import ascii_uppercase, ascii_lowercase


first_word_chars = ascii_lowercase + "åäö_."
second_word_chars = ascii_uppercase + "ÅÄÖ |"

def split_rec(message):
    """ Splits a message using recursion """

    if not message:
        return '', ''
    else:
        first, second = split_rec(message[1:])

        if message[0] in first_word_chars:
            return message[0] + first, second
        elif message[0] in second_word_chars:
            return first, message[0] + second
        else:
            return first, second

def split_it(message):
    """ Splits a message using iteration """

    first_word = ''
    second_word = ''

    for char in message:
        if char in first_word_chars:
            first_word += char
        elif char in second_word_chars:
            second_word += char

    return first_word, second_word
