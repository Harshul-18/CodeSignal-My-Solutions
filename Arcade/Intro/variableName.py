# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

def solution(name):
    if name[0].isdigit():
        return False
    for i in name:
        if not (i.isalnum() or i == "_"):
            return False
    return True