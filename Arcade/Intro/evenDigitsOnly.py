# Check if all digits of the given integer are even.

def solution(n):
    number = n
    digit = n%10
    while digit%2==0 and n != n%10:
        n = n//10
        digit = n%10
    return digit%2==0    