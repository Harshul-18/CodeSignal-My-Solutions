# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

def solution(inputString):
    result = ''
    for i in inputString:
        asci = ord(i)
        if asci == 122:
            asci = 96
        result += chr(asci+1)
    return result