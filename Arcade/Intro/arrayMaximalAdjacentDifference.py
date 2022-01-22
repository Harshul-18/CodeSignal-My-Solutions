# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

def solution(inputArray):
    maxSum = 0
    for i in range(len(inputArray)-1):
        maxSum = max(abs(inputArray[i]-inputArray[i+1]), maxSum)
    return maxSum