# Given an integer n, return the largest number that contains exactly n digits.

def solution(n):
    return sum(9*(10**i) for i in range(n))