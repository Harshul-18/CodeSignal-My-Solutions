# Some phone usage rate may be described as follows:

# first minute of a call costs min1 cents,
# each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?

def solution(min1, min2_10, min11, s):
    if s<min1:
        return 0
    elif s>=min1 and s<=min1+9*min2_10:
        return 1+(s-min1)//min2_10
    return 10+(s-min1-9*min2_10)//min11