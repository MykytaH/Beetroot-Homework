incoming = input("Enter string of ( and ): ")


def nested_parentheses(incoming):
    opening_brackets = []
    for bracket_1 in incoming:
        if bracket_1 == "(":
            opening_brackets.append(bracket_1)
        else:
            if not opening_brackets:
                return False
            bracket_2 = opening_brackets.pop()
            if bracket_2 == '(':
                if bracket_1 != ")":
                    return False
    return True


print(nested_parentheses(incoming))
