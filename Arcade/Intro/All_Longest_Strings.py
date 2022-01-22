# Given an array of strings, return another array containing all of its longest strings.

def solution(inputArray):
    maxLength = 0
    for i in inputArray:
        maxLength = max(maxLength, len(i))
    return [*filter(lambda x: len(x) == maxLength, inputArray)]