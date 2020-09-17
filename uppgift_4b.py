def check_type(expression, dictionary):
    if isinstance(expression, list):
        return interpret(expression, dictionary)
    elif expression in dictionary:
        return dictionary[expression]
    else:
        return expression

def interpret(expressions, dictionary):
    """ Docstring """

    if isinstance(expressions, str):          # 1 element
        return check_type(expressions, dictionary)
    elif len(expressions) == 2:                 # 2 elements
        a = check_type(expressions[1], dictionary)

        if a == "true":
            return "false"
        else:
            return "true"
    else:                                       # 3 elements
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
