# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

def solution(inputString):
    length = len(inputString)
    temp = []
    for i in range(length):
        if (inputString[i] == "("):
            temp.append(i)
        elif (inputString[i] == ")"):
            dummy = inputString[temp[-1]:i+1]
            inputString = inputString[:temp[-1]] + dummy[::-1] + inputString[i + 1:]
            del temp[-1]
    res = ""
    for i in range(length):
        if (inputString[i] != ')' and inputString[i] != '('):
            res += (inputString[i])
    return res