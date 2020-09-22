def check_type(expression, dictionary):
    """ Checks the type of an element in a logical expression """

    if isinstance(expression, list):
        return interpret(expression, dictionary)
    elif expression in dictionary:
        return dictionary[expression]
    else:
        return expression

def interpret(expressions, dictionary):
    """ Interpets a logical expression and returns its boolean value """

    if isinstance(expressions, str):    # 1 element means it is a boolean value
        return check_type(expressions, dictionary)
    elif len(expressions) == 2:     # 2 elements means it is a NOT operation
        a = check_type(expressions[1], dictionary)

        if a == "true":
            return "false"
        else:
            return "true"
    else:   # 3 elements means it is either an OR or an AND operation
        a = check_type(expressions[0], dictionary)
        b = check_type(expressions[2], dictionary)

        if expressions[1] == "OR":
            if a == "true" or b == "true":
                return "true"
            else:
                return "false"
        elif expressions[1] == "AND":
            if a == "true" and b == "true":
                return "true"
            else:
                return "false"
