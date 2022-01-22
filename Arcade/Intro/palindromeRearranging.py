# Given a string, find out if its characters can be rearranged to form a palindrome.

def solution(inputString):
    return sum(map(lambda x: inputString.count(x) % 2, set(inputString))) <= 1