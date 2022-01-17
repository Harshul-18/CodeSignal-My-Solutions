# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def solution(inputArray):
    return max([i*j for i, j in zip(inputArray[1:], inputArray[:-1])])