# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

def solution(inputArray, elemToReplace, substitutionElem):
    if elemToReplace in inputArray:
        inputArray = str(inputArray).replace(str(elemToReplace), str(substitutionElem))
    return eval(str(inputArray))