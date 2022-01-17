# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

# This solution is Copied. It's not mine solution
def solution(a, b):
    return sorted(a)==sorted(b) and sum(1 if i!=j else 0 for i, j in zip(a, b))<=2